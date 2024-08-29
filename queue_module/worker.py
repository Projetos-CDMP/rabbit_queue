import pika
import os
import time
import logging
logging.basicConfig(level=logging.INFO)

def callback(ch, method, properties, body):
    logging.info(f"Received {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def connect_to_rabbitmq(retries=5, delay=5):
    rabbitmq_host = os.getenv('RABBITMQ_HOST')
    rabbitmq_port = int(os.getenv('RABBITMQ_PORT'))
    rabbitmq_user = os.getenv('RABBITMQ_DEFAULT_USER')
    rabbitmq_pass = os.getenv('RABBITMQ_DEFAULT_PASS')

    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    
    for attempt in range(retries):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials))
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            logging.info(f"Connection attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise Exception("Failed to connect to RabbitMQ after several attempts")

def main():
    logging.info('STARTING WORKER')
    connection = connect_to_rabbitmq()
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    logging.info('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()