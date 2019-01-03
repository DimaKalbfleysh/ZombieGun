import pygame


class Shot:
    def __init__(self, coordinates, facing):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.radius = 4
        self.color = (255, 50, 155)
        self.facing = facing
        self.vel = 1 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self, shots):
        if 450 > self.x > 1:
            self.x += self.vel
        else:
            shots.remove(self)
