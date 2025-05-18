from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bonjour, ceci est l'app Flask de Ecuyer !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
