import sys
import pika


# подключение
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello World! 5"
# exchange - имя точки обмена, routing_key - ключ маршрутизации, с которым сообщение будет опубликовано
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print(" [x] Sent %r" % (message,))

connection.close()