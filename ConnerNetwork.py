import numpy as np
import time

class Neuron():

    def __init__(self):
        self.weights = []
        self.inputs = [] 
        self.output = 0
        self.sum = 0
        self.bias = 1
        
    def activation(self,newInputs):
        sum = 0  #Every activation you need to reset the sum.
        self.inputs = newInputs

        for i in xrange(len(self.inputs)):
            self.sum += self.inputs[i] * self.weights[i]

        self.sum += self.bias 

        if self.sum <=  0:
            self.output = 0
        else:
            self.output = self.sum

        return self.output

class Network():

    def letterTable(self):
        self.letterTable = {}

        values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        for i in xrange(len(values)):
            self. letterTable[values[i]] = i
            self.letterTable[i] = values[i]

    def __init__(self,sizes):
        self.sizes = sizes
        self.letterTable()
        self.network = [] 
        self.outputs = []

        for i in xrange(len(self.sizes)):
            self.network.append([])
            self.outputs.append([])

            for x in xrange(self.sizes[i]):
                self.network[i].append(Neuron())
                self.outputs[i].append(0)                     
        
        for i in xrange(len(self.sizes)):
            for x in xrange(self.sizes[i]):
                if i == 0:
                    self.network[i][x].weights = np.random.randn(1)
                else:    
                    self.network[i][x].weights = np.random.randn(sizes[i-1]) 
    
    def predict(self,input):
        for i in xrange(len(self.sizes)):    
            for x in xrange(self.sizes[i]):
                if i == len(self.sizes)-1: #-1 is beause the for loop is indexed from 0
                    self.outputs[i][x] = self.network[i][x].activation(self.outputs[i-1])
                    if x == (self.sizes[i]-1): #You need to -1 again!       
                        return self.outputs[i]

                elif i == 0:
                    self.outputs[0][x] = self.network[i][x].activation(map(int, str(input[x]))) #Now this is realy not working, I don't need to guess... D:
                else:
                    self.outputs[i][x] = self.network[i][x].activation(self.outputs[i-1])
    
    def convert(self,string):
        array = [0] * self.sizes[0]

        for i in xrange(len(string)):
            if string[i] != ' ':
                array[(i*26)+self.letterTable[string[i]]] = 1
        return array

    def unconvert(self,array):
        string = ''
        for i in xrange(len(array)/26):
            if 1 in array[(i*26):(i+1)*26]:
                string += self.letterTable[array[(i*26):(i+1)*26].index(1)]
            else:
                string += ' '
        return string

    def cost(self,input,output): #Source: http://rosettacode.org/wiki/Levenshtein_distance#Python         
        if len(input) > len(output):
            input,output = output,input
        distances = range(len(input) + 1)
        for index2,char2 in enumerate(output):
            newDistances = [index2+1]
            for index1,char1 in enumerate(input):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
            distances = newDistances
        return distances[-1] 
         
    def train():
        pass

network = Network([780,1000,10,1000,780])

def test(string):
    return network.unconvert(network.predict(network.convert(string)))

def benchmark():
    for i in xrange(10000):
        network = Network([1,i,i,i])
        print "3 Layers:","1 Layer of One Neuron","and 3 layers of",i,"neurons"
        start = time.time()
        network.predict([1])
        end = time.time()
        print "Took:",end - start,"seconds"
benchmark()

