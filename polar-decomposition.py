import numpy as np
from numpy.linalg import svd
from scipy.linalg import polar


def Gram_matrix(A):
  G = np.zeros(A.shape, dtype=int)
  for i in range(len(A)):
    for j in range(len(A)):
      G[i, j] = np.dot(A[:, i], A[:, j].T)
  return G

A = np.array([7,8,5,4,9,6,5,1,6,8,1,5,7,0,3,4]).reshape(4, 4)
print(A)

U, P = polar(A)

u, s, vt = svd(A)
s = np.diag(s)
Psvd = np.dot(vt.T, np.dot(s, vt))

#print('\nPolar decomposition : ')
#print('U : \n', U)
#print('P : \n', P)
#print('\nuse SVD to Polar decomposition : ')
#print('U_u.vt : \n', np.dot(u, vt))
#print('P_v.s.vt : \n', Psvd)

print('P - Psvd : %.14f' %np.linalg.norm(Psvd - P))
print('\nGram Matrix is : \n', Gram_matrix(P))