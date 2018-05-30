from Draw import *
import random
import time

# 0 - green, 1 - yellow, 2 - red, 3 - blue
# list of x,y coordinates of the 4 tiles
sqaures = [(100, 100), (100, 300), (300, 100), (300, 300)]

DARK_YELLOW = color(198, 187, 35)
colors = [(GREEN, DARK_GREEN), (YELLOW, DARK_YELLOW), (RED, DARK_RED), (BLUE, DARK_BLUE)]
order = []

# global variable of the width of each square
width = 200


def startScreen(): 
    global width
    setCanvasSize(600, 600)
    
    # background color
    BEIGE = color(245, 225, 144)
    setBackground(BEIGE)    
    
    # words
    setFontSize(32)
    string("SIMON", 250, 30)
    string("Try to copy the sequence!", 115, 60)
    
    # board
    drawSq(DARK_GREEN, 100, 100, width)
    drawSq(DARK_YELLOW, 100, 300, width)
    drawSq(DARK_RED, 300, 100, width)
    drawSq(DARK_BLUE, 300, 300, width)
    drawCircle()

# function that takes in the color of a tile, the x, y coordinates and width
# and draw the square
def drawSq(color, x, y, w):
    setColor(color)
    filledRect(x, y, w, w)

# function that draws the circle in the middle 
def drawCircle():
    setColor(BLACK)
    # black circle in the middle of the canvas
    # the x, y = 250, diameter = 75
    filledOval(250, 250, 110, 110)
    
def checkMousePressed():
    return mouseX(), mouseY()

def computerTurn(tryAgain=False):
    global width
    global order
    global colors
    global sqaures
    
    if not tryAgain:
        seqSize = 5 # amount of tiles in the sequence 
        for i in range(seqSize):
            # pick a random tile
            tile = random.randint(0, 3)
            # add it to the order list
            order.append(tile)
        
    print(order)
    # in the computer turn, the tiles each are 'pressed' once in order
    # so change the color to 'pressed' color and then back
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
            
# 0 - green, 1 - yellow, 2 - red, 3 - blue   
# returns the number corresponding to the tile clicked
def determineSqClicked(x, y):
    if 100 <= x < 300 and 100 <= y < 300:
        return 0
    elif 100 <= x < 300 and 300 <= y < 500:
        return 1
    elif 300 < x <= 500 and 100 <= y < 300:
        return 2
    else:
        return 3

# function that redraws the board with input     
def changeShade(color, x, y, width):
    drawSq(color, x, y, width)
    drawCircle()            
    show(1000)  

# ?? not sure how this method is working or how to implement it correctly
def playerTurn():
    global colors
    global sqaures
    
    tile = 0
    playerTiles = []
    
    while tile <= len(order):
        if mousePressed():
            pressedX, pressedY = checkMousePressed()
            
            tilePressed = determineSqClicked(pressedX, pressedY)
            changeShade(colors[tilePressed][0], sqaures[tilePressed][0], sqaures[tilePressed][1], width)
            changeShade(colors[tilePressed][1], sqaures[tilePressed][0], sqaures[tilePressed][1], width)   
            
            playerTiles.append(tilePressed)
            
            #if tilePressed != tile:
                #return False  
                
                
            # move onto the next tile in the sequence
            # if the player didn't click, will continue through the while loop
            tile += 1 
            
    #for tile in order:
        #if mousePressed():
            #pressedX = mouseX()
            #pressedY = mouseY()
            
            #tilePressed = determineSqClicked(pressedX, pressedY)
            #changeShade(colors[tilePressed][0], sqaures[tilePressed][0], sqaures[tilePressed][1], width)
            #changeShade(colors[tilePressed][1], sqaures[tilePressed][0], sqaures[tilePressed][1], width)
            
            
            #if tilePressed != tile:
                #return False 
        #else:
            #time.sleep(10000000)
    print(playerTiles)
    
    if matchesComputer(playerTiles, order):
        showSuccessMessage()
        return True
    else:
        showFailMessage()
        return False

def matchesComputer(platerTiles, order):
    for i in range(len(order)):
        if order[i] != playerTiles[i]:
            return False
    return True

def showSuccessMessage():
    string("You got it! Let's make this harder...", 100, 80)
    time.sleep(3)
    startScreen()
    
def showFailMessage():
    string("You almost had it! Let's try it again...", 100, 80)
    time.sleep(3)
    startScreen()  
       
def playGame():
    startScreen()
    time.sleep(2) # pause after startup before showing sequence
    while True:
        computerTurn()
        status = playerTurn()
        if not status:
            computerTurn(tryAgain = True)   # giving the player a chance to do the same one again
playGame()