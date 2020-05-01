import json

from kafka import KafkaProducer
from datetime import datetime
import time
producer = KafkaProducer(bootstrap_servers="localhost:9092")

# while True:
for _ in range(10000):
    '''
        1. books
        2. toys
        3. groceries
        4. apparel
        5. electronics
    '''
    message = dict()
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-28T%H:%M:%S.%f")[:-3] + "Z"
    message = {
        "timestamp": dt_string,
        "event": "product_review",
        "product_id": "123475",
        "product_name": "Harry Potter",
        "product_review": "Bad book, I did not like it",
        "product_catalog": "books"
    }
    print("Date and TIme: ", dt_string)
    # time.sleep(2)
    json_str = json.dumps(message)
    msg = producer.send('test', str.encode(json_str)).get(timeout=30)
    print(msg)