import pgzrun
import random


WIDTH = 700
HEIGHT = 500

next_satellite=0

total_satellites=8


satellites = []
lines = []

for i in range (total_satellites):
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
    for line in lines:
        
        screen.draw.line(line[0], line[1], (255, 255, 255))



def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite<total_satellites:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite: 
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite=next_satellite+1
        else:
            lines=[]
            next_satellite=0
pgzrun.go()