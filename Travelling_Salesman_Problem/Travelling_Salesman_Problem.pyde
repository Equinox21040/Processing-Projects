from math import factorial 


# Variables 
dots = []
number = 5
distance = []
k = float(0)
least_vaule = 0
dots1 = []
a = list(range(number))


def setup():
    global dots,number
    size(800,800)
#Assigning Dots 
    for i in range(number):
        x = random(100,700)
        y = random(100,700)
        a = [x,y]
        dots.append(a)
        frameRate(10)
        
        
def draw():
    background(0)
    global distance,k,dot_dist,a,lol,least_value,dots1
    
    
    #Creating Dots
    stroke(255)
    strokeWeight(15)
    for i in range(number):
        point(dots[i][0],dots[i][1])
    
    
    
    #Creating Lines and list of distances
    strokeWeight(1)
    for i in range(number - 1):
        line(dots[i][0],dots[i][1],dots[i + 1][0],dots[i + 1][1])
        distance.append(dist(dots[i][0],dots[i][1],dots[i + 1][0],dots[i + 1][1]))
        
        
    #Adding up Distances
    total_distance = sum(distance)
    distance = []
    
    #Percentage Counter
    textSize(20)
    per = float(((k) / (factorial(number) - 1))*100)
    text("Percentage Completed " + str(per) , 10 ,30)
    
    
    
    
    #Check for least distance
    if k == 0 :
        least_value = total_distance
        dots1.append(list(dots))
            
            
            
    if total_distance <= least_value : 
        least_value = total_distance
        dots1.append(list(dots))
    
    
    
    
    #End statement
    if k == factorial(number) - 1:
        line_draw(dots1[len(dots1) - 1])
        textSize(20)
        text("Smallest Possilble Distance is " + str(least_value),10,780)
        noLoop()
    
    
    
    #Lexcicograpic Order Generation 
    largestI = -1
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            largestI = i
    largestJ = -1
    for j in range(len(a)):
        if a[j] > a[largestI]:
            largestJ = j
    
    a[largestI], a[largestJ] = a[largestJ], a[largestI]
    
    b = a[largestI + 1:]
    b.reverse()
    a[largestI + 1:] = b
    
    dots[largestI], dots[largestJ] = dots[largestJ], dots[largestI]
    
    b = dots[largestI + 1:]
    b.reverse()
    dots[largestI + 1:] = b
    
    k = k + 1
    
def line_draw(dots1):
    strokeWeight(5)
    stroke(255,153,51)
    for i in range(number - 1):
        line(dots1[i][0],dots1[i][1],dots1[i + 1][0],dots1[i + 1][1])
