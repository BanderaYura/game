from pygame import*
from random import randint

mixer.init

WIDTH = 1200
HEIGHT = 690
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("runner")
clock = time.Clock()
groundlvl = 630

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
        super().__init__("player.png",500,groundlvl - 75,75,75)
        self.speed_y = 10
        self.jump_speed = 30
        self.speed = 15
        self.onground = True
        self.wh = 5
        self.gravity = 1
        self.jumpcount = 0

    def jump (self):
        self.rect.y -= self.jump_speed
        self.onground = False
        self.gravity = 0
        self.speed_y = 5
        
 
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < WIDTH - self.width:
            self.rect.x += self.speed
        if keys [K_SPACE]:
            self.jump()
        #if keys [K_UP]:
            #self.rect.y -= self.jump_speed
        #if keys [K_DOWN]:
            #self.rect.y += self.jump_speed
        if self.wh == 0:
            player.rect.y = 570
        if not self.onground:
            self.gravity += 1
            self.rect.y += self.speed_y + self.gravity
        if self.rect.y >= 570:
            self.onground = True
            self.gravity = 0
            self.speed_y = 0
        if self.onground == False:
            start_num = 7
            start_num - 1
            if start_num == 0:
                print('jfiwjf ')

class Kakt (GameSpirite):
    def __init__(self):
        rand_h = randint(75,150)
        rand_x = randint(0,WIDTH)
        super().__init__("kakt.png",WIDTH+rand_x,groundlvl - rand_h , int(rand_h / 2) ,rand_h)
       
      
    def update(self):
        self.rect.x -= bg_speed
        if self.rect.x <= -100:
            self.kill()
      

fon1_x = 0
fon2_x = WIDTH



bg_speed = 7
fon = transform.scale(image.load('fon.png'), (WIDTH, HEIGHT))
fon2 = transform.scale(image.load('fon.png'), (WIDTH, HEIGHT))
run = True
FPS = 60
player = Player()
kakts = sprite.Group()


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if fon1_x < - WIDTH:
        fon1_x = WIDTH

    if fon2_x < - WIDTH:
        fon2_x = WIDTH
    rand_num = randint(0,100)
    if rand_num == 70:
        kakts.add(Kakt())

    fon1_x -= bg_speed
    fon2_x -= bg_speed
    window.blit (fon, (fon1_x,0))
    window.blit (fon2, (fon2_x,0))
    player.update()
    player.draw()
    kakts.update()
    kakts.draw(window)
    display.update()
    clock.tick(FPS)
