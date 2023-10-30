from rmq_channel import rmq_channel
from pika.exchange_type import ExchangeType

connection, channel = rmq_channel()
# Declare a fanout exchange named 'pubsub'
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = "Hello, I want to broadcast this message"
# Publish the message to the 'pubsub' fanout exchange with an empty routing key
channel.basic_publish(exchange='pubsub', routing_key='', body=message)

print(f"Sent message: {message}")

connection.close()
