xpos = -100
ypos = 100
xvel = 5
yvel = 3
xac = 0
yac = 0
S = 8000
canvas = None


def setup():
    global canvas
    size(800,800)
    canvas = createGraphics(800,800)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    frameRate(120)
    
    
    
    
def draw():
    
    
    global xpos,ypos,xvel,yvel,xac,yac
    
    #background(0)
    image(canvas,0,0)
    translate(width/2,height/2)
    scale(1,-1)
    
    
    #Attractor
    circle(0,0,50)
    
    
    #object
    
    circle(xpos,ypos,10)
    pxpos = xpos
    pypos = ypos
    
    
    canvas.beginDraw()
    canvas.stroke(255)
    canvas.strokeWeight(1)
    canvas.translate(400,400)
    canvas.scale(1,-1)
    if frameCount > 1 :
        canvas.line(pxpos,pypos,xpos,ypos)
    canvas.endDraw()
    
    
    
    #mechanics
    uxpos = xpos / (((xpos**2) + (ypos**2))** 0.5)
    uypos = ypos / (((xpos**2) + (ypos**2))** 0.5)
    
    xac = -(uxpos * S) / ((xpos**2) + (ypos**2))
    yac = -(uypos * S) / ((xpos**2) + (ypos**2))
    
    xvel = xvel + xac
    yvel = yvel + yac
    
    
    
    
    xpos = xpos + xvel
    ypos = ypos + yvel
   
    
   
    
  
