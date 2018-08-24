import numpy as np

# Loading Data sets
As=np.load('class_attributes_seen.npy')
Au=np.load('class_attributes_unseen.npy')
X_seen = np.load('X_seen.npy', encoding = 'latin1')
X_test = np.load('Xtest.npy', encoding='latin1')
Y_test = np.load('Ytest.npy', encoding='latin1')

lambda_values = [0.01, 0.1, 1, 10, 20, 50, 100]

# Calculating mean of each seen class
mean_seen = np.asarray([np.mean(X_seen[i], axis=0) for i in range(40)])

# Using the closed form solution for finding W for all values of lambda
t1 = np.asarray([np.add(np.dot(As.transpose(), As), l * np.identity(85)) for l in lambda_values])
t2 = np.dot(As.transpose(), mean_seen)
W = np.asarray([np.dot(np.linalg.inv(t), t2) for t in t1])
mean_unseen = np.asarray([np.dot(Au, w) for w in W])

# Running Test Data and Predicting the class
if __name__=='__main__':

    test_count = len(X_test)
    lambda_values_iter = iter(lambda_values)

    for m in mean_unseen:
        correct_prediction = 0  # for counting number of correct predictions
        for t in range(test_count):
            dist = [np.linalg.norm(m[i]-X_test[t]) for i in range(10)]
            p_class = 1+dist.index(min(dist))
            if p_class == int(Y_test[t]):
                correct_prediction += 1

        print(correct_prediction, "/", test_count, "correct,", end=' ')
        print("Accuracy = ", round(correct_prediction/test_count * 100,4), "% at Lambda =", next(lambda_values_iter))

    exit()