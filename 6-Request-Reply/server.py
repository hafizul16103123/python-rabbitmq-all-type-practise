from rmq_channel import rmq_channel

def on_request_message_received(ch, method, properties, body):
    print(f"Received Request: {properties.correlation_id}")
    # publish reply to requester using reply-queue
    ch.basic_publish('', routing_key=properties.reply_to, body=f'Hey its your reply to {properties.correlation_id}')

channel = rmq_channel()

channel.queue_declare(queue='request-queue')

channel.basic_consume(queue='request-queue', auto_ack=True,
    on_message_callback=on_request_message_received)

print("Starting Server")

channel.start_consuming()