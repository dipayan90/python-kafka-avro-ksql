# Python Kafka KSQL Demonstration

Demonstrates how to use python to consume and produce messages to kafka. 
Also demonstrates how to use ksql for analytics on kafka streams

# steps for running

## Download and unzip kafka

```bash
wget http://mirror.olnevhost.net/pub/apache/kafka/2.2.0/kafka_2.12-2.2.0.tgz
tar -xzf kafka_2.12-2.2.0.tgz
cd kafka_2.12-2.2.0
``` 

## Initialize zookeper server and kafka server


### Zookeper


```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```


### Kafka server


```bash
bin/kafka-server-start.sh config/server.properties
```

## Create a test topic and make sure it exists

```bash
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

## Lets start the app now 


### Installation


```bash
pip install . 
```

### Open python shell and execute following commands

```bash
python 
```

```python
from app.main import ApplicationRunner
runner = ApplicationRunner("test")
runner.main()
```

