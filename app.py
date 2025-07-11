from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('model/modelForPrediction.pkl', 'rb'))
scaler = pickle.load(open('model/standardScaler.pkl', 'rb'))

# Route for the home page
@app.route('/')
def index():
    return render_template('home.html')  # Use home.html if that's your file

# Route for prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ""

    if request.method == "POST":
        # Correct data extraction
        Pregnancies = int(request.form.get('Pregnancies'))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        # Correct input structure
        new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                      Insulin, BMI, DiabetesPedigreeFunction, Age]])
        prediction = model.predict(new_data)

        if prediction[0] == 1:
            result = 'Diabetic'
        else:
            result = 'Non-Diabetic'

        return render_template('result.html', result=result)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
