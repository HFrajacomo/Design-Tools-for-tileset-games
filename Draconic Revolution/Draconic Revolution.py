import pygame as pg
import sys
from time import sleep
from threading import Thread, Event

sys.path.append('src\\')

from Bevel import Bevel
from Map import Map
from Tile import Tile
#from TiledMap import TiledMap
from Obj import Obj
from ServerHolder import *


def handle_mouse(ev):
	if(dict_gamestate[GAMESTATE] == 1):
		pass

def handle_keyboard(ev):
	global QUIT

	if(pg.key.name(ev.key) == "escape"): # Quit test
		QUIT = True

def handle_keyups(ev):
	pass

def screen_refresher():
	while(not QUIT):
		pg.display.flip()
		

pg.init()

dict_gamestate = {0:"LOADING", 1:"INGAME"}

screen = pg.display.set_mode((0,0), pg.FULLSCREEN | pg.HWSURFACE | pg.DOUBLEBUF) 
pg.display.set_caption("Draconic Revolution")

FPS = 30
threads = []
QUIT = False
GAMESTATE = 1

# Map
m = loadmap("map\\draconis")

# Bevels
map_bev = Bevel(1344, 960, (55,25,25,255), (0,0))  # Sobra x = 96 e y = 120
side_bev = Bevel(480, 1080, (155,155,155), (1440, 0))
minimap_bev = Bevel(300, 300, (200,0,0), (1440,0))
dynamicbuttons_bev = Bevel(180, 300, (200,200,0), (1740,0))
dynamicwindow_bev = Bevel(480, 360, (155,0,255), (1440, 300))
equipment_bev = Bevel(480,270,(80,80,80), (1440, 660))
hotkeys_bev = Bevel(480, 150, (255,255,255), (1440, 930))
lifebar_bev = Bevel(1440,20,(255,0,0),(0,960))
magicbar_bev = Bevel(1440,20,(0,0,255),(0,980))
apbar_bev = Bevel(1440,20,(0,255,0),(0,1000))
guardbar_bev = Bevel(1440,20,(180,0,180),(0,1020))
hungerbar_bev = Bevel(1440,20,(200,120,0),(0,1040))
sleepbar_bev = Bevel(1440,20,(200,200,200),(0,1060))

# Draw Bevels
map_bev.draw(screen)
side_bev.draw(screen)
minimap_bev.draw(screen)
dynamicbuttons_bev.draw(screen)
dynamicwindow_bev.draw(screen)
equipment_bev.draw(screen)
lifebar_bev.draw(screen)
magicbar_bev.draw(screen)
apbar_bev.draw(screen)
guardbar_bev.draw(screen)
hungerbar_bev.draw(screen)
sleepbar_bev.draw(screen)

# CLOCK
clock = pg.time.Clock()

threads.append(Thread(target=screen_refresher))

for th in threads:
	th.start()

while(not QUIT):
	for ev in pg.event.get():
		if(ev.type in [pg.MOUSEBUTTONDOWN]):#, pg.MOUSEMOTION, pg.MOUSEBUTTONUP]):
			handle_mouse(ev)
		elif(ev.type in [pg.KEYDOWN]):
			handle_keyboard(ev)
		elif(ev.type in [pg.KEYUP]):
			handle_keyups(ev)