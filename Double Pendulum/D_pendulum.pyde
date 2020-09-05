x1 = 0
y1 = 0
x2 = 0
y2 = 0
px2 = 0
py2 = 0
m1 = 30
m2 = 30
r1 = 150
r2 = 300
a1 = PI/2
a2 = PI/2
a1_v = 0
a2_v = 0
a1_a = 0
a2_a = 0
g = 1
canvas  = None


def setup():
    size(1000,1000)
    global canvas
    canvas = createGraphics(1000,1000)
    canvas.beginDraw()
    canvas.background(255)
    canvas.endDraw()
    frameRate(90)
    
def draw():
    global x1,y1,x2,y2,a1,a2,a1_v,a2_v,a1_a,a2_a,m1,m2,canvas,px2,py2
    image(canvas,0,0)
    #background(255,255,255)
    translate(500,500)
    rectMode(CENTER)
    rect(0,0,30,30)
    fill(0,0,0)
    strokeWeight(5)
    x1 = r1*sin(a1)
    y1 = r1*cos(a1)
    x2 = r2*sin(a2) + x1
    y2 = r2*cos(a2) + y1
    
    line(0,0,x1,y1)
    line(x1,y1,x2,y2)
    circle(x1,y1,m1)
    circle(x2,y2,m2)
    
    a1_v = a1_v + a1_a
    a2_v = a2_v + a2_a
    a1 = a1 + a1_v
    a2 = a2 + a2_v
    
    
    num1 = -g*(2*m1 + m2)*sin(a1)
    num2 = -m2*g*sin(a1 - 2*a2)
    num3 = -2*sin(a1 - a2)*m2
    num4 = sq(a2_v)*r2 + sq(a1_v)*r1*cos(a1 - a2)
    den1 = r1*(2*m1 + m2 - m2*cos(2*a1 - 2*a2))
    
    a1_a = 0.80*(num1 + num2 + num3*num4)/den1
    
    
    num5 = 2*sin(a1 - a2)
    num6 = sq(a1_v)*r1*(m1 + m2)
    num7 = g*(m1+m2)*cos(a1)
    num8 = sq(a2_v)*r2*m2*cos(a1 - a2)
    den2 =  r2*(2*m1 + m2 - m2*cos(2*a1 - 2*a2))
    
    a2_a = 0.80*(num5*(num6 + num7 + num8)) / den2
    
    
    
    canvas.beginDraw()
    canvas.strokeWeight(5)
    canvas.translate(500,500)
    if frameCount > 1 :
        canvas.line(px2,py2,x2,y2)
    canvas.endDraw()
    
    
    px2 = x2
    py2 = y2
