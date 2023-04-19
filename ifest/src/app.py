from flask import Flask
from routes.blueprint import blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/chat')

@app.route('/')
def main():
    return 'Olá! Bem-vindo ao iFest. Qual o seu nome?'

app.run()
