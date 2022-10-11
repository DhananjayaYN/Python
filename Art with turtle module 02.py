# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 20:43:41 2022

@author: Laptop Outlet
"""

import turtle 
turtle.bgcolor('black')
turtle.hideturtle()
turtle.speed(15)

for i in range (120):
    turtle.pencolor('red')
    turtle.circle(i)
    turtle.right(3)
    
for i in range(120):
    turtle.pencolor('orange') 
    turtle.circle(i*0.8)
    turtle.right(3)

for i in range(120):
    turtle.pencolor('yellow') 
    turtle.circle(i*0.6)
    turtle.right(3)
    