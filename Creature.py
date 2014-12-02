import math, pygame, random
from ConnerNetwork import Network

class Creature():
	def __init__(self):
		self.pos = [0,0]
		self.hunger = 0
		self.health = 10
		self.network = Network([3,3,2])
		self.counter = 0
		self._living = False


	def draw(self, surf, viewPos, scale):
		color = (191,255,32)
		short = scale/(2*math.sqrt(3))

		offset = [
		int(viewPos[0] + self.pos[0]*(short*3) + short*2),
		int(viewPos[1] + self.pos[1]*scale+self.pos[0]*(scale/2) + scale/2)
		]

		pygame.draw.circle(surf, color, offset, int(scale/2))

	def place(self, world):
		while self._living == False:
			self._living = True
			self.pos = [random.randint(0, world.xSize), random.randint(0, world.ySize)]
			self.timestep(world)

	def timestep(self, world):
		if self.pos[0] > world.xSize or self.pos[0] < 0:
			self._living = False

		if self.pos[1] > world.ySize or self.pos[1] < 0:
			self._living = False

		if self._living == False:
			return
		try:
			if world.map[self.pos[0]][self.pos[1]] < 1:
				self._living = False
		except IndexError:
			self._living = False
			return
			

	def sim(self, world):
		if self._living == False:
			return
		if self.pos[0] >= world.xSize:
			self.pos[0] == 0
		if self.pos[1] >= world.ySize:
			self.pos[1] == 0

		if self.counter % 7 == 0:
			self.pos[0] += 1

		self.timestep(world)
		
		self.counter += 1
