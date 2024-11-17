import threading
import queue
import time
from .logger import get_logger

class ThreadPool:
    def __init__(self, num_threads):
        """
        Initialize the thread pool with a specified number of threads.
        :param num_threads: Number of threads in the pool.
        """
        self.tasks = queue.Queue()  # Queue to hold tasks
        self.threads = []
        self.logger = get_logger()
        self.stop_event = threading.Event()

        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self):
        """Thread worker function to process tasks from the queue."""
        while not self.stop_event.is_set():
            try:
                task, args = self.tasks.get(timeout=1)  # Wait for a task
                self.logger.info(f"Thread {threading.current_thread().name} processing task.")
                task(*args)  # Execute the task
                self.tasks.task_done()  # Mark the task as done
            except queue.Empty:
                continue  # No tasks in the queue

    def add_task(self, task, *args):
        """Add a new task to the queue."""
        self.tasks.put((task, args))  # Enqueue the task
        self.logger.info(f"Task added to the queue: {task.__name__}")

    def wait_completion(self):
        """Block until all tasks in the queue have been processed."""
        self.tasks.join()  # Block until all tasks are done

    def stop(self):
        """Stop the thread pool and wait for all threads to finish."""
        self.stop_event.set()  # Signal threads to stop
        for thread in self.threads:
            thread.join()  # Wait for each thread to finish
        self.logger.info("All threads have been stopped.")

    def handle_keyboard_interrupt(self):
        """Handle KeyboardInterrupt to stop the thread pool gracefully."""
        try:
            while not self.stop_event.is_set():
                time.sleep(1)  # Keep the main thread alive
        except KeyboardInterrupt:
            self.logger.info("Received KeyboardInterrupt. Stopping all workers...")
            self.stop()  # Stop the thread pool
