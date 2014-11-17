import math


class Network(object):
	def __init__(self):
		super(Network, self).__init__()
		self.arg = arg
	def init(self, numInput, numHidden, numOutput):
		self.numInput = numInput
		self.numHidden = numHidden
		self.numOutput = numOutput
		self.input = [0 for x in range(numInput)]
		self.hidden = [[0] for x in range(numHidden)]
		self.output = [0 for x in range(numOutput)]
		self.weights = [0 for x in range(numHidden)]

	def simulate(self, input):
		for neuron in self.hidden:
			for inputVal in self.input:
				pass


		return output
	def learnItter(self):
		pass
class Neuron():
	def __init__(self):
		pass