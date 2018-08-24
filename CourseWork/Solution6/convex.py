import numpy as np

# Loading Data sets
class_attributes_seen=np.load('class_attributes_seen.npy')
class_attributes_unseen=np.load('class_attributes_unseen.npy')
X_seen = np.load('X_seen.npy', encoding = 'latin1')
X_test = np.load('Xtest.npy', encoding='latin1')
Y_test = np.load('Ytest.npy', encoding='latin1')

# Finding the similarity vector of unseen class through convex combination
sim_vector = []
similarity_vector = []
for c in range(10):
    sim_c = [np.dot(class_attributes_unseen[c], class_attributes_seen[k]) for k in range(40)]
    sim_vector.append(sim_c)
sim_vector = np.asarray(sim_vector)

# # Normalising the similarity Vector
for s in sim_vector:
    sim_c_normalised = np.asarray([s[k]/sum(s) for k in range(40)])
    similarity_vector.append(sim_c_normalised)
similarity_vector = np.asarray(similarity_vector)

# Calculating mean of each seen class
mean_seen = np.asarray([np.mean(X_seen[i], axis=0) for i in range(40)])

# Finding Mean of unseen classes
mean_unseen = np.matmul(similarity_vector, mean_seen)


# Running Test Data and Predicting the class
predicted_class = []
correct = 0

for t in range(len(X_test)):
    dist = [np.linalg.norm(mean_unseen[i]-X_test[t]) for i in range(10)]
    p_class = 1+dist.index(min(dist))
    predicted_class.append(p_class)
    if p_class == int(Y_test[t]):
        correct += 1
print(correct, "correct out of ", len(X_test))
print("Accuracy = ", correct/len(X_test) * 100, "%")
