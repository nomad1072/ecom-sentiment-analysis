package org.siddharth.dataflow.models

import net.liftweb.json._
import net.liftweb.json.Serialization.write
import net.liftweb.json.DefaultFormats
import org.joda.time.format.DateTimeFormat
import org.joda.time.{DateTime, DateTimeZone}

object Parser {
  implicit val formats = DefaultFormats

  def writeEcomAnalysisEvent(event: EcomEventAnalysis): String = write(event)

  def parseEcomEvent(strJson: String): EcomEvent = {
    try {
      val objJson = net.liftweb.json.parse(strJson)
      objJson.extract[EcomEvent]
    }
    catch {
      case e: Exception => {
        val currentDateTime = new DateTime().withZone(DateTimeZone.UTC)
        val dateTimeFormatter = DateTimeFormat.forPattern("yyyy-MM-dd'T'HH:mm:ss.SSSZ")
        val currentTimestamp: String = dateTimeFormatter.print(currentDateTime).dropRight(5) + "Z"

        EcomEvent(
          event = "error_occurred",
          product_id = Some(""),
          product_catalog = Some(""),
          product_name = Some(""),
          timestamp = currentTimestamp,
          product_review = Some("")
        )
      }
    }
  }
}
