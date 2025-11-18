from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Dockerized Python App!"

@app.route('/info')
def info():
    return "This is a sample Flask app running inside Docker."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

