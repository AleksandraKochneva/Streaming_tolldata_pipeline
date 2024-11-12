from kafka.admin import KafkaAdminClient,NewTopic
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='admin')
topic_list = []
new_topic = NewTopic(name="toll", num_partitions= 1, replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)