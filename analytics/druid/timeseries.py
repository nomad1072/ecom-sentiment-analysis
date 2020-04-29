'''
    Timeseries event count. Granularity set to day
'''

timeseries_query_string = """

    {
        "queryType": "timeseries",
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
            "2020-04-25T05:14:56.000Z/2020-04-30T15:36:27.903Z"
            ]
        },
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
        "aggregations": [
            {
            "type": "count",
            "name": "total_event_count"
            }
        ],
        "postAggregations": [],
        "context": {
            "sqlOuterLimit": 100,
            "sqlQueryId": "be46b1f1-926c-40b6-a004-396013d29bc7"
        },
        "descending": false
    }

"""