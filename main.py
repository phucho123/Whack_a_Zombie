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
bg = pygame.image.load("assets/images/background_1.png")
# bg = pygame.transform.scale(bg,(600,600))
hammer = pygame.image.load("assets/animation/hammer.png")
zombie = Zombie()
ui = UI()
sound = Sound()
sound.playBGMusic()
pygame.mouse.set_visible(False)

hammer_frame = 0
hammer_frame_timStep = 0


def drawHammer(screen,mx,my):
    global hammer_frame_timStep, hammer_frame
    if hammer_frame_timStep > 0:
        hammer_frame_timStep -= 1
    else:
        hammer_frame = 0
    screen.blit(hammer,(mx-20,my-20),(hammer_frame*120,0,120,120))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
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
    screen.blit(bg,(0,0))
    zombie.draw(screen)
    ui.draw(screen)
    if zombie.time_out_hole:
        ui.draw_timer_bar(screen,zombie.time_out_hole)

    mx,my = pygame.mouse.get_pos()
    drawHammer(screen,mx,my)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()