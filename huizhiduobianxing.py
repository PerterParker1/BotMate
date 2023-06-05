import turtle as t

t.setup(500, 400)

def my_draw(r):
    t.circle(r)
    t.circle(r) 
    t.circle(r)
    t.circle(r, 360, 16)
    t.circle(r, 360, 12)   
    t.circle(r, 360, 8)   
    t.circle(r, 360, 4)   
my_draw(150)
my_draw(200)
my_draw(250)


t.done()