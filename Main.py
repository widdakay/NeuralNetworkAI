import pygame, sys, random, time, math

import network

from pygame.locals import *
 
class App:
	def __init__(self):
		self._running = True
		self.surf = None
		self.frameCount = 1
		self.startTime = time.time()

		self.size = self.width, self.height = -1, -1
		
		self.map = Map(32, 32)
		self.map.generate()

		self.viewPos = [0, 0]
		self.keys = {}
		for i in range(300):
			self.keys[i] = False
		self.creature = Creature()
 
	def on_init(self):
		pygame.init()
		self.size = self.width, self.height = pygame.display.list_modes()[0]

		self.surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
		pygame.mouse.set_visible(False)
		self._running = True
 
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
	def on_loop(self):
		if self.keys[pygame.K_LEFT]:
			self.viewPos[0] += 3

		if self.keys[pygame.K_UP]:
			self.viewPos[1] += 3

		if self.keys[pygame.K_RIGHT]:
			self.viewPos[0] -= 3

		if self.keys[pygame.K_DOWN]:
			self.viewPos[1] -= 3

		if self.keys[pygame.K_ESCAPE]:
			self._running = False

		mouse_pos = pygame.mouse.get_pos()

		self.viewPos[0] += mouse_pos[0]-self.width/2
		self.viewPos[1] += mouse_pos[1]-self.height/2

		pygame.mouse.set_pos([self.width/2, self.height/2])


		self.creature.sim(self.map)
		

	def on_render(self):
		self.surf.fill((0, 0, 0))
		if self.frameCount % 60 == 0:
			# regenerate terrain every second
			self.map.generate()

		self.map.draw(self.surf, self.viewPos)
		self.creature.draw(self.surf)

		self.frameCount += 1

	def on_cleanup(self):
		pygame.quit()
 
	def main(self):
		if self.on_init() == False:
			self._running = False
 
		while self._running:
			for event in pygame.event.get():
				self.on_event(event)
				if event.type == pygame.KEYDOWN:
					self.keys[event.key] = True
				if event.type == pygame.KEYUP:
					self.keys[event.key] = False
				if event.type == pygame.QUIT:
					self._running = False
				

			self.on_loop()
			self.on_render()
			pygame.display.flip()
		self.on_cleanup()

class Creature():
	def __init__(self):
		self.pos = [0,0]
		self.hunger = 0
		self.health = 10

	def draw(self, surface):
		pass
	def sim(self, map):
		pass



class Map():
	def __init__(self, xSize, ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.map = [[0 for x in xrange(self.xSize)] for y in xrange(self.ySize)]
		#print self.map

	def generate(self):
		islandPos = [random.uniform(0,self.xSize/4), random.uniform(0,self.ySize/4)]
		islandPos[0] += self.xSize/2 - self.xSize/4
		islandPos[1] += self.ySize/2 - self.ySize/4
		
		islandScale = [random.uniform(0,self.xSize/2), random.uniform(0,self.ySize/2)]
		islandScale[0] += (islandScale[0]+islandScale[1])/2
		islandScale[1] += (islandScale[0]+islandScale[1])/2



		for x in range(len(self.map)):
			for y in range(len(self.map[x])):
				#self.map[x][y] += random.randint(0,1)
				self.map[x][y] = min(80/((x-islandPos[0])**2 + (y-islandPos[1])**2 + 0.0001), 2)

		level1 = [[0 for x in xrange(self.xSize/8)] for y in xrange(self.ySize/8)]
		for x in range(len(level1)):
			for y in range(len(level1[x])):
				level1[x][y] = random.uniform(-1,1)

		level2 = [[0 for x in xrange(self.xSize/4)] for y in xrange(self.ySize/4)]
		for x in range(len(level2)):
			for y in range(len(level2[x])):
				level2[x][y] = random.uniform(-1,1)

		level3 = [[0 for x in xrange(self.xSize/2)] for y in xrange(self.ySize/2)]
		for x in range(len(level3)):
			for y in range(len(level3[x])):
				level3[x][y] = random.uniform(-1,1)

		level4 = [[0 for x in xrange(self.xSize/1)] for y in xrange(self.ySize/1)]
		for x in range(len(level4)):
			for y in range(len(level4[x])):
				level4[x][y] = random.uniform(-1,1)



		for x in range(len(self.map)):
			for y in range(len(self.map[x])):
				self.map[x][y] *= level1[x/8][y/8]*0.25+1
				self.map[x][y] *= 0.5*level2[x/4][y/4]*0.25+1
				self.map[x][y] *= 0.25*level3[x/2][y/2]*0.25+1
				self.map[x][y] *= 0.125*level4[x/1][y/1]*0.25+1

		for x in range(len(self.map)):
			for y in range(len(self.map[x])):
				if self.map[x][y] > 1:
					if random.random() > 0.95:
						self.map[x][y] = 9
		#print self.map





	def draw(self, surf, offset):
		for x in range(len(self.map)):
			for y in range(len(self.map[x])):
				#print x, y, self.map[x][y]
				color = (0,0,0)
				if self.map[x][y] < 1:
					color = (10,30,90)
				elif self.map[x][y] < 2:
					color = (230,200,100)
				elif self.map[x][y] < 3:
					color = (50,230,30)
				elif self.map[x][y] < 10:
					color = (240,50,80)
				#color = (random.random()*255,random.random()*255,random.random()*255)
				#pygame.draw.rect(surf, color, (x*20,y*20,20,20))



				scale = 30
				short = scale/(2*math.sqrt(3))
				side = short*2

				pygame.draw.polygon(surf, color, hexagon(x*(short*3)+offset[0], y*scale+x*(scale/2)+offset[1], scale/2))


def hexagon(x, y, size):
	sqrt3 = math.sqrt(3)
	short = size/sqrt3
	side = short*2

	return (
		(x+short, y),
		(x+short+side, y),
		(x+short*2+side, y+size),

		(x+short+side, y+size*2),
		(x+short, y+size*2),
		(x, y+size)
		)

if __name__ == "__main__" :
	app = App()
	app.main()

