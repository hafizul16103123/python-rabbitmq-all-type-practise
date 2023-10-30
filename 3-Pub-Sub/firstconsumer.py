from aio_pika import ExchangeType
from rmq_channel import rmq_channel

# Define a callback function for handling received messages
def on_message_received(ch, method, properties, body):
    print(f"firstconsumer - Received new message: {body}")
    
connection, channel = rmq_channel()

# Declare a fanout exchange named 'pubsub'
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

# Declare an exclusive queue for the first consumer
queue = channel.queue_declare(queue='', exclusive=True)

# Bind the exclusive queue to the 'pubsub' fanout exchange
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

# Set up a basic consumer for the exclusive queue, invoking the on_message_received callback
channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("Starting Consuming")
channel.start_consuming()
