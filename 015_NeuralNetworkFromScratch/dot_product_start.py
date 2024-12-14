#%% packages
import numpy as np
# %%
X = [0, 1]
w1 = [2, 3]
w2 = [0.4, 1.8]

# %% Question: which weight is more similar to input data X
x_dot_w1 = np.dot(X, w1)
x_dot_w2 = np.dot(X, w2)
if x_dot_w1 > x_dot_w2:
    print('w1 is more similar to X')
else:
    print('w2 is more similar to X')
