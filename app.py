import numpy as np 
# use "py -m ensurepip --default pip" to install pip
# use "py -m pip install numpy" to install numpy (so happy I figured this out with google or help lol)

np.random.seed(0)

X = [[1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
        def __init__(self, n_inputs, n_neurons):
                self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
                self.biases = np.zeros((1, n_neurons))
        def forward(self, inputs):
                self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4, 6)
layer2 = Layer_Dense(6, 3)

layer1.forward(X)
#print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)