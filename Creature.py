import math, pygame, random
from network import Network

class Creature():
	def __init__(self):
		self.pos = [0,0]
		self.hunger = 0
		self.health = 10
		self.network = Network()
		self.counter = 0
		self._living = False
		self.color = (127,255,64)
		self.direction = 0


	def draw(self, surf, world):
		offset = world.project(self.pos)
		offset = [int(offset[0]+world.scale/2), int(offset[1]+world.scale/2)]
		"""[
		int(viewPos[0] + self.pos[0]*(short*3) + short*2),
		int(viewPos[1] + self.pos[1]*scale+self.pos[0]*(scale/2) + scale/2)
		]"""

		pygame.draw.circle(surf, self.color, offset, int(world.scale/2))
		pygame.draw.line(surf, (255,0,0), offset, [
			offset[0]+math.cos((5-self.direction+2)*(math.pi/3))*world.scale/2,
			offset[1]+math.sin((5-self.direction+2)*(math.pi/3))*world.scale/2
			])

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

	def getInputArray(self, map):
		array = []
		# is there a dangerous object ahead
		# is there food ahead

		if self.direction == 0:
			array[0] = map[self.pos[0]+0][self.pos[1]]
		

	def sim(self, world):
		if self._living == False:
			return
		if self.pos[0] >= world.xSize:
			self.pos[0] == 0
		if self.pos[1] >= world.ySize:
			self.pos[1] == 0

		if self.counter % 1 == 0:
			output = self.network.simulate([1,1,1])
			self.direction += int(output[0])

			
			self.direction %= 6
			self.pos = world.move(self.pos, self.direction, 1)
			print self.direction

		self.timestep(world)
		
		self.counter += 1


if __name__ == "__main__":
	import Main
	Main.run()