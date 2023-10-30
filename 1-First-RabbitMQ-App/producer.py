from rmq_channel import rmq_channel

# Establish a connection and create a channel using a helper function (rmq_channel)
connection, channel = rmq_channel()

# Declare a queue named 'letterbox'
channel.queue_declare(queue='letterbox')

# Define the message you want to send
message = "Hello, this is my first message"

# Publish the message to the 'letterbox' queue with an empty exchange (default)
channel.basic_publish(exchange='', routing_key='letterbox', body=message)

# Print a message indicating that the message was sent
print(f"Sent message: {message}")

# Close the connection to RabbitMQ when you're done
connection.close()
