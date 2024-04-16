import numpy as np
def attention(Q, K, V, dk):
    QKT = np.dot(Q, K.T)
    weighted_values = np.dot(np.apply_along_axis(lambda x: np.exp(x) / np.sum(np.exp(x)), 0, QKT / np.sqrt(dk)), V)
    return weighted_values

# Define the Q, K, V and dk here
Q = np.random.rand(2,2)
K = np.random.rand(2,2)
V = np.random.rand(2,2)
dk = np.shape(Q)[1]

# Call the function
outputs=attention(Q, K, V, dk)