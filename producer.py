import pika

rabbit_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = rabbit_connection.channel()

def create_queue(name: str):
    channel.queue_declare(queue=name)

def send_msg(msg: str, queue: str):
    channel.basic_publish(exchange='', routing_key=queue, body=msg)
    print("{} sent to: {}".format(msg, queue))
    rabbit_connection.close()

if __name__ == '__main__':
    create_queue('halo_Q')
    send_msg('hola', 'halo_Q')


