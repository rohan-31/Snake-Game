import os, random

path = os.getcwd()
NUM_ROWS = 20
NUM_COLS = 20
RESOLUTION = 600
TILE_WIDTH = RESOLUTION/NUM_COLS 
TILE_HEIGHT = RESOLUTION/NUM_ROWS
BOUND = 600 #BOUNDARY OF THE PLAYING BOARD

class Main_Snake:  #MAIN SNAKE CLASS TO INITIALIZE SNAKE ELEMENTS
    
    def __init__(self):
        self.piece1 = loadImage(path + "/GameImages/head_left.png") #LOADING HEAD IMAGE
        self.piece2 = loadImage(path + "/GameImages/head_up.png") #LOADING HEAD IMAGE
        self.greenn = loadImage(path + "/GameImages/green.png") #LOADING BODY IMAGE(80, 153, 32)
        self.redd = loadImage(path + "/GameImages/red.png")#LOADING RED BODY IMAGE(Apple: 173, 48, 32)
        self.yellow = loadImage(path + "/GameImages/yellow.png")#LOADING YELLOW BODY IMAGE(Banana: 251, 226, 76)
        self.head = self.piece1 
        self.body = [] #HOLDS BODY ELEMENTS
        self.Max_Length = 400
        self.dir = RIGHT #INTIAL DIRECTION
        self.direction = RIGHT 
        self.Switcher = [[LEFT,RIGHT], [DOWN,UP], [RIGHT,LEFT], [UP,DOWN] ]
        self.bound = BOUND
            

         
class Snake(Main_Snake): #SNAKE SUB CLASS FOR INDIVIDUAL ELEMENTS
     def __init__(self):
         Main_Snake.__init__(self)
         self.body = []
         self.body.insert(0,self.head)
         for i in range(2):
            self.body.append(self.greenn)
         self.x = [300]*len(self.body)
         self.y = [300]*len(self.body)
         self.alive = True
         self.collide = False
         self.count = 0
         self.dir = RIGHT
    
     def update(self):  #METHOD USED TO UPDATE THE ELEMENTS OF THE SNAKE AND THEIR ATTRIBUTES
         
         for i in range(len(self.body)-1,0,-1):
             self.x[i] = self.x[i-1]
             self.y[i] = self.y[i-1]
                    
         for i in range(3,len(self.body)): 
                if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                    text("Game over", 270, 300)
                    text("Your score : " + str(game.fruit.count),260,400)
                    self.alive = False
                    self.x[0] += 6000
                    self.y[0] += 6000
    
             
         if [self.dir, self.direction] in self.Switcher: #USED TO PREVENT OPPOSTE SIDE MOVEMENTS.
             if self.dir == LEFT:
                 self.x[0] += 30
                 
             if self.dir == RIGHT:
                 self.x[0] += -30
                 
             if self.dir == UP:
                 self.y[0] += 30
                 
             if self.dir == DOWN:
                 self.y[0] += -30
                 
                 
         if self.dir == LEFT and self.direction != RIGHT: #SPEED  AND CHECKS FOR DIRECTIONS.
                self.direction = LEFT
                self.head = self.piece1
                self.x[0] += -30
            
         if self.dir == RIGHT and self.direction != LEFT: #SPEED  AND CHECKS FOR DIRECTIONS.
                self.direction = RIGHT
                self.head = self.piece1
                self.x[0] += 30
            
         if self.dir == UP and self.direction != DOWN: #SPEED  AND CHECKS FOR DIRECTIONS.
                self.direction = UP
                self.head = self.piece2
                self.y[0] += -30
            
         if self.dir == DOWN and self.direction != UP: #SPEED  AND CHECKS FOR DIRECTIONS.
                self.direction = DOWN
                self.head = self.piece2
                self.y[0] += 30
                 
                
         if self.x[0] + 30 > self.bound or self.x[0] < 0: #BOUNDARY CHECKS
                text("Game Over",270,300)
                text("Your score : " + str(game.fruit.count),260,400)
                self.alive = False
                
                
         if self.y[0] + 30 > self.bound or self.y[0] < 0: #BOUNDARY CHECKS
                text("Game Over",270,300)
                text("Your score : " + str(game.fruit.count),260,400)
                self.alive = False

            
         
     def display_1(self,X1=0,Y1=0,X2=30,Y2=30): #METHOD USED TO DISPLAY THE SNAKE BODY.    
         for i in range(0,len(self.body)):
             image(self.body[i], self.x[i], self.y[i],30,30,30,30,0,0) #GENERATING DEFAULT RIGHT ROTATED IMAGE.
             if self.direction == LEFT:
                 self.body[0] = self.piece1
                 image(self.body[i], self.x[i], self.y[i]) #GENERATING LEFT-FACING IMAGE.
             elif self.direction == RIGHT:
                 self.body[0] = self.piece1
                 image(self.body[i], self.x[i], self.y[i],30,30,30,30,0,0) #GENERATING RIGHT ROTATED IMAGE.
             elif self.direction == UP:
                 self.body[0] = self.piece2
                 image(self.body[i], self.x[i], self.y[i]) #GENERATING UPWARD-FACING IMAGE.
             elif self.direction == DOWN:
                 self.body[0] = self.piece2
                 image(self.body[i], self.x[i], self.y[i],30,30,30,30,0,0) #GENERATING DOWN-FACING IMAGE.
                 
             
         
     def display(self): # METHOD USED TO DISPLAY THE BODY OF THE SNAKE.
            self.update()
            for i in range(3,len(self.body)):
                if self.x[0] != self.x[i] and self.y[0] != self.y[i]:
                    self.display_1()
        
        
class Fruit_Element(Snake):  #FRUIT SUB CLASS FOR FRUIT ELEMENTS
    
    def __init__(self):
        Snake.__init__(self)
        self.Fruit = ["apple","banana"]
        self.randomizer = random.randint(0,1)
        self.cfruit = self.Fruit[self.randomizer] #USED TO RANDOMIZE FRUIT SELECTION
        self.fruit = loadImage(path + "/GameImages/" + str(self.cfruit) + ".png") #LOADS FRUIT IMAGES
        self.x1 = random.randrange(0,600,30)  #USED TO GENERATE RANDOM COORDINATES FOR THE FRUIT
        self.y1 = random.randrange(0,600,30)  #USED TO GENERATE RANDOM COORDINATES FOR THE FRUIT
        self.count = 0
        
    def display(self):
        for i in range(0, len(self.body)):
            if self.x1 == self.x[i] and self.y1 == self.y[i]:
                self.x1 = random.randrange(0,600,30)
                self.y1 = random.randrange(0,600,30)
                
        self.update()
        self.display_1()
        
        text("Your score : " + str(game.fruit.count),500,20) #UPDATES SCORE WITH EACH FRUIT CONSUMED
        image(self.fruit, self.x1, self.y1) #DISPLAYS FRUIT
        if self.x1 == self.x[0]  and self.y1 == self.y[0]:
            self.x.append(self.x[len(self.body)-1])
            self.count+=1
            self.y.append(self.y[len(self.body)-1])
            
            #if self.direction == LEFT or self.direction == RIGHT or self.direction == UP or self.direction == DOWN:
            if self.randomizer == 0:
                self.body.append(self.redd)
            elif self.randomizer == 1:
                self.body.append(self.yellow)
            self.randomizer = random.randint(0,1)
            self.cfruit = self.Fruit[self.randomizer] #USED TO RANDOMIZE FRUIT SELECTION
            self.fruit = loadImage(path + "/GameImages/" + str(self.cfruit) + ".png") #LOADS FRUIT IMAGES
            self.x1 = random.randrange(0,600,30) #USED TO GENERATE RANDOM COORDINATES FOR THE FRUIT
            self.y1 = random.randrange(0,600,30) #USED TO GENERATE RANDOM COORDINATES FOR THE FRUIT
            

        noFill()
        stroke(0,0,0)
        strokeWeight(5)
        rect(self.y1 * TILE_WIDTH, self.x1 * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)

class Game: #MAIN GAME CLASS
    
    def __init__(self):
        self.w = RESOLUTION
        self.h = RESOLUTION
        self.bound= BOUND
        self.snake = Snake()  #CREATES AN INSTANCE OF THE SNAKE ELEMENT CLASS
        self.fruit = Fruit_Element() #CREATES AN INSTANCE OF THE FRUIT ELEMENT CLASS
        self.completed = False
        
    def display(self):  
       if self.snake.alive == False: #CHECK IF END OF THE GAME HAS OCCURED
            text("Game Over", 270, 300) 
            text("Your score : " + str(game.fruit.count),260,400) #DISPLAYS FINAL SCORE
            return
       elif self.snake.Max_Length == (game.fruit.count+3): #CHECK IF END OF THE GAME HAS OCCURED
            text("Maximum snake length reached. Congratulations.", 270, 300) #DISPLAYS FINAL SCORE
            self.completed = True
            return
            
       self.snake.display() #CALLS SNAKE ELEMENT CLASS DISPLAY FUNCTION
       self.fruit.display() #CALLS FRUIT ELEMENT CLASS DISPLAY FUNCTION

        
        
game = Game() #CREATES AN INSTANCE OF THE GAME CLASS
       
def setup():
    size(RESOLUTION, RESOLUTION) 
    background(255,255,255)

def draw():
    if frameCount%10 == 0: #SLOWS DOWN SPEED OF THE GAME
        background(0,0,0) #SETS UP CANVAS OF THE GAME
        game.display()    

def keyPressed(): # UPDATES DIRECTIONS BASED ON KEY INPUTS.
    if keyCode == RIGHT:
        game.snake.dir = RIGHT
        game.fruit.dir = RIGHT
        
    if keyCode == LEFT:
        game.snake.dir = LEFT
        game.fruit.dir = LEFT
        
        
    if keyCode == UP:
        game.snake.dir = UP
        game.fruit.dir = UP
        
    if keyCode == DOWN:
        game.snake.dir = DOWN
        game.fruit.dir = DOWN
    
 
def mouseClicked(): #USED TO RESTART ENDED GAMES WITH MOUSECLICK.
    global game
    if game.snake.alive == False or game.completed == True:
        game = Game()    
