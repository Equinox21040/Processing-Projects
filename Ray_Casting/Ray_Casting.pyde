from Class_file import * 
x1 = 0
y1 = 0
wall_point = []
no_walls = 5
list_dist = []

def setup():
    global x3,x4,y3,y4
    size(800,800)
    frameRate(120)
    for i in range(no_walls):
        x3 = random(100,700)
        x4 = random(100,700)
        y3 = random(100,700)
        y4 = random(100,700)
        wall_point.append(x3)
        wall_point.append(y3)
        wall_point.append(x4)
        wall_point.append(y4)
    
    
    
def draw():
    background(0)
    global x1,y1,wall_point,list_dist
    x1 = mouseX
    y1 = mouseY
    loc = 0
    
    for i in range(no_walls):
        
        for i in range(0,360,20):
            Ray(x1,y1,i)
            Wall1 = Wall(wall_point[loc + 0],wall_point[loc + 1],wall_point[loc + 2],wall_point[loc + 3])
            intersect_point = Wall1.intersect(x1,y1,i)
            intersect_point = list(intersect_point)
            line(x1,y1,intersect_point[0],intersect_point[1])
            distance = dist(x1,y1,intersect_point[0],intersect_point[1])
            
        loc = loc + 4 
