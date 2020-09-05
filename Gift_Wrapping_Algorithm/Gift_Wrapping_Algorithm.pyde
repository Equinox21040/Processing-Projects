number = 100
points = []
leftmost_point = []
index = 1
leftmost_point_buffer = []
convex_hull = []


def setup():
    size(800,800)
    frameRate(30)
    
    global points,leftmost_point,leftmost_point_buffer
    
    
    #Creating points
    for i in range(number):
        x = random(100,700)
        y = random(100,700)
        dots = [x,y]
        points.append(list(dots))
    
    #Finding Leftmost point    
    points.sort()
    leftmost_point = list(points[0])
    leftmost_point_buffer = leftmost_point
    
def draw():
    background(0)
    translate(0,800)
    scale(1,-1)
    
    global points,leftmost_point,index , leftmost_point_buffer , convex_hull
    
    
    
    #Displaying Points
    stroke(255)
    strokeWeight(10)
    for i in range(len(points)):
        point(points[i][0],points[i][1])
    
    #finding next point in convex hull 
    
    target_point = [points[index][0] , points[index][1]]
    
    for i in range(len(points)):
        strokeWeight(1)
        diff = [leftmost_point[0] - target_point[0] , leftmost_point[1] - target_point[1]]
        
        target = [leftmost_point[0]  - points[i][0] , leftmost_point[1] - points[i][1]]
        
        cross_pro = diff[0]*target[1] - diff[1]*target[0]
        
        if cross_pro > 0 :
            target_point = [points[i][0],points[i][1]]
    
    
    point(target_point[0] , target_point[1])
    
    
    
    #Reassigning the new point as the old starting point 
    
    leftmost_point = list(target_point)
    
    convex_hull.append(list(target_point))
    
    index = index + 1
    
    if target_point[0] == leftmost_point_buffer[0] and target_point[1] == leftmost_point_buffer[1]  :
        noLoop()
        
    #Drawing convex Hull
    
    for i in range(len(convex_hull) - 1):
        stroke(255,153,51)
        strokeWeight(5)
        line(convex_hull[i][0],convex_hull[i][1],convex_hull[i + 1][0],convex_hull[i + 1][1])
    line(convex_hull[0][0],convex_hull[0][1],convex_hull[len(convex_hull)-1][0],convex_hull[len(convex_hull)-1][1])
        
        
                       
    
