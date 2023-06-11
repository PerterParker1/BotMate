import random
from turtle import *
 
my_turtle = Turtle()
my_win = my_turtle.getscreen()
 
def tree(branch_len,t):
    if branch_len > 5:
        if branch_len <= 20:
            t.pencolor('green')  
        else:
            t.pencolor('black')
        t.pensize(branch_len//10)  
        t.fd(branch_len)
        degree = random.randint(15,30)  
        t.rt(degree)
        gap = random.uniform(10,15)  
        tree(branch_len-gap,t)
        t.lt(2*degree)
        tree(branch_len-gap, t)
        t.rt(degree)
        t.backward(branch_len)

my_turtle.setheading(90)
my_turtle.speed(10)
my_turtle.up()
my_turtle.backward(300)
my_turtle.down()
tree(100,my_turtle)
 
my_win.exitonclick()