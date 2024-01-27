import pygame
from setting import TIME_OUT_HOLE


class UI:
    def __init__(self):
        self.score = 0
        self.x = 200
        self.y = 5
        self.width = 800
        self.height = 20
        self.cur_time = 100
        self.hit = 0
        self.miss = 0
        self.font = pygame.font.Font("assets/fonts/ScaryZombie-2OoMv.ttf", 36)
        
    def updateScore(self,score):
        self.score = score
    def draw(self,screen):
        self.cur_time-=0.2
        if self.cur_time <= 0: self.cur_time = 0
        screen.blit(self.font.render(f"Hit: {self.hit}",True,(255,255,255)),(0,30))
        screen.blit(self.font.render(f"Miss: {self.miss}",True,(255,0,0)),(0,90))
        # self.draw_timer_bar(screen)
    def draw_timer_bar(self,screen,time_out_hole):
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,self.width,self.height),2,10)
        pygame.draw.rect(screen,(255,0,0),(self.x+2,self.y+2,(self.width-4)*min(time_out_hole,TIME_OUT_HOLE)/TIME_OUT_HOLE,self.height-4),0,10)
    def increase_hit(self):
        self.hit+=1
    def increase_miss(self):
        self.miss+=1
        