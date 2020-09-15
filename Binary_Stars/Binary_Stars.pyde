m1 = float(3)
m2 = float(1)
a = 400
t = 0
canvas = None

def setup():
    global canvas
    size(800,800)
    canvas = createGraphics(1000,1000)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    frameRate(120)
    
    
def draw():
    global t , canvas
    image(canvas,0,0)
    translate(width/2 , height/2)
    scale(1,-1)
    
    BarC1 = a*(m2 / (m1 + m2))
    BarC2 = -a*(m1 / (m1 + m2))
    
    x1 = BarC1 * cos(2 * PI * t)
    y1 = BarC1 * sin(2 * PI * t)
    x2 = BarC2 * cos(2 * PI * t)
    y2 = BarC2 * sin(2 * PI * t)
    
    fill(255)
    circle(x1,y1,m1 * 50)
    circle(x2,y2,m2 * 50)
    fill(255,0,0)
    circle(0,0,10)
    fill(0)
    
    canvas.beginDraw()
    canvas.stroke(255)
    canvas.strokeWeight(1)
    canvas.translate(400,400)
    canvas.scale(1,-1)
    if frameCount > 1 :
        canvas.beginShape()
        canvas.vertex(x1,y1)
        canvas.endShape()
        canvas.beginShape()
        canvas.vertex(x2,y2)
        canvas.endShape()
    canvas.endDraw()
    
    t = t + 0.0008333
