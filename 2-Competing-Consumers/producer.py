from rmq_channel import rmq_channel
import time
import random

# Establish a connection and create a channel using a helper function (rmq_channel)
connection, channel = rmq_channel()

# Declare a queue named 'letterbox'
channel.queue_declare(queue='letterbox')

# Initialize a variable to track the message ID
messageId = 1

# Continuously send messages in a loop
while True:
    # Construct the message with a unique message ID
    message = f"Sending Message Id: {messageId}"

    # Publish the message to the 'letterbox' queue with an empty exchange
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

    # Print a message indicating that the message was sent
    print(f"Sent message: {message}")

    # Sleep for a random time interval (1 to 4 seconds) before sending the next message
    time.sleep(random.randint(1, 4))

    # Increment the message ID for the next message
    messageId += 1

