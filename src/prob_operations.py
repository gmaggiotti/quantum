import numpy as np

# M = ∑ ∣f(a)⟩⟨a∣
#     a∈Σ

f_a = np.array([[1/2,1/2]]).T
a = np.array([[0,1]])
result = np.matmul(f_a,a)
print(result)