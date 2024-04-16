import numpy as np

# sample data
X = np.array([[1], [3], [5], [7]])
y_true = np.array([[3], [5], [7], [9]])  # Next number in the series

# Initialize parameters
input_size = 1
hidden_size = 4
output_size = 1

# Define weight and bias
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))

# Define activation function (sigmoid)
# The sigmoid function is commonly used in machine learning and neural networks because it maps any real-valued number to the range \((0, 1)\), 
# which is useful for tasks such as binary classification where you want to output probabilities. 
# As \(x\) becomes larger, the sigmoid function approaches 1, and as \(x\) becomes smaller, it approaches 0. 
# This property allows it to introduce non-linearity to neural network models.

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Hyperparameters
learning_rate = 0.01
epochs = 1000

# Training loop
for epoch in range(epochs):
    
    # Forward pass (feedforward)
    # X is a matrix representing the input data. Each row of X corresponds to a single data point, and each column corresponds to a feature (in this case, it seems to be a single feature).
    # W1 is the weight matrix connecting the input layer to the hidden layer of a neural network. It has dimensions (input_size, hidden_size), where input_size is the number of features in the input data, and hidden_size is the number of neurons in the hidden layer.
    # np.dot(X, W1) performs matrix multiplication between X and W1. 
    # This operation effectively transforms the input data into the hidden layer space, where each row of the resulting matrix represents the transformed features for a particular data point.
    
    hidden_layer_input = np.dot(X, W1) + b1
    hidden_layer_output = sigmoid(hidden_layer_input)
    y_pred = np.dot(hidden_layer_output, W2) + b2

    # Compute loss (mean squared error)
    loss = np.mean((y_pred - y_true) ** 2)

    # Backpropagation
    dL_dy_pred = 2 * (y_pred - y_true)
    dW2 = np.dot(hidden_layer_output.T, dL_dy_pred)
    db2 = np.sum(dL_dy_pred, axis=0)
    dhidden = np.dot(dL_dy_pred, W2.T) * (hidden_layer_output * (1 - hidden_layer_output))
    dW1 = np.dot(X.T, dhidden)
    db1 = np.sum(dhidden, axis=0)

    # Update weights and biases
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.4f}")

# Test the trained network
test_input = np.array([[9]])  # Predict the next number after 9
hidden_output = sigmoid(np.dot(test_input, W1) + b1)
predicted_number = np.dot(hidden_output, W2) + b2
print(f"Predicted next number: {predicted_number[0][0]:.2f}")
