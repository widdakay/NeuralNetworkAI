import pygame, sys, time, math

import network
from Map import Map
from Creature import Creature

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

		self.scale = 30.0

		for i in range(300):
			self.keys[i] = False
		self.creature = Creature()
 
	def on_init(self):
		pygame.init()
		displayModes = pygame.display.list_modes()
		print "Display modes:", displayModes
		x = displayModes[0][0]
		y = displayModes[0][1]

		if x > 1440:
			x = 1440
		if y > 900:
			y = 900

		mode = (x,y)
		print "Using mode:", mode
		self.size = self.width, self.height = mode

		self.surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
		pygame.mouse.set_visible(False)


		self.creature.place(self.map)

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
		if self.frameCount % 240 == 0:
			# regenerate terrain every 2 seconds
			self.map.generate()
			self.creature.place(self.map)

		if self.creature._living == False:
			self.creature.place(self.map)

		self.map.draw(self.surf, self.viewPos, self.scale)
		self.creature.draw(self.surf, self.viewPos, self.scale)

		self.frameCount += 1

	def on_cleanup(self):
		pygame.quit()
	def setScale(self, oldScale, scale):
		if scale < 1:
			return
		self.viewPos = [(self.viewPos[0] - self.width/2)*(scale/oldScale)+self.width/2, (self.viewPos[1] - self.height/2)*(scale/oldScale)+self.height/2]
		self.scale = scale
 
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
				if event.type == MOUSEBUTTONDOWN:
					if event.button == 4:
						self.setScale(self.scale, self.scale * 1.03)
					if event.button == 5:
						self.setScale(self.scale, self.scale * 0.97)
				

			self.on_loop()
			self.on_render()
			pygame.display.flip()
		self.on_cleanup()




if __name__ == "__main__" :
	app = App()
	app.main()

