import pgzrun
import random
from time import time

WIDTH = 700
HEIGHT = 500

r=255
g=0
b=0

message="start"

next_satellite=0

total_satellites=8


satellites = []
lines = []

for i in range (total_satellites):
    satellite = Actor ("satellite")
    satellite.pos = random.randint (0, 650), random.randint (0, 450)
    satellites.append(satellite)
    
global start_time
start_time=time()

def update():
    pass

def draw():
    global start_time, elapsed_time
    message=1
    screen.fill((r, g, b))
    for i in satellites:
        i.draw()
        screen.draw.text(str(message),(i.pos[0],i.pos[1]+25 ), color="red")
        message=message+1   
    for line in lines:
        
        screen.draw.line(line[0], line[1], (255, 255, 255))

    if next_satellite<total_satellites:
        elapsed_time=time()-start_time
        elapsed_time=round(elapsed_time,2)
        screen.draw.text(str(elapsed_time),(650, 0), color="green")
    else:
        screen.draw.text(str(elapsed_time),(650, 0), color="green")
        
def on_mouse_down(pos):
    global next_satellite, lines, r, g, b
    if next_satellite<total_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite: 
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
                r=random.randint(0,255)
                g=random.randint(0, 255)
                b=random.randint(0, 255)
                        
            next_satellite=next_satellite+1

        else:
            lines=[]
            next_satellite=0
            g=b=0
            r=255
pgzrun.go()