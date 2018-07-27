'''Draggable Points, Reflection, Rotation
Feb. 24, 2017'''

from dragpoint import Dragpoint

def setup():
    global A,B,C,pointList
    size(600,600)
    A = Dragpoint(random(width),random(height))
    B = Dragpoint(random(width),random(height))
    C = Dragpoint(random(width),random(height))
    pointList = [A,B,C]
    
def draw():
    global pointList
    #translate(width/2,height/2)
    #noFill()
    background(255) #white
    
    # println("A: ("+str(A.x)+","+str(A.y)+')')
    # println("B: ("+str(B.x)+","+str(B.y)+')')
    # println("C: ("+str(C.x)+","+str(C.y)+')')
    
            
    for p in pointList:
        #println(p)
        p.update()
    #Sides of triangle ABC
    line(A.x,A.y,B.x,B.y)
    line(A.x,A.y,C.x,C.y)
    line(B.x,B.y,C.x,C.y)
    
    #medians
    D = midpointD(A,B)
    E = midpointD(A,C)
    F = midpointD(B,C)
    
    fill(255,255,0) #yellow
    line(A.x,A.y,F[0],F[1])
    ellipse(F[0],F[1],10,10)
    
    line(B.x,B.y,E[0],E[1])
    ellipse(E[0],E[1],10,10)
    
    line(C.x,C.y,D[0],D[1])
    ellipse(D[0],D[1],10,10)
    
    med1 = line2points(A,F)
    med2 = line2points(B,E)
    med3 = line2points(C,D)
    
    centroid = intersection(med1,med2)
    fill(0,255,255)
    ellipse(centroid[0],centroid[1],10,10)
    
    #calculate distances
    AC = dist(A.x,A.y,centroid[0],centroid[1])
    CF = dist(centroid[0],centroid[1],F[0],F[1])
    ACloc = [(A.x + centroid[0])/2.0,(A.y + centroid[1])/2.0]
    CFloc = [(F[0] + centroid[0])/2.0,(F[1] + centroid[1])/2.0]
    #fill(0)
    mAC = midpointD2(A,centroid)
    fill(0,255,0)
    ellipse(mAC[0],mAC[1],10,10)
    # textSize(24)
    # text(str(round(AC,1)),ACloc[0],ACloc[1])
    # text(str(round(CF,1)),CFloc[0],CFloc[1])
    
    BC = dist(B.x,B.y,centroid[0],centroid[1])
    CE = dist(centroid[0],centroid[1],E[0],E[1])
    BCloc = [(B.x + centroid[0])/2.0,(B.y + centroid[1])/2.0]
    CEloc = [(E[0] + centroid[0])/2.0,(E[1] + centroid[1])/2.0]
    mBC = midpointD2(B,centroid)
    fill(0,255,0)
    ellipse(mBC[0],mBC[1],10,10)
    # textSize(24)
    # text(str(round(BC,1)),BCloc[0],BCloc[1])
    # text(str(round(CE,1)),CEloc[0],CEloc[1])
    
    CC = dist(C.x,C.y,centroid[0],centroid[1])
    CD = dist(centroid[0],centroid[1],D[0],D[1])
    CCloc = [(C.x + centroid[0])/2.0,(C.y + centroid[1])/2.0]
    CDloc = [(D[0] + centroid[0])/2.0,(D[1] + centroid[1])/2.0]
    mCC = midpointD2(C,centroid)
    fill(0,255,0)
    ellipse(mCC[0],mCC[1],10,10)
    # textSize(24)
    # text(str(round(CC,1)),CCloc[0],CCloc[1])
    # text(str(round(CD,1)),CDloc[0],CDloc[1])
    
    #println(AC / CF)
    saveFrame("####.png")

def midpointD(P,Q):
    '''Returns the midpoint of two
    Draggable points'''
    midx = (P.x + Q.x)/2.0
    midy = (P.y + Q.y)/2.0
    return midx,midy

def midpointD2(P,Q):
    '''Returns the midpoint of two
    points, a draggable and regular'''
    midx = (P.x + Q[0])/2.0
    midy = (P.y + Q[1])/2.0
    return midx,midy

def midpoint(P,Q):
    '''Returns the midpoint of two
     points'''
    midx = (P[0] + Q[0])/2.0
    midy = (P[1] + Q[1])/2.0
    return midx,midy

def line2points(ptD,pt):
    '''Returns the slope and y-intercept
    of the line between two points. ptD is 
    a draggable point.'''
    slope = (pt[1] - ptD.y)/float(pt[0] - ptD.x)
    y_int = ptD.y - slope*ptD.x
    return slope, y_int

def intersection(line1,line2):
    '''Returns point of intersection between two 
    lines. Lines are lists: [slope,y_int]'''
    x = (line2[1] - line1[1])/float(line1[0]-line2[0])
    y = line1[0]*x + line1[1]
    return x,y

    
