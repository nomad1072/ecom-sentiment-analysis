package org.siddharth.dataflow.models

case class EcomEventAnalysis(event: String,
                             timestamp: String,
                             product_id: String,
                             product_catalog: String,
                             product_name: String,
                             product_review: String,
                             epoch_time: Long,
                             sentiment: String,
                             sentiment_score: Double)

case class EcomEvent(
                    timestamp: String,
                    event: String,
                    product_catalog: Option[String],
                    product_id: Option[String],
                    product_name: Option[String],
                    product_review: Option[String])

case class SentimentResponse(
                            Sentiment: Option[String],
                            Score: Double
                            )
