import connexion

app = connexion.App(__name__, specification_dir='resources')
app.add_api('api.yaml')
app.run(port=8080)