import pika


def rmq_channel():
    credentials = pika.PlainCredentials('admin', 'admin-pass')
    parameters = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return connection,channel