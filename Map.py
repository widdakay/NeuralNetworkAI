import random, math, pygame


class Map():
	def __init__(self, xSize, ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.map = [[0 for x in xrange(self.xSize)] for y in xrange(self.ySize)]
	
	def getNeighbors(self, x, y):
		return (self.map[x][y])

	def generate(self):
		islandPos = [random.uniform(0,self.xSize/8), random.uniform(0,self.ySize/8)]
		islandPos[0] += self.xSize/2 - self.xSize/8
		islandPos[1] += self.ySize/2 - self.ySize/8
		
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





	def draw(self, surf, offset, scale):
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

				short = scale/(2*math.sqrt(3))
				side = short*2

				pygame.draw.polygon(surf, color, hexagon(self.project([x,y], offset, scale), scale/2))
				pygame.draw.lines(surf, (255,255,255), True, hexagon(self.project([x,y], offset, scale), scale/2))
	def project(self, worldPos, offset, scale):
		short = scale/(2*math.sqrt(3))
		side = short*2

		return [worldPos[0]*(short*3)+offset[0], worldPos[1]*scale+worldPos[0]*(scale/2)+offset[1]]



def hexagon(pos, size):
	x = pos[0]
	y = pos[1]

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
