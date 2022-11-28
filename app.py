from flask import Flask
from stock import getData
import asyncio
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    [headerData, stockData]= asyncio.run(getData())
    # print("headerData:- ",headerData)
    # print("headerData:- ", stockData)
    data={
        'headerData':headerData, 
        'stockData':stockData,
    }    
    return json.dumps(data)