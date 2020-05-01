from kafka import KafkaConsumer
from kafka import KafkaClient

topic_name = "test-topic-2"

#kafka = KafkaClient("localhost:9092")
consumer = KafkaConsumer(topic_name, bootstrap_servers="localhost:9092")

print ("Created consumer for topic: [%s]" % ( topic_name))
print ("Waiting for messages...")

for msg in consumer:
    print (msg.value)
