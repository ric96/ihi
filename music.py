import pygame
import os
import random
import time
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
pygame.mixer.init()
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set("play", "0")
mc.set("title", "null")
while True:
	randomfile = random.choice(os.listdir("music/"))
	file = 'music/'+randomfile
	mc.set("title", randomfile)
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
  		pygame.time.Clock().tick(10)
		if mc.get("play") == "0":
			pygame.mixer.music.pause()
		elif mc.get("play") == "1":
			pygame.mixer.music.unpause()
		time.sleep(1)
