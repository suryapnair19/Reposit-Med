from flask import Flask, render_template, request
import pickle 
import numpy as np

# Load the trained model
model_path = r'C:\Users\surya\Desktop\render-project\modelmed.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)
app = Flask(__name__)

# Define the prediction function (replace with actual model prediction)
def predict_medical_cost(age, sex, bmi, children, smoker, region):
    # Here is where you would load a model and make a prediction.
    # For demonstration purposes, we will use a mock formula for prediction.
    base_cost = 2000
    cost = base_cost + age * 50 + bmi * 20 + children * 200 + smoker * 3000
    if sex == 1:
        cost *= 0.9  # Applying a discount for female, example only
    if region == 0:  # Northeast example modifier
        cost *= 1.05
    return f"${cost:,.2f}"

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get form values
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker'])
    region = int(request.form['region'])

    # Call the prediction function
    prediction_text = predict_medical_cost(age, sex, bmi, children, smoker, region)

    # Render the HTML with the prediction result
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
