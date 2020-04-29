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
        "intervals": {
            "type": "intervals",
            "intervals": [
            "2020-04-27T08:18:46.000Z/2020-04-30T15:36:27.903Z"
            ]
        },
        "virtualColumns": [],
        "filter": {
            "type": "not",
            "field": {
            "type": "selector",
            "dimension": "event",
            "value": null,
            "extractionFn": null
            }
        },
        "granularity": {
            "type": "all"
        },
        "dimensions": [
            {
            "type": "default",
            "dimension": "product_name",
            "outputName": "product_name",
            "outputType": "STRING"
            },
            {
            "type": "default",
            "dimension": "product_catalog",
            "outputName": "product_catalog",
            "outputType": "STRING"
            }
        ],
        "aggregations": [
            {
            "type": "count",
            "name": "count"
            }
        ],
        "postAggregations": [],
        "having": null,
        "limitSpec": {
            "type": "default",
            "columns": [
            {
                "dimension": "count",
                "direction": "descending",
                "dimensionOrder": {
                "type": "numeric"
                }
            }
            ],
            "limit": 10
        },
        "context": {
            "sqlOuterLimit": 100,
            "sqlQueryId": "fe53f514-c8f5-4d01-929b-9733e0f6af3d"
        },
        "descending": false
    }
"""