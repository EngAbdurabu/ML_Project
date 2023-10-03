from flask import Flask, request, jsonify
import joblib
from custom_transformers import MultiColumnLabelEncoder  # Import the custom transformer

# ... Rest of your code ...

# Load the saved pipeline

# ... Rest of your code ...


app = Flask(__name__)

# Load the saved pipeline
loaded_pipeline = joblib.load("healthcare_pipeline.pkl")


@app.route("/")
def home():
    return "Healthcare Prediction API"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data as JSON
        input_data = request.json

        # Make predictions using the loaded pipeline
        predictions = loaded_pipeline.predict([input_data])

        # Assuming it's a binary classification task (0 or 1)
        prediction_result = "Stroke Risk" if predictions[0] == 1 else "No Stroke Risk"

        return jsonify({"prediction": prediction_result})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
