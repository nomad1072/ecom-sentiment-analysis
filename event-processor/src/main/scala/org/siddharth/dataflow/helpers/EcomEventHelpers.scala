package org.siddharth.dataflow.helpers

import java.nio.charset.StandardCharsets

import net.liftweb.json.DefaultFormats
import org.siddharth.dataflow.models.Parser.parseEcomEvent
import org.joda.time.format.DateTimeFormat
import org.siddharth.dataflow.models.{EcomEvent, EcomEventAnalysis, SentimentResponse}
import org.joda.time.{DateTime, DateTimeZone}
import org.slf4j.LoggerFactory
import org.apache.http.client.methods.HttpPost
import org.apache.http.entity.StringEntity
import org.apache.http.impl.client.DefaultHttpClient
import org.apache.http.util.EntityUtils

import scala.util.parsing.json.JSONObject





object EcomEventHelpers {
  implicit val formats = DefaultFormats
  private val logger = LoggerFactory.getLogger(EcomEventHelpers.getClass)
  private val DATE_TIME_PATTERN = DateTimeFormat.forPattern("yyyy-MM-dd'T'HH:mm:ss.SSSZ")

  def toEpochTime(timestamp: String): Long =
    DateTime.parse(timestamp, DATE_TIME_PATTERN).withZone(DateTimeZone.UTC).getMillis

  def toDateTime(epochTime: Long): String =
    new DateTime(epochTime).withZone(DateTimeZone.UTC).toString()

  def sentimentApi(ecomEvent: EcomEvent): (String, Double) = {
    val obj = Map("review_body" -> ecomEvent.product_review.getOrElse(""))
    val json = Map("data" -> new JSONObject(obj))

    val jsonObject = new JSONObject(json)
    println("Json String BOdy: ", jsonObject.toString())
    val post = new HttpPost("http://localhost:5000/api/v1/sentiment/")
    post.setHeader("Content-type", "application/json")

    // add the JSON as a StringEntity
    post.setEntity(new StringEntity(jsonObject.toString()))

    // send the post request
    val response = (new DefaultHttpClient).execute(post)
    val entity = response.getEntity
    val rJSON = EntityUtils.toString(entity, StandardCharsets.UTF_8)

    val objJson = net.liftweb.json.parse(rJSON)
    val sentimentResponse = objJson.extract[SentimentResponse]
    val sentiment: String = sentimentResponse.Sentiment.getOrElse("")
    val sentiment_score: Double = sentimentResponse.Score
    return (sentiment, sentiment_score)
  }

  def transform(strEvent: String): EcomEventAnalysis = {
    try {
      val ecomEvent: EcomEvent = parseEcomEvent(strEvent)
      if (ecomEvent.event == "product_review") {
        val (sentiment, sentiment_score) = sentimentApi(ecomEvent)
        println("Sentiment: ", sentiment)
        println("Sentiment Score: ", sentiment_score)
         val analysisEvent = EcomEventAnalysis(
           event = ecomEvent.event,
           timestamp = ecomEvent.timestamp,
           product_id = ecomEvent.product_id.getOrElse(""),
           product_catalog = ecomEvent.product_catalog.getOrElse(""),
           product_name = ecomEvent.product_name.getOrElse(""),
           product_review = ecomEvent.product_review.getOrElse(""),
           epoch_time = toEpochTime(ecomEvent.timestamp),
           sentiment,
           sentiment_score
         )
        analysisEvent
      } else {
        val analysisEvent = EcomEventAnalysis(
          event = ecomEvent.event,
          timestamp = ecomEvent.timestamp,
          product_id = ecomEvent.product_id.getOrElse(""),
          product_catalog = ecomEvent.product_catalog.getOrElse(""),
          product_name = ecomEvent.product_name.getOrElse(""),
          product_review = ecomEvent.product_review.getOrElse(""),
          epoch_time = toEpochTime(ecomEvent.timestamp),
          sentiment = "",
          sentiment_score = 0
        )
        analysisEvent
      }
    } catch {
      case e: Exception => {
        logger.error(e.toString, e)

        val errorEvent = EcomEventAnalysis(
          event = "error_occurred",
          timestamp = "",
          epoch_time = 0,
          product_id = "",
          product_catalog = "",
          product_name = "",
          product_review = "",
          sentiment = "",
          sentiment_score = 0
        )
        errorEvent
      }
    }
  }
}
