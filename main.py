import os
import cec
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

cec.init()

tv = cec.Device(cec.CECDEVICE_TV)

def change_tv_state(state: bool):

    if state:
        tv.power_on()
    else:
        tv.standby()


@app.route("/tv", methods=["POST"])
@cross_origin()
def set_state():
    data = request.get_json()
    change_tv_state(data['state'])
    return {"state": data['state']}


