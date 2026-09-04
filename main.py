import snake
import pygame # type: ignore

pygame.init()  # pygameを初期化
screen = pygame.display.set_mode((snake.WINDOW_WIDTH, snake.WINDOW_HEIGHT ))  # ウィンドウサイズ指定
pygame.display.set_caption("Snake Game")  # タイトル

square_num = 10
square_size = snake.WINDOW_WIDTH//square_num
crossedPoint = []

def drawGrid():
    for i in range(square_num):
        pygame.draw.line(screen, (255,255,255), (0,i*square_size), (snake.WINDOW_WIDTH,i*square_size), 3)
        pygame.draw.line(screen, (255,255,255), (i*square_size,0), (i*square_size,snake.WINDOW_HEIGHT), 3)

for i in range(square_num):
        for j in range(square_num):
            crossedPoint.append([i*square_size,j*square_size])

object = snake.Snake()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ウィンドウの×ボタンで終了
            running = False
    object.handleKeys()
    if(object.position in crossedPoint):
            object.direction = object.nextDirection
    object.move()
    screen.fill((0, 0, 128))
    drawGrid()
    if(object.position[0]+square_size > snake.WINDOW_WIDTH or
                object.position[1]+square_size > snake.WINDOW_HEIGHT or 
                object.position[0] < 0 or 
                object.position[1] < 0):
        object.direction = snake.death
        font = pygame.font.Font(None, 55)
        gameover = True
        while gameover:
            screen.fill((0, 0, 0)) 
            text = font.render("Game Over", True, (255, 255, 255))
            text_rect = text.get_rect(center=(snake.WINDOW_WIDTH//2, snake.WINDOW_HEIGHT//2))
            screen.blit(text, text_rect)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # ウィンドウの×ボタンで終了
                        gameover = False
                        running = False
            pygame.display.flip()  # 画面更新
            clock.tick(60) # FPS
    pygame.draw.rect(screen, (255,255,255), (object.position[0],object.position[1],square_size,square_size)) #(positionX,positionY,width,height)
    pygame.display.flip()  # 画面更新
    clock.tick(60) # FPS

pygame.quit()
