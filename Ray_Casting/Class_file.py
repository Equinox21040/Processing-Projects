class Wall():
    def __init__(self,x3,y3,x4,y4):
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        stroke(255)
        strokeWeight(3)
        line(x3,y3,x4,y4)
        
    def intersect(self,x1,y1,angle):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1 + 800 * cos(radians(angle))
        self.y2 = y1 + 800 * sin(radians(angle))
        self.x2r = x1 + 20 * cos(radians(angle))
        self.y2r = y1 + 20 * sin(radians(angle))
        
        
        self.den = (self.x1 - self.x2)*(self.y3 - self.y4) - (self.y1 - self.y2)*(self.x3 - self.x4)
        self.t = ((self.x1 - self.x3)*(self.y3 - self.y4) - (self.y1 - self.y3)*(self.x3 - self.x4)) / self.den 
        self.u = ((self.x1 - self.x2)*(self.y1 - self.y3) - (self.y1 - self.y2)*(self.x1 - self.x3)) / self.den
        
        if self.t >= 0 and self.t <= 1 and -self.u >= 0 and -self.u <= 1 :
            self.x2p = self.x1 + self.t*(self.x2 - self.x1)
            self.y2p = self.y1 + self.t*(self.y2 - self.y1)
            return self.x2p , self.y2p
        else:
            return self.x2r , self.y2r
        
        
class Ray():
    def __init__(self,x1,y1,angle):
        stroke(255)
        strokeWeight(5)
        point(x1,y1)
        self.x2 = x1 + 20 * cos(radians(angle))
        self.y2 = y1 + 20 * sin(radians(angle))
        strokeWeight(3)
        line(x1,y1,self.x2,self.y2)
    
    
