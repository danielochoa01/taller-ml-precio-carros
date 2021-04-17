from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('random_forest_regressor_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)