import pika
import os
import logging

logging.basicConfig(level=logging.INFO)

# Get RabbitMQ connection parameters from environment variables
rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_port = int(os.getenv('RABBITMQ_PORT'))
rabbitmq_user = os.getenv('RABBITMQ_DEFAULT_USER')
rabbitmq_pass = os.getenv('RABBITMQ_DEFAULT_PASS')

logging.info(f"Connecting to RabbitMQ at {rabbitmq_host}:{rabbitmq_port} with user {rabbitmq_user}")

# Connect to RabbitMQ server
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials))
channel = connection.channel()

logging.info("Connected to RabbitMQ")

# Declare the queue
channel.queue_declare(queue='task_queue', durable=True)
logging.info("Declared queue 'task_queue'")

# Send a message to the queue
message = os.getenv('MESSAGE', 'Hello, RabbitMQ!')
logging.info(f"Using message: {message}")
channel.basic_publish(exchange='', routing_key='task_queue', body=message)
logging.info(f"Sent message: {message}")

# Close the connection
connection.close()
logging.info("Closed connection to RabbitMQ")