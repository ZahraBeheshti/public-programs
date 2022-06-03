import numpy as np


A = np.array([[1, 3, 4, 6, 2], 
              [2, 5, 2, 4, 3], 
              [7, 1, 0, 6, 9], 
              [4, 5, 0, 3, 0], 
              [1, 7, 3, 5, 5], 
              [0, 4, 0, 8, 0], 
              [6, 1, 2, 4, 4]])

def Get_Norm (v, p=0):
  norm = np.sqrt(np.sum(np.power(v, 2)))
  if p : print('Euclidean Norm is : %.3f' % norm)
  return norm

def HouseHolder(a):
  x = np.zeros(a.size)
  x[0] = Get_Norm(a)
  v = (x - a).reshape(a.size, 1)
  I = np.eye(a.shape[0])
  H = I - (2 * v.dot(v.T)) / Get_Norm(v)**2
  return H

def QR(A):
  m, n = A.shape
  Q = np.eye(m)
  for i in range(n):
    H = np.eye(m)
    H[i:, i:] = HouseHolder(A[i:, i])
    A = H.dot(A)
    Q = Q.dot(H)
  return Q, A
 

Q, R = QR(A) # My Function
q, r = np.linalg.qr(A) # Python numpy Package

print('A : \n', A)
print('\nQ matrix : \n', Q.round(decimals=3))
print('\nR matrix : \n', R.round(decimals=3))

QQt = Q.dot(Q.T)
print('\nQQt : \n', QQt.round(decimals=3))

print('\nKian Function : %.15f' % np.linalg.norm(A - Q.dot(R)))
print('Python Package: %.15f' % np.linalg.norm(A - q.dot(r)))