import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler



# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load the preprocessor
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

# Initialize the Flask app
app = Flask(__name__)


# Define the API endpoint for model prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json

    # Load the data into a DataFrame
    df = pd.DataFrame(input_data, index=[0])

    # Add 'TotalIncome_log' column
    df['TotalIncome_log'] = np.log(df['ApplicantIncome'] + df['CoapplicantIncome'])

    # Preprocess the data
    preprocessed_data = preprocessor.transform(df)

    # Perform model prediction
    prediction = model.predict_proba(preprocessed_data)

    # Prepare the response data
    result = {
        'Loan_Status': 'Approved' if prediction[0][1] >= 0.5 else 'Rejected',
        'Probability': prediction[0][1]
    }

    # Return the response as JSON
    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
