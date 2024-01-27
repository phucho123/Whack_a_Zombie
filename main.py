import pygame
from Zombie import Zombie
from UI import UI
from Sound import Sound

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 670))
pygame.display.set_caption("Whack A Zombie")
clock = pygame.time.Clock()
running = True
game_state = "start"


bg = pygame.image.load("assets/images/background_1.png")
bg_start = pygame.transform.scale(pygame.image.load("assets/images/bg_start.jpg"),(1200,670))
my_font = pygame.font.Font('assets/fonts/ScaryZombie-2OoMv.ttf',64)
my_font_2 = pygame.font.Font('assets/fonts/ScaryZombie-2OoMv.ttf',40)
start_game = my_font_2.render("Start Game",True,(255,255,255))
start_game_hover = my_font_2.render("Start Game",True,(255,0,0))
game_name = my_font.render("Whack A Zombie",True,(255,0,0))
game_over = my_font.render("Game Over",True,(255,0,0))
play_again = my_font_2.render("Play Again",True,(0,255,0))
# bg = pygame.transform.scale(bg,(600,600))
hammer = pygame.image.load("assets/animation/hammer.png")
zombie = Zombie()
ui = UI()
sound = Sound()
sound.playStart()


hammer_frame = 0
hammer_frame_timStep = 0
def drawHammer(screen,mx,my):
    global hammer_frame_timStep, hammer_frame
    if hammer_frame_timStep > 0:
        hammer_frame_timStep -= 1
    else:
        hammer_frame = 0
    screen.blit(hammer,(mx-20,my-20),(hammer_frame*120,0,120,120))


def drawStartScreen(screen):
    screen.blit(bg_start,(0,0))
    if checkMouseInButton(600-start_game.get_width()/2,250,start_game):
        screen.blit(start_game_hover,(600-start_game.get_width()/2,250))
    else:
        screen.blit(start_game,(600-start_game.get_width()/2,250))
    screen.blit(game_name,(600-game_name.get_width()/2,100))

def drawGameOver(screen):
    screen.blit(bg_start,(0,0))
    screen.blit(game_over,(600-game_over.get_width()/2,150))
    if checkMouseInButton(600-play_again.get_width()/2,250,play_again):
        play_again.set_alpha(100)
    else:
        play_again.set_alpha(255)
    screen.blit(play_again,(600-play_again.get_width()/2,250))

def checkMouseInButton(x,y,button):
    mx,my = pygame.mouse.get_pos()
    if mx > x and mx < x+button.get_width() and my > y and my < y+button.get_height():
        return True
    return False

def start_to_run():
    global game_state
    game_state = "run"
    pygame.mouse.set_visible(False)
    sound.start.stop()
    sound.playBGMusic()

    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "run":
                mouse_x, mouse_y = pygame.mouse.get_pos()
                hammer_frame = 1
                hammer_frame_timStep = 10
                if (not zombie.return_to_hole) and zombie.checkCursorHit(mouse_x,mouse_y):
                    if not zombie.take_hit:
                        ui.increase_hit()
                        sound.playHit()
                        sound.playStunned()
                    zombie.takeHit()
                else:
                    ui.increase_miss()
                    sound.playMiss()
            elif game_state == "start":
                mx, my = pygame.mouse.get_pos()
                if checkMouseInButton(600-start_game.get_width()/2,250,start_game):
                    start_to_run()
            elif game_state == "over":
                if checkMouseInButton(600-play_again.get_width()/2,250,play_again):
                    game_state = "run"
                    pygame.mouse.set_visible(False)
                    ui.miss = 0
                    ui.hit = 0
                    sound.start.stop()
                    sound.playBGMusic()

    if game_state == "start":
        drawStartScreen(screen)

    elif game_state == "run":
        screen.blit(bg,(0,0))
        zombie.draw(screen)
        ui.draw(screen)
        if zombie.time_out_hole:
            ui.draw_timer_bar(screen,zombie.time_out_hole)
        mx,my = pygame.mouse.get_pos()
        drawHammer(screen,mx,my)
        if ui.miss == 10:
            game_state = "over"
            sound.background_music.stop()
            sound.stunned.stop()
            sound.playStart()
            pygame.mouse.set_visible(True)
    elif game_state == "over":
        drawGameOver(screen)
        ui.draw(screen)
    
    pygame.display.flip()
    clock.tick(60) 

pygame.quit()