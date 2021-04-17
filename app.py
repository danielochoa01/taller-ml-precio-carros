from flask import Flask, render_template, request
import jsonify
import requests
from datetime import date, datetime
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('random_forest_regressor_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    fuel_type_diesel=0

    if request.method == 'POST':
        year = int(request.form['year'])
        present_price = float(request.form['present_price'])
        kms_driven = int(request.form['kms_driven'])
        kms_driven2 = np.log(kms_driven)
        owner = int(request.form['owner'])
        fuel_type_petrol = request.form['fuel_type_petrol']
        seller_type_individual = request.form['seller_type_individual']
        transmission_manual = request.form['transmission_manual']


        year = datetime.now().year - year

        if fuel_type_petrol == 'Petrol':
                fuel_type_petrol = 1
                fuel_type_diesel = 0
        else:
            fuel_type_petrol = 0
            fuel_type_diesel = 1
        
        if seller_type_individual == 'Individual':
            seller_type_individual = 1
        else:
            seller_type_individual=0
        
        if transmission_manual == 'Mannual':
            transmission_manual = 1
        else:
            transmission_manual = 0

        prediction = model.predict([[present_price, kms_driven2, owner, year, fuel_type_diesel, fuel_type_petrol,seller_type_individual, transmission_manual]])
        output = round(prediction[0],2)

        if output<0:
            return render_template('index.html',prediction_texts = "Lo sentimos, no puedes vender este carro")
        else:
            return render_template('index.html',prediction_text = "Puedes vender el carro a {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)