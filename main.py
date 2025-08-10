from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from aiokafka import AIOKafkaProducer
import os
import databases

DATABASE_URL = os.getenv("DATABASE_URL")
REDPANDA_BOOTSTRAP = os.getenv("REDPANDA_BOOTSTRAP", "redpanda:9092")

db = databases.Database(DATABASE_URL)
app = FastAPI()
producer: AIOKafkaProducer | None = None

class Telemetry(BaseModel):
    device_id: str
    ts: str  # ISO timestamp
    metrics: dict


@app.on_event("startup")
async def startup():
    global producer
    await db.connect()
    producer = AIOKafkaProducer(bootstrap_servers=REDPANDA_BOOTSTRAP)
    await producer.start()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
    if producer:
        await producer.stop()


@app.post("/telemetry", status_code=202)
async def ingest(t: Telemetry):
    # validate minimal
    if not t.device_id:
        raise HTTPException(400, "device_id required")
    # write to timescale (simple table insertion)
    query = "INSERT INTO telemetry(device_id, ts, metrics) VALUES (:device_id, :ts, :metrics)"
    await db.execute(query=query, values={"device_id": t.device_id, "ts": t.ts, "metrics": str(t.metrics)})
    # publish to kafka topic
    await producer.send_and_wait("telemetry", str(t.dict()).encode("utf-8"))
    return {"status": "accepted"}