
from rmq_channel import rmq_channel

# Define a callback function for handling received messages
def on_message_received(ch, method, properties, body):
    print(f"Received new message: {body}")

# Establish a connection and create a channel using a helper function (rmq_channel)
connection, channel = rmq_channel()

# Declare a queue named 'letterbox',if not exists then only will be create
channel.queue_declare(queue='letterbox')

# Set up a basic consumer that listens to the 'letterbox' queue and invokes the
# on_message_received callback function for each received message
channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)

# Indicate that the consumer is starting
print("Starting Consuming")

# Start the consumer, which will continuously listen for and process messages
channel.start_consuming()
