import numpy as np;
x = np.array([1.0, 2.0, 3.0])
print(x)
#[1. 2. 3.]
print(type(x))
#<type 'numpy.ndarray'>

#numpy Arithmatic calculate array
y = np.array([2.0, 4.0, 6.0])
# sum
print(x+y)
# sub
print(x-y)
# mul
print(x*y)
# div
print(x/y)

#N dim array
A = np.array([[1,2],[3,4]])
print(A)
# shape of array, A.shape
# data type
print(A.shape, A.dtype)
B = np.array([[3,0],[0,6]])
print(A+B, A*B)
print(A*10)

#broadcast
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*B)

#access array
X = np.array([[51,55],[14,19],[0,4]])
print('===access array===')
print(X)
print('X[0]: ', X[0])
print('X[1][1]: ', X[1][1])
print('X[0][1]: ', X[0][1])
print('X[2][1]: ', X[2][1])
# use for loop print
print('for loop print')
for row in X:
    print(row)

#flatten
X = X.flatten()
print('flatten array: ', X)
print('index 0,2,4 item', X[np.array([0,2,4])])
