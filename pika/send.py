import pika

# подключение
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

# создание очереди
channel.queue_declare(queue='hello')

# exchange - точка обмена | routing_key - имя очереди
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()
