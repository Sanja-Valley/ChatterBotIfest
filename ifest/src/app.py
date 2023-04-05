from flask import Flask
from routes.blueprint import blueprint

app = Flask(__name__)

# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/chat')

@app.route('/')
def main():
    return 'Olá! Bem-vindo ao iFest. Qual o seu nome?'

