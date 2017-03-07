import numpy as np
A = np.array([1,2,3,4])
print(A, np.ndim(A), A.shape, A.shape[0])

B = np.array([[1,2],[3,4],[5,6]])
print(B, np.ndim(B), B.shape)

#dot product
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))

# can't dot product case
C = np.array([[1,2],[3,4]])
D = np.array([[1,2,3],[4,5,6]])
#print(np.dot(D,C))
