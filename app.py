from flask import Flask, request, jsonify
import numpy as np
import pickle

# Load the trained Logistic Regression model (ensure the .pkl file is in the same directory)
model = pickle.load(open('logreg_model.pkl', 'rb'))

# Initialize the Flask app
app = Flask(__name__)

# Define the predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the patient data from the request
    data = request.get_json()

    # Convert the data into the right format (e.g., array or list of feature values)
    features = np.array([data['features']])

    # Make a prediction (get the probability of being readmitted)
    prediction = model.predict_proba(features)[:, 1][0]

    # Return the prediction as a JSON response
    return jsonify({
        'readmission_probability': prediction
    })

# Run the app (this allows the app to run locally)
if __name__ == '__main__':
    app.run(debug=True)