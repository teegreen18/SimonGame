from Draw import *
import random

sqaures = [(100, 100), (100, 300), (300, 100), (300, 300)]
colors = [(GREEN, DARK_GREEN), (YELLOW, WHITE), (RED, DARK_RED), (BLUE, DARK_BLUE)]
order = []
width = 200


def startScreen(): 
    setCanvasSize(600, 600)
    drawSq(GREEN, 100, 100, width)
    drawSq(YELLOW, 100, 300, width)
    drawSq(RED, 300, 100, width)
    drawSq(BLUE, 300, 300, width)
    drawCircle()
# four squares of different colors at (100, 100), (300, 100), (100, 300), (300, 300)
# all 200 wide and long
def drawSq(color, x, y, w):
    setColor(color)
    filledRect(x, y, width, width)

def drawCircle():
    setColor(BLACK)
    # black circle in the middle of the canvas
    # the x, y = 250, diameter = 75
    filledOval(250, 250, 110, 110)

def computerTurn():
    global width
    tile = random.randint(0, 3)
    order.append(tile)
    print(order)
    for sq in order:
        changeShade(colors[sq][0], sqaures[sq][0], sqaures[sq][1], width)
        changeShade(colors[sq][1], sqaures[sq][0], sqaures[sq][1], width)
        #if sq == 0:
            #changeShade(DARK_GREEN, sqaures[
        #elif sq == 1:
            #drawSq(WHITE, 100, 300, width)
            #drawCircle()            
            #show(2000)
            #drawSq(YELLOW, 100, 300, width)
            #drawCircle()            
            #show(1000)
        #elif sq == 2:
            #drawSq(DARK_RED, 300, 100, width)
            #drawCircle()        
            #show(2000)
            #drawSq(RED, 300, 100, width)
            #drawCircle()            
            #show(1000)
        #else:
            #drawSq(DARK_BLUE, 300, 300, width)
            #drawCircle()            
            #show(2000)
            #drawSq(BLUE, 300, 300, width)
            #drawCircle()            
            #show(1000)
            
# 0 is green, 1 is yellow, 2 is red, 3 is blue           
def determineSqClicked(x, y):
    if 100 <= x < 300 and 100 <= y < 300:
        return 0
    elif 100 <= x < 300 and 300 <= y < 500:
        return 1
    elif 300 < x <= 500 and 100 <= y < 300:
        return 2
    else:
        return 3
    
def changeShade(color, x, y, width):
    drawSq(color, x, y, width)
    drawCircle()            
    show(2000)  

def playerTurn():
    for tile in order:
        if mousePressed():
            pressedX = mouseX()
            pressedY = mouseY()
            
            tilePressed = determineSqClicked(pressedX, pressedY)
            changeShade(colors[tilePressed][0], sqaures[tilePressed][0], sqaures[tilePressed][1], width)
            changeShade(colors[tilePressed][1], sqaures[tilePressed][0], sqaures[tilePressed][1], width)
            
            
            if tilePressed != tile:
                return False 
    return True
                    
def playGame():
    startScreen()
    while True:
        computerTurn()
        playerTurn()
playGame()