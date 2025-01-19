import json
import threading
import time
from .rabbitmq_client import RabbitMQClient
from .logger import get_logger
from .thread_pool import ThreadPool

class Worker:
    def __init__(self, consumer_func_map, thread_count=1, retry_delay=5):
        self.consumer_func_map = consumer_func_map
        self.thread_count = thread_count
        self.retry_delay = retry_delay
        self.stop_event = threading.Event()
        self.logger = get_logger()
        self.thread_pool = ThreadPool(num_threads=self.thread_count)

    def start(self):
        for queue_name in self.consumer_func_map.keys():
            self.logger.info(f"Starting {self.thread_count} worker threads for queue '{queue_name}'.")
            for _ in range(self.thread_count):
                threading.Thread(target=self._consume_jobs, args=(queue_name,)).start()

        try:
            while True:
                time.sleep(1)  # Keep the main thread alive
        except KeyboardInterrupt:
            self.logger.info("Received KeyboardInterrupt. Stopping all workers...")
            self.stop_event.set()  # Signal all threads to stop
            self.thread_pool.handle_keyboard_interrupt()

    def _consume_jobs(self, queue_name):
        rabbitmq_client = RabbitMQClient(queue_name=queue_name)

        while not self.stop_event.is_set():
            try:
                job = rabbitmq_client.get_job()  # Modify this method to handle blocking calls
                if job:
                    self.logger.info(f"Processing job from queue '{queue_name}'.")
                    try:
                        self.thread_pool.add_task(self.process_job, job)
                    except Exception as e:
                        self.logger.error(f"Error processing job from queue '{queue_name}': {e}")
                else:
                    self.logger.info(f"No jobs in queue '{queue_name}', retrying in {self.retry_delay} seconds...")
                    time.sleep(self.retry_delay)

            except Exception as e:
                self.logger.error(f"Error fetching job from queue '{queue_name}': {e}")
                time.sleep(1)  # Wait before retrying on error

            # Check stop event periodically to allow for graceful shutdown
            time.sleep(0.1)

        self.logger.info(f"Worker for queue '{queue_name}' is stopping.")

    def process_job(self, job):
        job = json.loads(job)
        consumer_func = self.consumer_func_map.get(job['job_type'])
        if consumer_func:
            try:
                consumer_func(job)
                self.logger.info(f"Completed job {job['job_id']}.")
            except Exception as e:
                self.logger.error(f"Error processing job {job['job_id']}: {e}")
