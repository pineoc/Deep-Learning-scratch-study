
# neural network can be used classification, regression
# generally, regression use identity function
# classification use softmax function

#identity function
#ex)
'''
def identify_function(x):
    return x
'''
#softmax function
#warning! overflow!
'''
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a/ sum_exp_a

    return y
'''
#fix overflow warning
'''
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #overflow solution
    sum_exp_a = np.sum(exp_a)
    y = exp_a/ sum_exp_a

    return y
'''
#soft max test
import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #overflow solution
    sum_exp_a = np.sum(exp_a)
    y = exp_a/ sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y, np.sum(y))
#softmax function output sum = 1
#this result can understand to probability

# output layer neuron setting
# if you want to classificate 0-9 from number image
# output layer neuron number set to 10
