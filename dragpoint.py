dragging = False

class Dragpoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = 5
        self.selected = False
        
    def update(self):
        #check if mouse is on a point
        if dist(mouseX,mouseY,self.x,self.y) < self.r + 10 and mousePressed:
            self.selected = True
            self.x = mouseX
            self.y = mouseY
            
        fill(0)  
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
        fill(255,0,0)
        # text("("+str(round(self.x,1))+","+str(round(self.y,1))+")",
        #      self.x+5,self.y+5)
        
