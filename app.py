from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model
model = joblib.load("titanic_rf_model.pkl")

# Init Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Titanic Survival Prediction API is running on AWS Elastic Beanstalk!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
