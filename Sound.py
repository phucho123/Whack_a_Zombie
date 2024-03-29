import pygame

class Sound:
    def __init__(self):
        self.background_music = pygame.mixer.Sound("assets/sound/background/Driftveil City.mp3")
        self.miss = pygame.mixer.Sound("assets/sound/effects/miss.mp3")
        self.hit = pygame.mixer.Sound("assets/sound/effects/hit.mp3")
        self.stunned = pygame.mixer.Sound("assets/sound/effects/stunned.mp3")
        self.start = pygame.mixer.Sound("assets/sound/background/start_sound.mp3")
    def playBGMusic(self):
        self.background_music.play(-1)
    def playHit(self):
        self.hit.play()
    def playMiss(self):
        self.miss.play()
    def playStunned(self):
        self.stunned.play()
    def playStart(self):
        self.start.play(-1)
        self.start.play()