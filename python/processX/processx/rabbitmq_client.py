import pika

class RabbitMQClient:
    def __init__(self, queue_name):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.queue_name = queue_name
        self.channel.queue_declare(queue = self.queue_name)
    
    def get_job(self):
        method_frame, header_frame, body = self.channel.basic_get(queue = self.queue_name)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            return body
        return None
