import math, random


class Network(object):
	def __init__(self):
		super(Network, self).__init__()
		self.arg = arg
	def init(self, numInput, numHidden, numOutput):
		self.network = [
					[0,0,0],
					[Neuron(), Neuron()],
					[Neuron(), Neuron(), Neuron()]
					]


	def simulate(self, input):
		for i in range(len(self.network[0])):
			self.network[0][i] = input[i]

		for val in self.network[1]:
			pass #Bself.

		return output

	def learnItter(self):
		pass

class Neuron():
	def __init__(self):
		self.weights = [random.random(),random.random(),random.random()]
		self.bias = random.random()
		self.output = 0

