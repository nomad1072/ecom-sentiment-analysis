'''
    Average sentiment across product catalog
'''

def sentiment_query():
    query = """

        {
            "queryType": "topN",
            "dataSource": {
                "type": "table",
                "name": "flink-output-1"
            },
            "virtualColumns": [],
            "dimension": {
                "type": "default",
                "dimension": "product_catalog",
                "outputName": "product_catalog",
                "outputType": "STRING"
            },
            "metric": {
                "type": "numeric",
                "metric": "sentiment"
            },
            "threshold": 100,
            "intervals": {
                "type": "intervals",
                "intervals": [
                "2020-04-25T01:23:50.000Z/146140482-04-24T15:36:27.903Z"
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
                "name": "sentiment",
                "fieldName": "average_sentiment",
                "expression": null
                }
            ],
            "postAggregations": [],
            "context": {
                "sqlOuterLimit": 100,
                "sqlQueryId": "fe75f2ce-f009-4ee2-b80f-1f756019e3d9"
            },
            "descending": false
        }

    """
    # obj = query.replace("__catalog__", '"{}"'.format(product_catalog))
    return query