# worker_registry.py

from custom_workers import ImageProcessingWorker, VideoProcessingWorker

class WorkerRegistry:
    def __init__(self):
        self.worker_map = {}

    def register_worker(self, worker_class):
        """Register a worker class and its associated queue."""
        if worker_class.queue_name:
            self.worker_map[worker_class.queue_name] = worker_class
            print(f"Registered worker {worker_class.__name__} for queue {worker_class.queue_name}")

    def get_worker_for_queue(self, queue_name):
        """Retrieve the worker class for a specific queue."""
        return self.worker_map.get(queue_name)

    def auto_register_all_workers(self):
        """Automatically find and register all workers that subclass BaseWorker."""
        print(BaseWorker)
        for subclass in BaseWorker.__subclasses__():
            self.register_worker(subclass)

# Create the registry and register workers
worker_registry = WorkerRegistry()
worker_registry.auto_register_all_workers()
