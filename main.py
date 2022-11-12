from pygame import*
from random import randint

mixer.init()
font.init()

WIDTH = 1200
HEIGHT = 690
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("runner")
clock = time.Clock()

groundlvl = 660


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
        self.jump_speed = 23
        self.speed = 12
        self.onground = True
        self.wh = 4
        self.gravity = 0.2
        self.jumpcount = 0

    def jump (self):
        if self.rect.y > 270:
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
        if self.wh <= 0:
            player.rect.y = 570
            self.wh == 4
        if not self.onground:
            #self.gravity += 0.2
            #self.speed_y += 0.2
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
        self.rect.bottom = groundlvl
       
  
    def update(self):
        global points,count_text
        self.rect.x -= bg_speed
        if self.rect.x <= -100:
            self.kill()
            points += 1
            count_text = font1.render(str(points),True,(0,255,0))
        
      

fon1_x = 0
fon2_x = WIDTH



bg_speed = 7
fon = transform.scale(image.load('fon.png'), (WIDTH, HEIGHT))
fon2 = transform.scale(image.load('fon.png'), (WIDTH, HEIGHT))
run = True
game = True
FPS = 60
player = Player()
points = 0
kakts = sprite.Group()

font1 = font.SysFont("Impact",70)
font2 = font.SysFont("Impact",50)
font3 = font.SysFont("Impact",33)
result = font2.render('Ти програв',True,(0,255,0))
count_text = font1.render('0',True,(0,255,0))
chance = font3.render('Щоб грати дальше ,нажміть "2",але майте на увазі,всі очки обнуляться',True,(0,255,0))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            player.jump()

    if fon1_x < - WIDTH:
        fon1_x = WIDTH

    if fon2_x < - WIDTH:
        fon2_x = WIDTH
    rand_num = randint(0,100)
    if rand_num == 70:
        kakts.add(Kakt())
    collide = sprite.spritecollideany(player,kakts)
    if collide:
        game = False
    if game:
        fon1_x -= bg_speed
        fon2_x -= bg_speed
        window.blit (fon, (fon1_x,0))
        window.blit (fon2, (fon2_x,0))
        player.update()
        player.draw()
        kakts.update()
        kakts.draw(window)
    else:
        window.blit(result, (470,150))
        window.blit(chance,(90,220))
        keys = key.get_pressed()
        if keys [K_2]:
            game = True
            points = 0
        count_text = font1.render(str(points),True,(0,255,0))
    window.blit(count_text,(30,30))




    display.update()
    clock.tick(FPS)
