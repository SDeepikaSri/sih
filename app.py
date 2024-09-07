from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def predict():
    # Extract data from the request form
    crop = request.form['crop']
    region = request.form['region']

    # Call your ML model here to get the predictions
    # For now, mock the prediction
    predictions = { "January": 100, "February": 110, "March": 120 }

    # Render the 'result.html' template with the predictions
    return render_template('result.html', crop=crop, region=region, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)

