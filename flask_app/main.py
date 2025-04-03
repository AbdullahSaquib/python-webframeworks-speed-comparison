import asyncio
from time import sleep
from flask import Flask, jsonify 


app = Flask(__name__) 


@app.route('/sync-ping') 
def ping():  
    return jsonify({"message": "pong"}) 


@app.route('/sync-cpu-bound') 
def cpu_bound(): 
    count = 0
    for _ in range(1_000_000):
        count += 1
    return jsonify({"message": "CPU Bound"}) 


@app.route('/sync-io-bound') 
def io_bound():  
    sleep(0.1)
    return jsonify({"message": "IO Bound"}) 


@app.route("/async-ping")
async def aping(): 
    return jsonify({"message": "pong"})


@app.route('/async-cpu-bound') 
async def acpu_bound():
    count = 0
    for _ in range(1_000_000):
        count += 1 
    return jsonify({"message": "CPU Bound"})


@app.route('/async-io-bound') 
async def aio_bound():
    await asyncio.sleep(0.1)
    return jsonify({"message": "IO Bound"})


if __name__ == '__main__': 
	app.run(debug=True) 
