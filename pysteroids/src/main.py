import pygame
import random
from enum import Enum
from player import Player
from bullet import Bullet
from asteroid import Asteroid

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
score = 0

#Sprite groups
asteroid_sprite_group = pygame.sprite.Group()
bullet_sprite_group = pygame.sprite.Group()
player_sprite_group = pygame.sprite.Group()

class GameState(Enum):
    MENU = 1
    MAIN = 2
    SCORE = 3

state = GameState.MENU
player = Player()
player_sprite_group.add(player)
bullets = [] # Array of bullets on screen
asteroids = [] # Array that stores all asteroids on screen
asteroid_count = 0

def main_menu(keys):
    global score
    global bullets
    global asteroids
    global asteroid_count
    score = 0 # Reset
    bullets = []
    asteroids = []
    asteroid_count = 0

    asteroid_sprite_group.empty()
    bullet_sprite_group.empty()

    # RESET PLAYER POS
    player.x = pygame.display.get_window_size()[0] / 2
    player.y = pygame.display.get_window_size()[1] / 2
    player.vel_x = 0
    player.vel_y = 0

    title_font = pygame.font.SysFont(None, 64)
    title = title_font.render("Pysteroids", False, (255,255,255))
    title_pos = (pygame.display.get_window_size()[0] / 2 - 110, pygame.display.get_window_size()[1] / 2 - 50 )
    menu_text = pygame.font.SysFont(None, 32)
    screen.blit(title, title_pos)
    screen.blit(menu_text.render("Pressione Espaço para Iniciar", False, "yellow"), (title_pos[0] - 55, title_pos[1] + 100))
    screen.blit(menu_text.render("Você consegue fazer 1000 pontos? >:)", False, "red"), (title_pos[0] - 95, title_pos[1] + 150))
    screen.blit(menu_text.render("Espaço - Para atirar || Setinhas - Para se mover", False, "white"), (380, pygame.display.get_window_size()[1] - 30))

    # Start game
    if keys[pygame.K_SPACE]:
        global state
        state = GameState.MAIN

def main_game(keys):

    #Score code with increasing difficulty
    global score
    global state
    global asteroid_count

    if score < 200:
        min_asteroids = 5
    elif score < 500:
        min_asteroids = 10
    elif score < 1000:
        min_asteroids = 15
    else:
        min_asteroids = 20

    score_font = pygame.font.SysFont(None, 32)
    screen.blit(score_font.render(f"Pontuação: {score}", False, "white"), (10, 10))

    #Player code
    player.draw(screen)

    if keys[pygame.K_LEFT]:
        player.move_left()
    elif keys[pygame.K_RIGHT]:
        player.move_right()
    
    player.move_foward(keys)
    player.warp()

    for b in bullets:
            b.draw(screen)
            b.move()

    # Asteroid section
    if asteroid_count < min_asteroids:
        size = random.choice([1,2,3])
        new_asteroid = Asteroid(size, random.randint(0, 1280), random.randint(0, 720))
        asteroid_sprite_group.add(new_asteroid)
        asteroids.append(new_asteroid)
        asteroid_count += 1
    
    for asteroid in asteroids:
        asteroid.move()
        asteroid.draw(screen)
        asteroid.warp()

    collisions = pygame.sprite.groupcollide(asteroid_sprite_group, bullet_sprite_group, True, True)
    for asteroid in collisions:
        match asteroid.size:
            case 3:
                score += 5
            case 2:
                score += 10
            case 1:
                score += 25
        if asteroid.size >= 2:
            new_size = asteroid.size - 1
            new_asteroid_1 = Asteroid(new_size, asteroid.x, asteroid.y)
            new_asteroid_2 = Asteroid(new_size, asteroid.x, asteroid.y)
            asteroid_sprite_group.add(new_asteroid_1)
            asteroid_sprite_group.add(new_asteroid_2)
            asteroids.append(new_asteroid_1)
            asteroids.append(new_asteroid_2)
            asteroid_count += 2
        asteroids.remove(asteroid)
        asteroid_count -= 1
        for bullet in collisions[asteroid]:
            bullets.remove(bullet)
    
    # GAMEOVER
    death = pygame.sprite.groupcollide(player_sprite_group, asteroid_sprite_group, False, True)
    if death:
        state = GameState.SCORE

def score_screen(keys):
    global score
    global state
    title_font = pygame.font.SysFont(None, 64)
    if score >= 1000:
        title = title_font.render("Uaaaaaaau :0", False, "green")
    else:
        title = title_font.render("Game Over :(", False, "white")
    title_pos = (pygame.display.get_window_size()[0] / 2 - 110, pygame.display.get_window_size()[1] / 2 - 50 )
    menu_text = pygame.font.SysFont(None, 32)
    screen.blit(title, title_pos)
    screen.blit(menu_text.render(f"Pontuação: {score}", False, "white"), (title_pos[0] - 50, title_pos[1] + 150))
    screen.blit(menu_text.render("Pressione ESC para retornar ao menu", False, "white"), (450, pygame.display.get_window_size()[1] - 30))
    if keys[pygame.K_ESCAPE]:
        state = GameState.MENU

while running:
    keys = pygame.key.get_pressed()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                bullet = Bullet(player.head, player.seno, player.cosseno, screen)
                bullet_sprite_group.add(bullet)
                bullets.append(bullet)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    match state:
        case state.MENU:
            main_menu(keys)
        case state.MAIN:
            main_game(keys)
        case state.SCORE:
            score_screen(keys)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
