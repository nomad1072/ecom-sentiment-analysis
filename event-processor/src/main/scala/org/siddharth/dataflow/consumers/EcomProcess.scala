package org.siddharth.dataflow.consumers

import java.util.Properties

import org.siddharth.dataflow.helpers.EcomEventHelpers.{toEpochTime, transform}
import org.siddharth.dataflow.models.Parser.{parseEcomEvent, writeEcomAnalysisEvent}
import org.apache.flink.api.common.serialization.SimpleStringSchema
import org.apache.flink.api.common.typeinfo.TypeInformation
import org.apache.flink.streaming.api.TimeCharacteristic
import org.apache.flink.streaming.api.functions.timestamps.AscendingTimestampExtractor
import org.apache.flink.streaming.api.scala.{DataStream, StreamExecutionEnvironment}
import org.apache.flink.streaming.connectors.kafka.{FlinkKafkaConsumer, FlinkKafkaProducer}
import org.siddharth.dataflow.models.{EcomEvent, EcomEventAnalysis}
import org.slf4j.LoggerFactory

object EcomProcess {
  private val logger = LoggerFactory.getLogger(EcomProcess.getClass)

  def main(args: Array[String]): Unit = {
    try {
      val env = StreamExecutionEnvironment.getExecutionEnvironment
      val inputTopic = "test"
      val outputTopic = "flink-output-1"
      val bootstrapServers = "localhost:9092"

      val props = new Properties()
      props.setProperty("bootstrap.servers", bootstrapServers)
//      props.setProperty("group.id", groupID )
      logger.info(s"Subscribing to topic: '$inputTopic' with following properties: " + props)
      println("Hello World!")
      env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime)

      implicit val typeInfo1 = TypeInformation.of(classOf[String])
      implicit val typeInfo2 = TypeInformation.of(classOf[EcomEventAnalysis])
      val kafkaSource = new FlinkKafkaConsumer[String](inputTopic, new SimpleStringSchema(), props)
      kafkaSource.assignTimestampsAndWatermarks(new AscendingTimestampExtractor[String] {
        override def extractAscendingTimestamp(strEvent: String): Long = {
          val ecomEvent: EcomEvent = parseEcomEvent(strEvent)
          toEpochTime(ecomEvent.timestamp)
        }
      })


      val stream: DataStream[String] = env.addSource(kafkaSource)
      val transformedStream = stream.map((s: String) => transform(s))
      val outputStream: DataStream[String] = transformedStream.map((event: EcomEventAnalysis) => writeEcomAnalysisEvent(event))
      val kafkaSink = new FlinkKafkaProducer[String](outputTopic, new SimpleStringSchema(), props)
      outputStream.addSink(kafkaSink)

      env.execute("flink-job")
    } catch {
      case e: Exception => {
        logger.error("Unexpected error happened in Flink job! More details are in next log message(s)")
        logger.error(e.toString, e)
        e.printStackTrace()
        println(e.toString)
      }
    }
  }
}
