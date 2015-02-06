import math, random


class Network(object):
	def __init__(self):
		self.network = [
					[Neuron(0),Neuron(0),Neuron(0)],
					[Neuron(3), Neuron(3)],
					[Neuron(2), Neuron(2), Neuron(2)]
					]

	def simulate(self, input):
		for i in range(len(self.network[0])):
			self.network[0][i].output = input[i]

		for i in range(len(self.network[1])):
			self.network[1][i].simulate(self.network[0])

		for i in range(len(self.network[2])):
			self.network[2][i].simulate(self.network[1])

		output = []
		for neuron in self.network[2]:
			output.append(neuron.output)
		return output

	def learnItter(self):
		pass

class Neuron():
	def __init__(self, numInputs):
		self.weights = [random.random(),random.random(),random.random()]
		self.bias = random.random()
		self.output = 0

	def simulate(self, inputs):
		s = 0
		for i in range(len(inputs)):
			s += self.weights[i]*inputs[i].output
		s += self.bias
		self.output = s

		return self.output


if __name__ == "__main__":
	print "Running tests..."
	network = Network()
	print network.simulate([1,1,1])