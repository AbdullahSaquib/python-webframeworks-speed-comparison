from fastapi import FastAPI
import time
import asyncio


app = FastAPI()


@app.get("/sync-ping")
def ping(): 
    return {"message": "pong"}


@app.get('/sync-cpu-bound') 
def cpu_bound():
    count = 0
    for _ in range(1_000_000):
        count += 1 
    return {"message": "CPU Bound"}


@app.get('/sync-io-bound') 
def io_bound():
    time.sleep(0.1)
    return {"message": "IO Bound"}


@app.get("/async-ping")
async def aping(): 
    return {"message": "async pong"}


@app.get('/async-cpu-bound') 
async def acpu_bound():
    count = 0
    for _ in range(1_000_000):
        count += 1 
    return {"message": "CPU Bound"}


@app.get('/async-io-bound') 
async def aio_bound():
    await asyncio.sleep(0.1)
    return {"message": "IO Bound"}
