import pygame
import random
from setting import TIME_IN_HOLE,TIME_OUT_HOLE,TIME_STEP,FRAME,STUNNED_FRAME,STUNNED_TIME_STEP

# hole_positions = [(90,40),(420,40),(250,170),(250,450),(80,310),(420,305)]
hole_positions = [(235,500),(325,365),(490,425),(645,505),(790,430),(1020,390)]
# (235,500)
# (325,365)
# (490,425)
# (645,505)
# (790,430)

hole = random.choice(hole_positions)

class Zombie:
    def __init__(self):
        # zombie_sprite_sheet = pygame.image.load("assets/animation/mole.png")
        zombie_sprite_sheet = pygame.image.load("assets/animation/zombie.png")
        zombie_sprite_sheet_2 = pygame.image.load("assets/animation/zombie2.png")
        zombie_sprite_sheet_3 = pygame.image.load("assets/animation/zombie3.png")
        zombie_sprite_sheet_4 = pygame.image.load("assets/animation/zombie4.png")
        stunned_sprite_sheet = pygame.image.load("assets/animation/stunned.png")
        self.zombie = []
        self.stunned = []
        self.zombie_type = 0

        self.zombie.append([zombie_sprite_sheet.subsurface(853, 0, 10, 10)
                            ,zombie_sprite_sheet.subsurface(310, 0, 120, 120)
                            ,zombie_sprite_sheet.subsurface(455, 0, 120, 120)
                            ,zombie_sprite_sheet.subsurface(580, 0, 120, 120)
                            ,zombie_sprite_sheet.subsurface(722, 0, 120, 120)
                            ,zombie_sprite_sheet.subsurface(853, 0, 120, 120)])
        self.zombie.append([zombie_sprite_sheet_2.subsurface(853, 0, 10, 10)
                            ,zombie_sprite_sheet_2.subsurface(310, 0, 120, 120)
                            ,zombie_sprite_sheet_2.subsurface(455, 0, 120, 120)
                            ,zombie_sprite_sheet_2.subsurface(580, 0, 120, 120)
                            ,zombie_sprite_sheet_2.subsurface(722, 0, 120, 120)
                            ,zombie_sprite_sheet_2.subsurface(853, 0, 120, 120)])
        self.zombie.append([zombie_sprite_sheet_3.subsurface(878, 0, 10, 10)
                            ,zombie_sprite_sheet_3.subsurface(335, 0, 120, 120)
                            ,zombie_sprite_sheet_3.subsurface(480, 0, 120, 120)
                            ,zombie_sprite_sheet_3.subsurface(605, 0, 120, 120)
                            ,zombie_sprite_sheet_3.subsurface(747, 0, 120, 120)
                            ,zombie_sprite_sheet_3.subsurface(878, 0, 120, 120)])
        self.zombie.append([zombie_sprite_sheet_4.subsurface(853, 0, 10, 10)
                            ,zombie_sprite_sheet_4.subsurface(310, 0, 120, 120)
                            ,zombie_sprite_sheet_4.subsurface(455, 0, 120, 120)
                            ,zombie_sprite_sheet_4.subsurface(580, 0, 120, 120)
                            ,zombie_sprite_sheet_4.subsurface(722, 0, 120, 120)
                            ,zombie_sprite_sheet_4.subsurface(853, 0, 120, 120)])

        self.stunned.append(pygame.transform.scale(stunned_sprite_sheet.subsurface(0, 0, 100, 58),(100,58)))
        self.stunned.append(pygame.transform.scale(stunned_sprite_sheet.subsurface(100, 0, 100, 58),(100,58)))
        self.stunned.append(pygame.transform.scale(stunned_sprite_sheet.subsurface(200, 0, 100, 58),(100,58)))
        self.stunned.append(pygame.transform.scale(stunned_sprite_sheet.subsurface(300, 0, 100, 58),(100,58)))

        self.frame = 0
        self.stunned_frame = 0
        self.stunned_timeStep = STUNNED_TIME_STEP
        self.timeStep = TIME_STEP
        self.x = hole[0]
        self.y = hole[1]
        self.take_hit = False
        self.return_to_hole = False
        self.time_in_hole = TIME_IN_HOLE
        self.time_out_hole = TIME_OUT_HOLE
    def draw(self,screen):
        if not (self.return_to_hole and self.frame == 0): screen.blit(self.zombie[self.zombie_type][self.frame],(self.x,self.y))
        self.timeStep-=1
        if self.timeStep < 0:
            self.timeStep = 0
        if self.return_to_hole:
            if self.timeStep == 0:
                self.timeStep = TIME_STEP
                if self.frame > 0: self.frame -=1
        else:
            if self.timeStep == 0:
                self.timeStep = TIME_STEP
                if self.frame < 2: self.frame +=1
                elif self.frame < 3 and self.take_hit: self.frame += 1
        if self.return_to_hole == False:
            self.time_out_hole-=1
            if self.time_out_hole < 0:
                self.time_out_hole = 0
            if self.time_out_hole == 0:
                self.time_in_hole = TIME_IN_HOLE
                if self.frame > 2 and self.frame < 3:
                    self.stunnedAnimation()
                    pass
                else:
                    self.returnToHole()
                    pass
        else:
            self.time_in_hole-=1
            if self.time_in_hole < 0:
                self.time_in_hole = 0
            if self.time_in_hole == 0:
                self.time_out_hole = TIME_OUT_HOLE
                self.growFromHole()
        self.stunnedAnimation(screen)
    def takeHit(self):
        if self.take_hit or self.return_to_hole:
            return
        if not self.take_hit:
            self.time_out_hole+=100
        self.take_hit = True
        self.frame = 3
    def checkCursorHit(self,cursor_x,cursor_y):
        if self.x < cursor_x and (self.x + self.zombie[self.zombie_type][self.frame].get_width()) > cursor_x and self.y < cursor_y and (self.y + self.zombie[self.zombie_type][self.frame].get_height()) > cursor_y:
            return True
        return False
    def returnToHole(self):
        self.frame = 2
        self.return_to_hole = True
    def growFromHole(self):
        self.zombie_type = random.randint(0,3)
        self.frame = 0
        self.return_to_hole = False
        self.take_hit = False
        hole = random.choice(hole_positions)
        self.x = hole[0]
        self.y = hole[1]
    def stunnedAnimation(self,screen):
        if self.take_hit and not self.return_to_hole:
            self.stunned_timeStep-=1
            if self.stunned_timeStep <= 0:
                self.stunned_timeStep = STUNNED_TIME_STEP
                self.stunned_frame = (self.stunned_frame+1)%STUNNED_FRAME
            screen.blit(self.stunned[self.stunned_frame],(self.x,self.y-10))



