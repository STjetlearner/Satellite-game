import pgzrun
import random


WIDTH = 700
HEIGHT = 500

satellites = []

for i in range (8):
    satellite = Actor ("satellite")
    satellite.pos = random.randint (0, 700), random.randint (0, 500)
    satellites.append(satellite)
    
def draw():
    message=1
    screen.blit("star background", (0, 0))
    for i in satellites:
        i.draw()
        screen.draw.text(str(message),(i.pos[0],i.pos[1]+25 ), color="red")
        message=message+1
pgzrun.go()