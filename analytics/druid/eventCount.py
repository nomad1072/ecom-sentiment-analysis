'''
    Event Count across product catalog for a particular day
'''

def event_count_query(product_catalog):
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
            "dimension": "event",
            "outputName": "event_name",
            "outputType": "STRING"
        },
        "metric": {
            "type": "numeric",
            "metric": "count"
        },
        "threshold": 100,
        "intervals": {
            "type": "intervals",
            "intervals": [
            "2020-04-24T05:14:56.000Z/2020-04-30T15:36:27.903Z"
            ]
        },
        "filter": {
            "type": "and",
            "fields": [
                {
                    "type": "selector",
                    "dimension": "product_catalog",
                    "value": __catalog__
                },
                {
                    "type": "not",
                    "field": {
                        "type": "selector",
                        "dimension": "event"
                    }
                }
            ]
        },
        "granularity": {
            "type": "all"
        },
        "aggregations": [
            {
            "type": "count",
            "name": "count"
            }
        ]
    }
    """
    obj = query.replace("__catalog__", '"{}"'.format(product_catalog))
    return obj