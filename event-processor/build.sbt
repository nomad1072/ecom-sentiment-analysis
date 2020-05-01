ThisBuild / resolvers ++= Seq(
    "Apache Development Snapshot Repository" at "https://repository.apache.org/content/repositories/snapshots/",
    Resolver.mavenLocal
)

name := "event-processor"

version := "0.1-SNAPSHOT"

organization := "org.siddharth"

ThisBuild / scalaVersion := "2.11.12"

val flinkVersion = "1.10.0"

resolvers += "apache.snapshots" at "https://repository.apache.org/content/repositories/snapshots/"


val flinkDependencies = Seq(
  "org.apache.flink" %% "flink-scala" % flinkVersion,
  "org.apache.flink" %% "flink-streaming-scala" % flinkVersion,
  "org.apache.flink" %% "flink-clients" % flinkVersion,
  "org.apache.flink" %% "flink-connector-kafka" % flinkVersion,
  "org.apache.httpcomponents" % "httpclient" % "4.5.12",
  "joda-time" % "joda-time" % "2.10.6",
  "net.liftweb" %% "lift-json" % "3.4.1",
  "org.scalaj" %% "scalaj-http" % "2.4.2")

lazy val root = (project in file(".")).
  settings(
    libraryDependencies ++= flinkDependencies
  )

assembly / mainClass := Some("org.siddharth.dataflow.consumers.EcomProcess")

// make run command include the provided dependencies
Compile / run  := Defaults.runTask(Compile / fullClasspath,
                                   Compile / run / mainClass,
                                   Compile / run / runner
                                  ).evaluated

// stays inside the sbt console when we press "ctrl-c" while a Flink programme executes with "run" or "runMain"
Compile / run / fork := true
Global / cancelable := true

// exclude Scala library from assembly
assembly / assemblyOption  := (assembly / assemblyOption).value.copy(includeScala = false)
