MATLAB format:

You can load everything as load('AwA_v1');

- X_seen is a cell array contaning the input feature matrices of each of the 40 seen classes (NxD format - rows are examples, columns are features). For example, X_seen{1} being the feature matrix of seen class 1 inputs, X_seen{2} being the feature matrix of seen class 2 inputs, and so on.

- Xtest is the feature matrix for the test data from all the 10 unseen classes (NxD format - rows are examples, columns are features).

- YTest is the ground truth label vector for the test data from all the 10 unseen classes.

- class_attributes_seen is a 40x85 matrix with each row being the 85-dimensional class attribute vector of a seen class.

- class_attributes_unseen is a 10x85 matrix with each row being the 85-dimensional class attribute vector of an  unseen class.



Python format:

X_seen=np.load('X_seen.npy') 	(40 x N_i x D): 40 feature matrices. X_seen[i] is the N_i x D feature matrix of seen class i

Xtest=np.load('Xtest.npy')	(6180, 4096): feature matrix of the test data.

Ytest=np.load('Ytest.npy',)	(6180, 1): ground truth labels of the test data

class_attributes_seen=np.load('class_attributes_seen.npy')	(40, 85): 40x85 matrix with each row being the 85-dimensional class attribute vector of a seen class.

class_attributes_unseen=np.load('class_attributes_unseen.npy')	(10, 85): 10x85 matrix with each row being the 85-dimensional class attribute vector of an  unseen class.


