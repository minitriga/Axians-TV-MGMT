import os
import cec
from flask import Flask
from flask import request

app = Flask(__name__)

cec.init()

tv = cec.Device(cec.CECDEVICE_TV)

def change_tv_state(state: bool):

    if state:
        tv.power_on()
    else:
        tv.standby()


@app.route("/tv", methods=["POST"])
def set_state():
    data = request.get_json()
    change_tv_state(data['state'])
    return {"state": data['state']}


