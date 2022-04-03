from message_queue import Subscriber, qm1, qm2

s1 = Subscriber(1,qm1)

s1.add_queue_to_consume(1)
s1.add_queue_to_consume(2)
s1.consume()


s2 = Subscriber(1,qm1)
s2.add_queue_to_consume(4)
s2.add_queue_to_consume(1)
s2.add_queue_to_consume(2)
s2.add_queue_to_consume(3)
s2.consume()