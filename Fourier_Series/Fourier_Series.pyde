#number of circles
number = 1000
#point list
points = []

#time
dt = 0.0087
time = 0

#pause
p = 1



def setup():
    size(800,800)
    frameRate(120)
    
    
def draw():
    global number
    
    
    #Cartesian system
    background(0)
    translate(400,400)
    scale(1,-1)
    
    
    #Initial Variables
    radius = 100
    x = -200
    y = 0
    global time,p,points
    
    
    #Loop for drawing circles
    for n in range(1,2 *(1 + number), 2):
        circle_creation(x,y,radius,n,time)
        radius1 = (4 / (PI*n)) * radius
        x = x + (radius1 * cos(PI* n * time))
        y = y + (radius1 * sin(PI* n * time))
    points.insert(0,y)
        
    #Drawing the mapping line    
    line(x,y,100,y)
    
    #Draw The Graph
    beginShape()
    for i in range(len(points)):
      vertex(100 + i , points[i])
      if i > 300 :
          points.pop(i)
          print("W")
    endShape()
    
    #Limit on points memory
    #if len(points) > 1000:
        #points = []
    
    
    
    #Time increment
    time = time + dt*p
   
   
   
   
#Function to create Circles and rotating lines    
def circle_creation(pos_x,pos_y,radius,n,time):
    fill(0)
    stroke(255)
    strokeWeight(2)
    radius = (4 / (n * PI)) * radius
    circle(pos_x,pos_y,2 * radius)
    x_pos = radius * cos(PI* n * time)
    y_pos = radius * sin(PI* n * time)
    line(pos_x,pos_y,pos_x + x_pos,pos_y + y_pos)
    
    
    
#Pause and resume 
def mousePressed():
    global p 
    p = 0
    
def keyPressed():
    global p 
    p = 1
