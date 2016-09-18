import pygame
import os
import subprocess
import time
from pygame.locals import *
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
screen = pygame.display.set_mode((800, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
back = pygame.image.load("project_images/back.jpg")
icon1 = pygame.image.load("project_images/icon1.png")
icon2 = pygame.image.load("project_images/icon2.png")
icon3 = pygame.image.load("project_images/icon3.png")
bar = pygame.image.load("project_images/bar.png")
back_button = pygame.image.load("project_images/back.png")
setting_button = pygame.image.load("project_images/setting.png")
home_button = pygame.image.load("project_images/home.png")
home_hover = pygame.image.load("project_images/home_hover.png")
setting_hover = pygame.image.load("project_images/setting_hover.png")
back_hover = pygame.image.load("project_images/back_hover.png")
bar = pygame.image.load("project_images/bar.png")
sun = pygame.image.load("project_images/sun.png")
wind = pygame.image.load("project_images/wind.png")
drop = pygame.image.load("project_images/drop.png")
font = pygame.font.Font("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf", 60)
font2 = pygame.font.Font("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf", 20)
font3 = pygame.font.Font("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf", 40)
music_logo = pygame.image.load("project_images/headph.png")
play = pygame.image.load("project_images/play-white.png")
pause = pygame.image.load("project_images/pause.png")


clock = pygame.time.Clock()
def main():
	while True:
		screen.blit(back, (0,0))
		home()
		pressed=pygame.key.get_pressed()
		for i in pygame.event.get():
			if pressed[K_q]:
				mc.set("play", "0")
				exit()
		clock.tick(30)
		pygame.display.set_caption(str(clock.get_fps()))
		pygame.display.update()

def home():
	while True:
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		screen.blit(icon1, (50,50))
		screen.blit(icon2, (271,50))
		screen.blit(icon3, (492,50))
		screen.blit(music_logo, (530,200))
		timedate()
		temp()
		blbar()
		if 50+171 > mouse[0] >50 and 50+370 > mouse[1] >50: #calander_button
			if click[0] == 1:
				calander()
		if 271+171 > mouse[0] >271 and 30+370 > mouse[1] >50: #weather_button
			if click[0] == 1:
				weather()
		if 492+171 > mouse[0] >492 and 30+370 > mouse[1] >50: #iot_button
			if click[0] == 1:
				music()
		pressed=pygame.key.get_pressed()
		for i in pygame.event.get():
                        if pressed[K_q]:
				mc.set("play", "0")
                                exit()
		return

def blbar():
	mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
	screen.blit(bar, (729,0))
        if 729+70 > mouse[0] > 729 and 225+70 > mouse[1] > 225: #hovered at back_button
                screen.blit(home_hover, (729,225))
        else:
                screen.blit(home_button, (729,225))

	return


def calander():
	subprocess.call("firefox https://calendar.google.com/calendar/render#main_7%7Cmonth", shell=True)
	return

def timedate():
	hour = font.render(time.strftime("%H:"), 1, (255, 255, 255))
        minute = font.render(time.strftime("%M"), 1, (255, 255, 255))
        second = font2.render(time.strftime("%S"), 1, (255, 255, 255))
        date = font.render(time.strftime("%d"), 1, (255, 255, 255))
        month = font2.render(time.strftime("%B"), 1, (255, 255, 255))
        year = font3.render(time.strftime("%Y"), 1, (255, 255, 255))
        day = font2.render(time.strftime("%A"), 1, (255, 255, 255))
        screen.blit(hour, (115,80))
        screen.blit(minute, (90,150))
        screen.blit(second, (170,160))
        screen.blit(date, (115,250))
        screen.blit(month, (70,310))
        screen.blit(year, (70,340))
        screen.blit(day, (60,380))
	return

def temp():
        temp = font3.render(str(mc.get("temp")), 1, (255,255,255))
        c = font2.render("\xb0C", 1, (255, 255, 255))
        hum = font3.render(str(mc.get("hum")), 1, (255,255,255))
        mod = font2.render("%", 1, (255, 255, 255))
        screen.blit(sun, (325, 60))
        screen.blit(temp, (320,135))
        screen.blit(c, (400, 140))
        screen.blit(drop, (320,260))
        screen.blit(hum, (285,340))
        screen.blit(mod,(370,350))

def weather():
	subprocess.call("firefox -new-window http://forecast.io/#/f/17.3753,78.4744", shell=True)
	return

def music():
	while True:
		name = font2.render(mc.get("title"), 1, (255, 255, 255))
       		screen.blit(back, (0,0))
		if mc.get("play") == "0":
			screen.blit(play, (300,140))
		elif mc.get("play") == "1":
			screen.blit(pause, (300,140))
		screen.blit(name, (90,400))
	        mouse = pygame.mouse.get_pos()
        	click = pygame.mouse.get_pressed()
		blbar()
	        if 729+70 > mouse[0] > 729 and 225+70 > mouse[1] > 225: #hovered at back_button
	                if click[0] == 1:
				return

                if 300+200 > mouse[0] > 300 and 140+200 > mouse[1] > 140:
                        if click[0] == 1:
                                if mc.get("play") == "0":
                                        mc.set("play", "1")
                                elif mc.get("play") == "1":
                                        mc.set("play", "0")
				time.sleep(1)
                pressed=pygame.key.get_pressed()
                for i in pygame.event.get():
                        if pressed[K_q]:
				mc.set("play", "0")
                                exit()
                clock.tick(30)
                pygame.display.set_caption(str(clock.get_fps()))
		pygame.display.update()


if __name__=='__main__':
	main()
