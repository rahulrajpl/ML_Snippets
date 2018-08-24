import numpy as np

# Loading Data sets
class_attributes_seen=np.load('class_attributes_seen.npy')
class_attributes_unseen=np.load('class_attributes_unseen.npy')
X_seen = np.load('X_seen.npy', encoding = 'latin1')
X_test = np.load('Xtest.npy', encoding='latin1')
Y_test = np.load('Ytest.npy', encoding='latin1')

# Calculating mean of each seen class
mean_seen = np.asarray([np.mean(X_seen[i], axis=0) for i in range(40)])
print(mean_seen[0])