import io
import random

from kafka import KafkaConsumer, KafkaProducer
import avro.schema
from avro.io import DatumWriter

from app import LoggerMixin


class ApplicationRunner(LoggerMixin):

    def __init__(self, topic_name: str):
        super().__init__()
        self.topic_name = topic_name
        self.kafka_producer = KafkaProducer()
        self.kafka_consumer = KafkaConsumer(self.topic_name, auto_offset_reset="earliest")
        schema_path = "user.avsc"
        self.schema = avro.schema.Parse(open(schema_path).read())
        self.names = ("john", "joe", "jane", "harry", "nicole", "adam", "kelly", "nancy", "michael", "dipayan")
        self.colors = ("red", "green", "blue", "white", "yellow")

    def consume(self):
        for msg in self.kafka_consumer:
            bytes_reader = io.BytesIO(msg.value)
            decoder = avro.io.BinaryDecoder(bytes_reader)
            reader = avro.io.DatumReader(self.schema)
            yield reader.read(decoder)

    def produce(self):
        writer = DatumWriter(self.schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        for i in range(0, 100):
            writer.write(
                {"name": self.names[random.randint(0, 9)], "favorite_color": self.colors[random.randint(0, 4)],
                 "favorite_number": random.randint(0, 10)}, encoder)
            raw_bytes = bytes_writer.getvalue()
            self.kafka_producer.send(topic=self.topic_name, value=raw_bytes)

    def main(self):
        self.produce()
        for rec in self.consume():
            print(rec)
