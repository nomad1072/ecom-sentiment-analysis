'''
TopN products by events
'''
topN_query_string = """
    
    {
        "queryType": "groupBy",
        "dataSource": {
            "type": "table",
            "name": "flink-output-1"
        },
        "virtualColumns": [],
        "dimensions": [{
            "type": "default",
            "dimension": "product_name",
            "outputName": "product_name",
            "outputType": "STRING"
        }, {
            "type": "default",
            "dimension": "product_catalog",
            "outputName": "product_catalog",
            "outputType": "STRING"
            }],
        "metric": {
            "type": "numeric",
            "metric": "sentiment_sum"
        },
        "threshold": 100,
        "intervals": {
            "type": "intervals",
            "intervals": [
                "2020-04-27T01:10:36.000Z/146140482-04-24T15:36:27.903Z"
            ]
        },
        "filter": {
            "type": "selector",
            "dimension": "event",
            "value": "product_review"
        },
        "granularity": {
            "type": "all"
        },
        "aggregations": [
            {
                "type": "count",
                "name": "count"
            },
            {
                "type": "doubleSum",
                "name": "sentiment_sum",
                "fieldName": "average_sentiment",
                "expression": null
            }
        ],
        "postAggregations": [],
        "context": {
            "sqlOuterLimit": 100,
            "sqlQueryId": "1c83447c-cfe3-4756-b033-45565252fc31"
        },
        "descending": false
    }
    
"""