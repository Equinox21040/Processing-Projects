angle = 45



def setup():
  size(800,800)


def draw():
  background(51)
  stroke(255)
  translate(width/2, height)
  branch(200)


def branch(l) :
  line(0,0,0,-l)
  translate(0, -l)
  if l > 1 :
    push()
    rotate(angle)
    branch(l * 0.67)
    pop()
    push()
    rotate(-angle)
    branch(l * 0.67)
    pop()
  

def mouseWheel(event):
    global angle
    angle = angle + 0.1
 
