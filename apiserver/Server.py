import connexion
import os
from flask import render_template

if __name__ == "__main__":

	app = connexion.App(__name__, specification_dir='resources')

	@app.route('/')
	def index():
		#We are using python templates in order to use this server address
		#TO-DO: find this servers ip so the UI can call it usinx ajax
	    return render_template('index.html', address="192.168.0.101:80")

	app.add_api('api.yaml')
	app.run(host="0.0.0.0", port=80, debug=True, threaded=True)
