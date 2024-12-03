from turtle import *

color('red')
fillcolor('yellow')

forward(100)
color('blue')
left(120)
color('blue')
forward(100)
color('blue')
backward(100)
color('blue')
right(100)
color('blue')
width(10)
home()

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break