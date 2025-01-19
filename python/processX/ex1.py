# example.py

from processx.job import Job

def main():
    # Create jobs and publish them to the RabbitMQ queue
    for i in range(5):
        job_data = {"image_path": f"path/to/image_{i}.jpg"}
        print(job_data)
        job = Job(job_type="image_processing", data=job_data)
        Job.publish_job(job=job, queue_name="image_processing")

if __name__ == "__main__":
    print("Test")
    main()
