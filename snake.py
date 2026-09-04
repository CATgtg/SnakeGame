import pygame #type: ignore

class Snake:
    def __init__(self):
        self.position = [(WINDOW_WIDTH/2),(WINDOW_HEIGHT/2)] #[横,縦]
        self.legth = 1
        self.direction = right
        
        self.nextDirection = right
        self.nextPosition = []

    def currentPosition(self):
        return self.position

    def handleKeys(self):
        keys = pygame.key.get_pressed()
        if(self.direction != up and self.direction != down):
            if(keys[pygame.K_UP] or keys[pygame.K_w]):
                self.nextDirection = up
            if(keys[pygame.K_DOWN] or keys[pygame.K_s]):
                self.nextDirection = down
        if(self.direction != right and self.direction != left):
            if(keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                self.nextDirection = right
            if(keys[pygame.K_LEFT] or keys[pygame.K_a]):
                self.nextDirection = left

    def move(self):
        self.position =  [x+y for x,y in zip(self.position,self.direction)]

WINDOW_HEIGHT = 480
WINDOW_WIDTH  = 480

up =    (0,-4)
down =  (0,4)
right = (4,0)
left =  (-4,0)
death = (0,0)