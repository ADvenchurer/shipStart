import random
import intertools
import pgzrun

WIDTH = 400
HEIGHT = 400

BLOCK_POSITIONS = [
    (350,50)
    (350,350)
    (50,350)
    (50,50)
]

block_positions = intertools.cycle(BLOCK_POSITIONS)

block = Actor('block', center = (50,50))
ship = Actor('ship', center = (200,200))

def draw():
    screen.clear()
    block.draw()
    ship.draw()

pgzrun.go()