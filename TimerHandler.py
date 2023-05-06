import pygame

class TimerHandler:
    def __init__(self, X_cordinate, Y_cordinate, screen):
        self. X_cordinate = X_cordinate
        self.Y_cordinate = Y_cordinate
        self.screen = screen

    def drawTime(self, time):
        self.screen.blit(self.playerPhoto,(self.X_cordinate, self.Y_cordinate))
