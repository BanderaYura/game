from pygame import*

mixer.init

WIDTH = 1500
HEIGHT = 800
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("runner")
clock = time.Clock()

class GameSpirite (sprite.Sprite):
    def __init__(self,image_name,x,y,width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        window.blit(self.image,self.rect)

class Player(GameSpirite):
    def __init__(self):
        super().__init__("player.png",70,660,75,75)
        self.speed_y = 0
        self.jump_speed = 50
        self.speed = 15
        self.onground = False

    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < WIDTH - self.width:
            self.rect.x += self.speed
        if keys [K_SPACE] and self.rect.x > WIDTH - self.width:
            self.rect.y -= self.jump_speed
        #if self.speed.rect.x < 0

        self.rect.y += self.speed_y

fon = transform.scale(image.load('fon.png'), (WIDTH, HEIGHT))
run = True
FPS = 60
player = Player()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        window.blit (fon, (0,0))
        player.update()
        player.draw()
        display.update()
        clock.tick(FPS)