import random, math, pygame


class Map():
	def __init__(self, xSize, ySize):
		self.xSize = xSize
		self.ySize = ySize
		self.scale = 30
		self.viewPos = [0,0]
		self.map = [[0 for x in xrange(self.xSize)] for y in xrange(self.ySize)]

		pygame.font.init()
		self.font = pygame.font.Font(None, 30)

	def getNeighbors(self, x, y):
		return (self.map[x][y])

	def getTileAt(self, pos):
		return self.map[pos[0]][pos[1]]

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





	def draw(self, surf):
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



				#pygame.draw.circle(surf, color, [int(self.project([x,y])[0]+2*side), int(self.project([x,y])[1]+2*side)], self.scale/2)

				pygame.draw.polygon(surf, color, hexagon(self.project([x,y]), self.scale/2))
				pygame.draw.lines(surf, (255,255,255), True, hexagon(self.project([x,y]), self.scale/2))
		self.drawHUD(surf)

	def drawHUD(self, surf):
		label = self.font.render("Beta", 1, (255,255,255))
		surf.blit(label, (10,10))

	def project(self, worldPos):
		short = self.scale/(2*math.sqrt(3))
		side = short*2

		x = int(worldPos[0]*(short*3)+self.viewPos[0])
		if worldPos[0] % 2 == 1:
			yOff = 0*(self.scale/2)
		else:
			yOff = -(self.scale/2)
		y = int(worldPos[1]*self.scale+yOff+self.viewPos[1])

		return [x, y]

	def move(self, pos, dir, dist):
		dir %= 6
		neighbors = [
		   [ [+1,  0], [+1, -1], [ 0, -1],
		     [-1, -1], [-1,  0], [ 0, +1] ],
		   [ [+1, +1], [+1,  0], [ 0, -1],
		     [-1,  0], [-1, +1], [ 0, +1] ]
		]
		parity = pos[0]%2
		d = neighbors[parity][dir]
		return [pos[0] + d[0], pos[1] + d[1]]



def hexagon(pos, size):
	x = pos[0]
	y = pos[1]

	sqrt3 = math.sqrt(3)
	short = size/sqrt3
	side = short*2

	vertices = []

	for i in range(6):
		angle = 2 * math.pi / 6 * (i + 0.5)

		vertices.append([size * math.cos(angle) + x, size * math.cos(angle) + y])
		#print vertices
	#return vertices
	return (
		(x+short, y),
		(x+short+side, y),
		(x+short*2+side, y+size),

		(x+short+side, y+size*2),
		(x+short, y+size*2),
		(x, y+size)
		)


if __name__ == "__main__":
	import Main
	Main.run()
