import numpy as np
from scipy import sparse

x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))



# 대각선 원소는 1이고 나머지는 0인 2차원 NumPy 배열을 만듭니다.
eye = np.eye(4)
print("NumPy 배열:\n{}".format(eye))

# NumPy 배열을 CSR 포맷의 SciPy 희소 행렬로 변환합니다.
# 0이 아닌 원소만 저장됩니다.
sparse_matrix = sparse.csr_matrix(eye)

print("SciPy의 CSR 행렬:\n{}".format(sparse_matrix))