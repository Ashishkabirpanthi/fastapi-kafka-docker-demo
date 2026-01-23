
from aiokafka import AIOKafkaProducer
import json
import asyncio

BOOTSTRAP_SERVERS = "kafka:9092"
TOPIC = "notifications"


class KafkaProducer():
    
    def __init__(self):
        self.producer:AIOKafkaProducer | None = None
  

    async def start_producer(self):
        if self.producer is None:
            self.producer = AIOKafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
             )
            print("Producer started")
            await self.producer.start()
            
    
    async def stop_producer(self):
        print("Producer stopped")
        if self.producer is not None:
            await self.producer.stop()
            
    
    

        
    async def send_notification(self,data: dict):
        producer = self.producer
        try:
            await producer.send_and_wait(TOPIC, data)
        except Exception as error:
            print("ERROR ",str(error))


producer = KafkaProducer()


