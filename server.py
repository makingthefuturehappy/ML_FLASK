import datetime
import pickle
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def intro():
    intro = "the server is launched...<br>"
    intro1 = 'this app is a show case, which makes a linear model prediction based on 2 numbers<br>'
    intro2 = "use: curl - i - X POST - H 'Content-Type: application/json' - d '{'params': '4,5'}' localhost:5000/predict"
    return intro1 + intro2 + intro2


@app.route('/predict', methods=['POST'])
def prediction():
    with open('ml_model.pkl', 'rb') as pkl_file:
        model = pickle.load(pkl_file)

    params = request.json.get('params')
    params = np.fromstring(str(params), sep=',').reshape(1,2)

    model_response = model.predict(params)
    print(f'prediction: {model_response}')
    return f'prediction: {model_response}'

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello {name}!'

@app.route('/time')
def current_time():
    return {'time': datetime.datetime.now()}

#server launch
if __name__ == '__main__':
    app.run('localhost', 5000)