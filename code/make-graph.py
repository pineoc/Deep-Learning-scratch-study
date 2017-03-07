##stair graph & sigmoid graph
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identify_function(x):
    return x

#draw graphs
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
y2 = sigmoid(x)
plt.plot(x,y)
plt.plot(x,y2)
plt.ylim(-0.1,1.1)
#plt.show()

#make 3 layered neural network
#x1,x2 -> y1,y2.
#first hidden layer, 3 node
#second hidden layer, 2 node
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print('shapes of layers first phase', W1.shape, X.shape, B1.shape)

#input -> first layer
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print(A1, Z1)

#first layer -> second layer
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print('shapes of layers second phase', Z1.shape, W2.shape, B2.shape)
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(A2, Z2)

#second layer -> output layer
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identify_function(A3) # or Y = A3
print('result', Y)
