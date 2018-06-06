from numpy import exp, array, random, dot


class NeuralNet():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(1)

        # Model a single neuron, with 3 input connections and 1 output connection.
        # Assigning random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synapticWeights = 2 * random.random((3,1)) - 1

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + exp( - x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    @staticmethod
    def sigmoidDerivative(x):
        return x * (1 - x)

    def train(self, trainingSetInputs, trainingSetOutputs, numberOfTrainingIterations):
        for iteration in xrange(numberOfTrainingIterations):
            # Pass the training set through our neural network (a single neuron).
            output = self.think(trainingSetInputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            error = trainingSetOutputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(trainingSetInputs.T, error * self.sigmoidDerivative(output))

            # Adjust the weights.
            self.synapticWeights += adjustment

    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.sigmoid(dot(inputs, self.synapticWeights))


if __name__ == "__main__":

    # Initialise a single neuron neural network.
    NeuralNet = NeuralNet()

    print "Random starting synaptic weights: "
    print NeuralNet.synapticWeights
    print trainingSetInputs

    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.
    trainingSetInputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    trainingSetOutputs = array([[0, 1, 1, 0]]).T

    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    NeuralNet.train(trainingSetInputs, trainingSetOutputs, 100000)

    print "New synaptic weights after training: "
    print NeuralNet.synapticWeights

    # Test the neural network with a new situation.
    print "Considering new situation [1, 0, 0] -> ?: "
print NeuralNet.think(array([1, 0, 0]))