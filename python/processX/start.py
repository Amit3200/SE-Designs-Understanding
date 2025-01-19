# start.py
import json
import time
from processx.worker import Worker
from processx.config import Config
from processx.logger import get_logger

logger = get_logger()

# Example consumer function that will process the job
def image_processing_consumer(job):
    logger.info(f"Processing job: {job['job_id']} with data: {job['data']}")
    # Simulate some processing time
    time.sleep(2)
    logger.info(f"Completed job: {job['job_id']}")

def main():
    # Define a mapping of job types to consumer functions
    consumer_func_map = {
        "image_processing": image_processing_consumer
    }

    # Create and start the worker
    worker = Worker(consumer_func_map, thread_count=Config.THREAD_COUNT)
    worker.start()

    logger.info("Worker started. Press Ctrl+C to stop.")

    try:
        # Keep the main thread alive to listen for keyboard interrupts
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Received KeyboardInterrupt. Stopping all workers...")
        worker.stop()  # Stop the worker gracefully

if __name__ == "__main__":
    main()
