import pika
import sys
import os
rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = rabbit_connection.channel()

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def receive_message(queue: str):
    channel.basic_consume(queue, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        receive_message('halo_Q')
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)