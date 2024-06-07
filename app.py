# from flask import Flask

# # Create a flask
# app = Flask(__name__)

# # Create an API end point
# @app.route('/')

# def say_hello():
#     return "Hello World"

# def make_pretty(func):
#     def inner():
#         print("decorator działa")
#         func()
#     return inner()

# if __name__ == '__main__':
#     app.run() # domyślnie ustawia localhost i port 5000




import numpy as np
from flask import Flask, request, jsonify

# Perceptron model
class Perceptron:
    def __init__(self, input_dim, learning_rate=0.01):
        self.weights = np.zeros(input_dim + 1)  # +1 for bias
        self.learning_rate = learning_rate

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0

    def train(self, training_inputs, labels, epochs=1000):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Sample training data: temperature, humidity, label (1: true, 0: false)
training_inputs = np.array([
    [30, 70],
    [25, 65],
    [20, 60],
    [35, 75],
    [28, 68]
])
labels = np.array([1, 1, 0, 1, 0])

# Train the model
model = Perceptron(input_dim=2)
model.train(training_inputs, labels)

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json(force=True)
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    
    if temperature is None or humidity is None:
        return jsonify({'error': 'Temperature and humidity are required'}), 400

    prediction = model.predict(np.array([temperature, humidity]))
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
