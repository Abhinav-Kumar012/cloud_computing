import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_direct', exchange_type='direct')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='logs_direct',
                      routing_key=routing_key,
                      body=message)

print(f" [x] Sent '{message}' with routing key '{routing_key}'")
connection.close()

