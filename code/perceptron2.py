#perceptron, add weight, bias

import numpy as np
x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7
print('w1x1+w2x2: ',np.sum(w*x))
print('b+w1x1+w2x2: ', np.sum(w*x)+b) #floating point inaccuracy

#AND function with bias
def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#NAND function with bias
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <=0:
        return 0
    else:
        return 1

#OR function with bias
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <=0:
        return 0
    else:
        return 1

#XOR can not make of linear
#it can make compose AND, NAND, OR
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print('XOR(0,0): ', XOR(0,0))
print('XOR(1,0): ', XOR(1,0))
print('XOR(0,1): ', XOR(0,1))
print('XOR(1,1): ', XOR(1,1))
