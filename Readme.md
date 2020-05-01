# Ecom Analysis

- We present a big data analytics solution to analyze customer reviews using kafka, flink and druid for businesses to make data driven decisions based on customer feedback on e-commerce websites. 
- We track ```product_viewed```, ```product_added_to_cart``` and ```product_review``` events and have a sentiment analysis model in the background that provides the sentiment of the text review.
- Finally, we convert these raw input events into processed events in our flink job and store these events back in kafka. Druid's kafka indexer directly picks the processed events from the kafka queue. 
- Our paper is attached in the pdf that talks in detail about our design in building this system. 
- We have a flink job, analytics service to query druid, a flask api to do sentiment analysis and a dashboard to track the events generated in the system.
