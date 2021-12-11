import pika
import json

class MessageProducer:
    def __init__(self):
        self.message        = None
        self.exchange       = 'notify_upload'
        self.exchange_type  = 'topic'
        self.routing_key    = 'misc.engineer'

    def clean_params(self, params):
        if type(params) == dict:
            return json.dumps(params)
        elif type(params) == str:
            return params
        return None

    def send(self, content):
        connection          = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel             = connection.channel()
        self.message        = self.clean_params(content)
        if content.get('department').lower() in ['engineer','it','tech']:
            self.routing_key = '*.engineer'
        else:
            self.routing_key = 'misc.*'
        channel.exchange_declare(exchange = self.exchange, exchange_type = self.exchange_type)
        channel.basic_publish(exchange = self.exchange, routing_key = self.routing_key, body = self.message)
        print("[x] Sent message %r:%r"%(self.routing_key, self.message))
        connection.close()
        return 200
    
