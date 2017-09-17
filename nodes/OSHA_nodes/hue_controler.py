from OSHA_tools.broadcaster import broadcast_msg
from OSHA_tools.upnp_tool import discover
from phue import Bridge
from flask import Flask
app = Flask(__name__)
b = Bridge('192.168.0.100')
b.connect()

@app.route('/controls', methods=['GET'])
def getControls():
    return '{"controls":["on", "off"]}'

@app.route('/controls/on', methods=['POST'])
def on():
	print b.get_api()
	b.set_light( [1,2], 'on', True)

@app.route('/controls/off', methods=['POST'])
def off():
	print b.get_api()
	b.set_light( [1,2], 'on', False)


def main():
	broadcast_msg("HUE_CONTROLER", 12345)
	app.run(host='0.0.0.0', port=80)
	