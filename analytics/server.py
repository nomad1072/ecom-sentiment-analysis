from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from typing import List, Dict

from druid.sentiment import sentiment_query
from druid.eventCount import event_count_query
from druid.timeseries import timeseries_query_string
from druid.topN import topN_query_string

import requests
import json

app = Flask(__name__)
druid_url = "http://34.82.43.25:8888/druid/v2"
CORS(app)

@app.route("/api/v1/average_sentiment", methods=['POST'])
def average_sentiment():
    try:
        sentiment_query_string = sentiment_query()
        headers = { 
            'Content-Type': 'application/json',
            'Connection':'close'
        }
        response = requests.request("POST", druid_url, headers=headers, data=sentiment_query_string)
        result = response.json()
        response.close()
        return make_response(jsonify(result), 200)
    except Exception as e:
        response = { 'status': 'error', 'message': 'Internal Server Error', 'error': e.message }
        return make_response(jsonify(response), 500)

@app.route("/api/v1/event_count", methods=['POST'])
def event_count():
    try:
        product_catalog = request.json["product_catalog"]
        print("Product catalog: ", product_catalog)
        sentiment_query = event_count_query(product_catalog)

        headers = { 
            'Content-Type': 'application/json',
            'Connection':'close'
        }
        response = requests.request("POST", druid_url, headers=headers, data=sentiment_query)
        result = response.json()
        response.close()

        return make_response(jsonify(result), 200)
    except Exception as e:
        response = { 'status': 'error', 'message': 'Internal Server Error', 'error': e.message }
        return make_response(jsonify(response), 500)

@app.route("/api/v1/timeseries", methods=['POST'])
def timeseries():
    try:
        timeseries_query = json.loads(timeseries_query_string)
        headers = { 
            'Content-Type': 'application/json',
            'Connection':'close'
        }
        response = requests.request("POST", druid_url, headers=headers, data=timeseries_query_string)
        result = response.json()
        response.close()
        return make_response(jsonify(result), 200)
    except Exception as e:
        response = { 'status': 'error', 'message': 'Internal Server Error', 'error': e.message }
        return make_response(jsonify(response), 500)

@app.route("/api/v1/topN", methods=['POST'])
def topN():
    try:
        headers = { 
            'Content-Type': 'application/json',
            'Connection':'close'
        }
        response = requests.request("POST", druid_url, headers=headers, data=topN_query_string)
        print('Response: ', response.close())
        result = response.json()
        response.close()
        return make_response(jsonify(result), 200)
    except Exception as e:
        response = { 'status': 'error', 'message': 'Internal Server Error', 'error': e.message }
        return make_response(jsonify(response), 500)


if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")
