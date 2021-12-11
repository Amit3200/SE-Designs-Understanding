import pika
import sys

exchange       = 'notify_upload'
exchange_type  = 'topic'
connection     = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel        = connection.channel()
channel.exchange_declare(exchange = exchange, exchange_type = exchange_type)
result         = channel.queue_declare('', exclusive = True)
queue_name     = result.method.queue

# binding_keys   = ["misc.*"]
binding_keys = sys.argv[1:]

for binding_key in binding_keys:
    print("binding : ",binding_key)
    channel.queue_bind(exchange = exchange, queue = queue_name, routing_key = binding_key)

def callback(ch, method, properties, body):
    print("[x] Receive message %r:%r"%(method.routing_key, body))

channel.basic_consume(queue = queue_name, on_message_callback = callback, auto_ack = True)
channel.start_consuming()