##############################
#    OOP Formative Shooter   #
#      Peyton Germann        #
#      Nov, 30, 2022         #
##############################
import pygame, random, time
from pygame.locals import *
size = (700, 700)
lasers = []
enemies = []
def redraw():
    screen.fill((0, 0, 0))
    for laser in lasers:
        laser.draw()
    ship.draw()
    for enemy in enemies:
        enemy.draw()

class ship(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.speed = speed
    def draw():
        screen.blit(spaceship, (ship_.x, ship_.y))
        pygame.display.update()
        total = 10
        while total > 0:
            stars()
            total = total - 1
class laser(object):
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.speed = speed
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
    
    def move(self):
        self.y -= self.speed
class Enemy(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.speed = speed
    
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(self.x, self.y, self.w, self.h))
    
    def move(self):
        self.y += self.speed
    
    def check_y(self):
        y = 0
        self.y = y
        return y

def randomnum():
    numx = random.randint(1, 699)
    numy = random.randint(1, 699)
    return numx, numy

def randomsize():
    size = random.randint(1, 15)
    return size

def stars():
    x, y = randomnum()
    size_ = randomsize()
    pygame.draw.circle(screen, (255, 255, 255),(x, y), size_)
    pygame.display.update()


def time(n):
    from time import sleep
    sleep(n)
    
spaceship = pygame.image.load('ship.png')
ship_ = ship(300, 600, 80, 80, 4)
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SHOOTER FUN :)")
COOLDOWN_DURATION = 100
last_fired = pygame.time.get_ticks()
last_enemy_spawn_time = 0
while running:
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Iterate through the enemies list in reverse
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_spawn_time >= 5000:
        enemy_x, enemy_y= randomnum()
        enemy_y = 0
        enemy_size = randomsize()
        enemy = Enemy(enemy_x, enemy_y, enemy_size, enemy_size, 2)
        enemies.append(enemy)
        last_enemy_spawn_time = current_time
    if keys[pygame.K_SPACE]:
        if pygame.time.get_ticks() > last_fired + COOLDOWN_DURATION:
            laser_ = laser(ship_.x + 35, ship_.y - 20, 5, 20, 8, (255, 0, 0))
            lasers.append(laser_)
            last_fired = pygame.time.get_ticks()
    if keys[pygame.K_d] and ship_.x < 700 - ship_.w - ship_.speed:
        ship_.x += ship_.speed
    if keys[pygame.K_a] and ship_.x > ship_.speed:
        ship_.x -= ship_.speed
    if keys[pygame.K_w] and ship_.y > ship_.speed:
        ship_.y -= ship_.speed
    if keys[pygame.K_s] and ship_.y < 700 - ship_.h - ship_.speed:
        ship_.y += ship_.speed
    if keys[pygame.K_RIGHT] and ship_.x < 700 - ship_.w - ship_.speed:
        ship_.x += ship_.speed
    if keys[pygame.K_LEFT] and ship_.x > ship_.speed:
        ship_.x -= ship_.speed
    if keys[pygame.K_UP] and ship_.y > ship_.speed:
        ship_.y -= ship_.speed
    if keys[pygame.K_DOWN] and ship_.y < 700 - ship_.h - ship_.speed:
        ship_.y += ship_.speed
    for laser_ in lasers:
        laser_.move()
    for enemy in enemies:
        enemy.move()
        enemy.check_y()
    redraw()
pygame.display.quit()