# from processx.worker import Worker

# # User-defined functions for different queues
# def process_image_job(job):
#     print(f"Processing image job: {job}")

# def process_video_job(job):
#     print(f"Processing video job: {job}")

# # Define the queue to function mapping
# consumer_map = {
#     "image_queue": process_image_job,
#     "video_queue": process_video_job
# }

# # Instantiate the Worker with the consumer map and thread configuration
# worker = Worker(consumer_func_map=consumer_map, thread_count=3)

# # Start consuming jobs from the defined queues
# worker.start()
