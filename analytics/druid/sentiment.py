'''
    Average sentiment across product catalog
'''

def sentiment_query(product_catalog):
    query = """

        {
            "queryType": "scan",
            "dataSource": {
                "type": "table",
                "name": "flink-output-1"
            },
            "intervals": {
                "type": "intervals",
                "intervals": [
                "2020-04-27T08:37:05.000Z/146140482-04-24T15:36:27.903Z"
                ]
            },
            "virtualColumns": [],
            "resultFormat": "compactedList",
            "batchSize": 20480,
            "limit": 100,
            "order": "none",
            "filter": {
                "type": "and",
                "fields": [
                {
                    "type": "selector",
                    "dimension": "event",
                    "value": "product_review",
                    "extractionFn": null
                },
                {
                    "type": "selector",
                    "dimension": "product_catalog",
                    "value": __catalog__,
                    "extractionFn": null
                }
                ]
            },
            "columns": [
                "product_catalog",
                "product_review",
                "sentiment_score"
            ],
            "legacy": false,
            "context": {
                "sqlOuterLimit": 100,
                "sqlQueryId": "a78c9f3b-b416-4f73-a1b7-298c99b6f1de"
            },
            "descending": false,
            "granularity": {
                "type": "all"
            }
        }

    """
    obj = query.replace("__catalog__", '"{}"'.format(product_catalog))
    return obj