import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(10)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_consume('hello', callback)
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='task_queue', durable=True)
                      # auto_ack=True)

channel.start_consuming()