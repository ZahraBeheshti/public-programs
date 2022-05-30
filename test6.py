# triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
# define square matrix
M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]])
print(M)

lower = tril(M)
print(lower)

upper = triu(M)
print(upper)
