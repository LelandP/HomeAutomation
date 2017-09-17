from OSHA_tools.broadcaster import listen_and_wait
import requests
import copy
import time

NODES = []
NODE_TEMPLATES = {"name":"",
				  "ip":"",
				  "node_type":"",
				  "control_list":[]}

def discover_nodes():
	while True:
		node_type, node_address = listen_and_wait(12345)
		node = copy.copy(NODE_TEMPLATES)
		node["name"] = node_type + "_" + node_address[0]
		node["ip"] = node_address[0]
		node["node_type"] = node_type
		time.sleep(5)
		node["control_list"] = requests.get("http://"+node["ip"]+"/controls").json()["controls"]

		print node
		NODES.append(node)

def main():
	discover_nodes()