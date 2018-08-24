import numpy as np

# Loading Data sets
class_attributes_seen=np.load('class_attributes_seen.npy')
class_attributes_unseen=np.load('class_attributes_unseen.npy')
X_seen = np.load('X_seen.npy', encoding = 'latin1')
X_test = np.load('Xtest.npy', encoding='latin1')
Y_test = np.load('Ytest.npy', encoding='latin1')

# Finding the similarity vector of unseen class through convex combination
sim_vector = []
sim_vector_normalized = []
for c in range(10):
    sim_c = [np.dot(class_attributes_unseen[c], class_attributes_seen[k]) for k in range(40)]
    sim_vector.append(sim_c)
sim_vector = np.asarray(sim_vector)

# # Normalising the similarity Vector
for s in sim_vector:
    sim_c_normalised = np.asarray([s[k]/sum(s) for k in range(40)])
    sim_vector_normalized.append(sim_c_normalised)
sim_vector_normalized = np.asarray(sim_vector_normalized)

# Calculating mean of each seen class
mean_seen = np.asarray([np.mean(X_seen[i], axis=0) for i in range(40)])

# Finding Mean of unseen classes
mean_unseen = np.matmul(sim_vector_normalized, mean_seen)

# Running Test Data and Predicting the class
if __name__=='__main__':

    correct_prediction = 0 # for counting number of correct predictions
    test_count = len(X_test)

    for t in range(test_count):
        dist = [np.linalg.norm(mean_unseen[i]-X_test[t]) for i in range(10)]
        p_class = 1+dist.index(min(dist))
        if p_class == int(Y_test[t]):
            correct_prediction += 1

    print(correct_prediction, "/", test_count, "correct,", end=' ')
    print("Accuracy = ", round(correct_prediction / test_count * 100, 4), "%")

    exit()