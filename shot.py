import pygame


class Shot:
    def __init__(self, coordinates, facing):
        self.shot_x = coordinates[0]
        self.shot_y = coordinates[1]
        self.radius = 4
        self.color = (255, 0, 155)
        self.facing = facing
        self.vel = 1 * facing

    def draw(self, win):
        pygame.display.update(pygame.draw.circle(win, self.color, (self.shot_x, self.shot_y), self.radius))

    def movement(self, shots):
        if 450 > self.shot_x > 1:
            self.shot_x += self.vel
        else:
            shots.remove(self)
