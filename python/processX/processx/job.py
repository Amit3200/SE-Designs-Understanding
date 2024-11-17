import uuid
import time
import json
import pika  # Make sure to install the pika library for RabbitMQ interaction
from .config import Config

class Job:
    def __init__(self, job_type, data, retries=0, max_retries=Config.MAX_RETRY):
        self.job_id = str(uuid.uuid4())  # Unique job identifier
        self.job_type = job_type
        self.data = data
        self.retries = retries
        self.max_retries = max_retries
        self.created_at = time.time()
        self.status = 'pending'  # Job status (pending, in_progress, completed, failed)

    def to_dict(self):
        return {
            'job_id': self.job_id,
            'job_type': self.job_type,
            'data': self.data,
            'retries': self.retries,
            'max_retries': self.max_retries,
            'created_at': self.created_at,
            'status': self.status
        }

    @staticmethod
    def from_dict(data):
        job = Job(
            job_type=data['job_type'],
            data=data['data'],
            retries=data.get('retries', 0),
            max_retries=data.get('max_retries', 3)
        )
        job.job_id = data['job_id']
        job.created_at = data['created_at']
        job.status = data['status']
        return job

    @staticmethod
    def publish_job(queue_name = None, job = None):
        queue_name = queue_name or Config.QUEUE_NAME  # Use config queue name if none provided
        """Publish a job to the specified RabbitMQ queue."""
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # Update with your RabbitMQ server details
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)  # Ensure the queue exists

        channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(job.to_dict()),
            properties=pika.BasicProperties(
                delivery_mode=2,  # Make message persistent
            )
        )

        connection.close()
        print(f"Published job {job.job_id} to queue '{queue_name}'.")
