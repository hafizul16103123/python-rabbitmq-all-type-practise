1. General Queue:
    Producer:
        steps:
            1. channel.queue_declare(queue='letterbox')
            2. channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    Consumer:
        steps: 
            1. channel.queue_declare(queue='letterbox')
            2. channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received) 

2. Worker queue:
    Producer:
        steps:
            1. channel.queue_declare(queue='letterbox')
            2. channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    Consumer:
        steps: 
            1. channel.queue_declare(queue='letterbox')
            2. channel.basic_qos(prefetch_count=1)
            3. channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)       

 3. Pubsub:
    Producer:
        steps:
            1. channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
            2. channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    Consumer:
        steps: 
            1. channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
            2. queue = channel.queue_declare(queue='', exclusive=True)
            3. channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
            4. channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)"# python-rabbitmq-all-type-practise" 
"# python-rabbitmq-all-type-practise" 
