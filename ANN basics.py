import numpy as np


class NeuralNetwork():

    def __init__(self):
        # Seeding for random number generation
        np.random.seed(1)
        # converting weigth to a 3X1 matrix b/w -1 and 1 with 0 mean
        self.synaptic_weigths = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        # Applying the sigmoid function
        return (1 / (1 + np.exp(x)))

    def sigmoid_derivative(self, x):
        # computing the derivative of the sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        for iteration in range(training_iterations):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weigths += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weigths))
        return output

nn = NeuralNetwork()
print("Beginning randomly generated weights: ")
print(nn.synaptic_weigths)

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T
nn.train(training_inputs, training_outputs, 5000)

print("Ending Weigths after Training: ")
print(nn.synaptic_weigths)

user_input_one = str(input("User Input One: "))
user_input_two = str(input("User Input Two: "))
user_input_three = str(input("User Input Three: "))

print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
print("New Output data: ")
print(nn.think(np.array([user_input_one, user_input_two, user_input_three])))
print("Wow, we did it!")
