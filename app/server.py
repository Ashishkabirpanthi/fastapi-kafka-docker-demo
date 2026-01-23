from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.kafka_producer import producer


@asynccontextmanager
async def lifespan(app:FastAPI):
    await producer.start_producer()
    yield 
    await producer.stop_producer()
    
    
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def index():
    await producer.send_notification({
        "message":"HELLO",
        "userId":"#224"
    })
    return {"res":"Hello"}
    
    
    