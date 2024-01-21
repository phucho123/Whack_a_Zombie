import pygame
from Zombie import Zombie
from UI import UI
from Sound import Sound

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("assets/images/background.png")
bg = pygame.transform.scale(bg,(600,600))
zombie = Zombie()
ui = UI()
sound = Sound()
sound.playBGMusic()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
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

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()