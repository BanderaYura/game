from pygame import*

mixer.init

WIDTH = 1500
HEIGHT = 800
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("runner")
clock = time.Clock()

class GameSpirite ():
    def __init__(self,image_name,x,y,width, height):
        super().__init__()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    
class Player(GameSpirite):
    def __init__(self):
        super().__init__("player.png",200,200,75,75)
        self.speed = 5
fon = transform.scale(image.load('fon.png'), (WIDTH, HEIGHT))

run = True
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit (fon, (0,0))
    display.update()
    clock.tick(FPS)