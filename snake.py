import pygame #type: ignore

WINDOW_HEIGHT = 480
WINDOW_WIDTH  = 480

up =    (0,-4)
down =  (0,4)
right = (4,0)
left =  (-4,0)
death = (0,0)

class Snake:    
    def __init__(self, x=None, y=None):
        self.length = 3
        self.direction = right
        
        self.nextDirection = right
        self.nextPosition = []
        if x is None and y is None:
            self.position = [(WINDOW_WIDTH/2),(WINDOW_HEIGHT/2)] #[横,縦]
            # self.legth = 1
            # self.direction = right
            
            # self.nextDirection = right
            # self.nextPosition = []
        else: #sub用コンストラクタって感じ
            self.position = [x,y]

    def currentPositionX(self): #現在位置
        return self.position[0]
    def currentPositionY(self):
        return self.position[1]

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
    
    def RESET(self): #R押下時に蛇の状態初期化
        self.position = [(WINDOW_WIDTH/2),(WINDOW_HEIGHT/2)]