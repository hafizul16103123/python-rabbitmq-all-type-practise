import pika
from rmq_channel import rmq_channel
import uuid

def on_reply_message_received(ch, method, properties, body):
    print(f"reply recieved: {body}")

connection , channel = rmq_channel()

#declare a reply queue that the replier will use to send back reply.
reply_queue = channel.queue_declare(queue='', exclusive=True)
channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True,
    on_message_callback=on_reply_message_received)

#declare a queue to publish message
channel.queue_declare(queue='request-queue')
cor_id = str(uuid.uuid4())
print(f"Sending Request: {cor_id}")
channel.basic_publish('', routing_key='request-queue', properties=pika.BasicProperties(
    reply_to=reply_queue.method.queue,
    correlation_id=cor_id
), body='Can I request a reply?')

print("Starting Client")

channel.start_consuming()