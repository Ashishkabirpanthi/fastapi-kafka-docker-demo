from aiokafka import AIOKafkaConsumer
import asyncio
import json
import logging

logging.basicConfig(level=logging.INFO)

BOOTSTRAP_SERVERS = "kafka:9092"
TOPIC = "notifications"
GROUP_ID = "notifications-handler"
RETRY_DELAY = 3 


class KafkaConsumer:
    def __init__(self):
        self.consumer: AIOKafkaConsumer | None = None
        self.running = True

    async def _start_consumer(self):
        while self.running:
            try:
                logging.info("Starting Kafka consumer...")
                self.consumer = AIOKafkaConsumer(
                    TOPIC,
                    bootstrap_servers=BOOTSTRAP_SERVERS,
                    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
                    group_id=GROUP_ID,
                    auto_offset_reset="earliest",
                )
                await self.consumer.start()
                logging.info("✅ Kafka consumer started")
                return
            except Exception as e:
                logging.warning(
                    "Kafka not ready yet, retrying in %ss... (%s)",
                    RETRY_DELAY,
                    e,
                )
                await asyncio.sleep(RETRY_DELAY)

    async def consume(self):
        while self.running:
            await self._start_consumer()

            try:
                async for msg in self.consumer:
                    logging.info("📩 Message received: %s", msg.value)

            except Exception as e:
                logging.error("❌ Kafka consumer error: %s", e)

            finally:
                await self._stop_consumer()
                logging.info("🔄 Restarting Kafka consumer...")

    async def _stop_consumer(self):
        if self.consumer is not None:
            try:
                await self.consumer.stop()
            except Exception:
                pass
            self.consumer = None

    async def shutdown(self):
        self.running = False
        await self._stop_consumer()


consumer = KafkaConsumer()

if __name__ == "__main__":
    try:
        asyncio.run(consumer.consume())
    except KeyboardInterrupt:
        logging.info("🛑 Shutting down Kafka consumer")
