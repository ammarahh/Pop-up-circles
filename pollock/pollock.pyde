def setup():
    size(512,512)
    
def draw():
    fill(255,random(255),0)
    ellipse(random(0,512), random(0,512), random(20,50), random(20,50))
