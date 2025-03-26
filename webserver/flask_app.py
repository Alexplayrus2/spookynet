# hosted at https://alexplayrus1.pythonanywhere.com

from flask import Flask
from flask import request
import json
mpdata = "{}"
app = Flask(__name__)

@app.route("/multiplayer/set")
def mpset():
    global mpdata
    data = json.loads(mpdata)
    data[request.args.get('name')] = request.args.get('val')
    mpdata = json.dumps(data)
    return request.args.get('val')

@app.route("/multiplayer/get")
def mpget():
    global mpdata
    data = json.loads(mpdata)
    return data[request.args.get('name')]

@app.route("/multiplayer/setandget")
def mpsetget():
    global mpdata
    data = json.loads(mpdata)
    data[request.args.get('name')] = request.args.get('val')
    mpdata = json.dumps(data)
    data = json.loads(mpdata)
    return data[request.args.get('getname')]
