import numpy as np

# Loading Data sets
class_attributes_seen=np.load('class_attributes_seen.npy')
class_attributes_unseen=np.load('class_attributes_unseen.npy')
X_seen = np.load('X_seen.npy', encoding = 'latin1')
X_test = np.load('Xtest.npy', encoding='latin1')
Y_test = np.load('Ytest.npy', encoding='latin1')

# Finding the similarity vector of unseen class through convex combination
sim_vector = []
# sim_c = np.empty(shape=[1,40])
similarity_vector = []
for c in range(10):
    # sim_c = np.asarray([np.dot(class_attributes_unseen[c], class_attributes_seen[k]) for k in range(40)])
    sim_c = [np.dot(class_attributes_unseen[c], class_attributes_seen[k]) for k in range(40)]
    sim_vector.append(sim_c)
sim_vector = np.asarray(sim_vector)

# Normalising the similarity Vector
for s in sim_vector:
    sim_c_normalised = np.asarray([s[k]/sum(s) for k in range(40)])
    # sim_c_normalised = np.asarray([s[k]/sum(s) for k in range(40)])
    similarity_vector.append(sim_c_normalised)
similarity_vector = np.asarray(similarity_vector)



# Calculating mean of each seen class
# mean_of_seen_classes = np.asarray([X_seen[i].mean() for i in range(40)])
mean_of_seen_classes = np.asarray([np.reshape(X_seen[i], X_seen[i].shape[0]*4096).mean() for i in range(40)])

# Finding Mean of unseen classes
mean_of_unseen_classes = []
for s in similarity_vector:
    mean_of_unseen_classes.append(sum([s[k]*mean_of_seen_classes[k] for k in range(40)]))

for i in mean_of_unseen_classes:
    print(i)
# Combining all 50 nos means calculated in to "mean_of_classes"
mean_of_classes =  mean_of_unseen_classes


# Running Test Data and Predicting the class
# m_test = X_test[1].mean()
# print("Test input is ", m_test)
# m_predicted = min(mean_of_classes, key=lambda x:abs(x-m_test))
# print("Predicted input is", m_predicted)
# m_class = mean_of_classes.index(min(mean_of_classes, key=lambda x:abs(x-m_test)))
# # print("Predicted Class is ", mean_of_classes.index(m_predicted))
# print("Predicted Class is ", m_class+1)
# print("Actual Class is ", int(Y_test[1]))

correct_predictions = 0
for t,y in zip(X_test,Y_test):
    # m_test = t.mean()
    m_test = np.reshape(t, t.shape[0]).mean()
    m_predicted = min(mean_of_classes, key=lambda x: abs(x - m_test))
    m_class = mean_of_classes.index(m_predicted)+1
    if m_class == int(y[0]):
        correct_predictions += 1

print(correct_predictions)
for t in X_test:
    print(t.shape)