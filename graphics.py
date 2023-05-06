import time
import pygame
import random
from squareObject import SquareObject
from player import Player
from Emotion import Emotion


class Graphics:
    right_side = 900 #הX של הצד הימני של הלוח
    left_side = 600#הX של הצד השמאלי של הלוח
    starter_y_for_objects = 30#הגובה ההתחלתי של המכשולים
    y_for_player = 700#הגובה של השחקן
    time_to_add_object = 3#כל כמה זמן להוסיף מכשול
    time_to_change_speed = 5#כל כמה זמן להגביר מהירות
    increase_speed_by = 0.75  #בכמה להגביר את המהירות - מכפילים את זמן השהייה בין תזוזה לתזוזה
    start_speed = 0.05#מהירות התחלתית

    WHITE = (255, 255, 255)

    def __init__(self, emotion):
        #מאתחל את הלוח
        pygame.init()
        # Set up the drawing window
        pygame.display.set_caption("test")
        # Initializing surface
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Fill the background with white
        self.screen.fill((255, 255, 255))

        self.emotion = emotion

        self.clock = pygame.time.Clock()

        # create the player
        #X_average = (self.left_side + self.right_side) / 2  # לנקודת ההתחלה של השחקן
        self.player = Player(self.left_side, self.right_side, self.y_for_player, self.screen)
        self.player.first_draw()

    def playerManager(self, emotiom):
        X_average = (self.left_side + self.right_side) / 2#לנקודת ההתחלה של השחקן
        player = Player(X_average, self.y_for_player, self.screen)
        player.first_draw()
        if emotiom == "happy":
            player.moveRight()
        elif emotiom == "sad":
            player.moveleft()


    def objectsManeger(self):
        startingTime = time.time()
        speed = self.start_speed
        speed_time = time.time()
        add_object_time = time.time()
        all_objects = []

        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            if (time.time() - add_object_time >= self.time_to_add_object):
                add_object_time = time.time()
                which_side_rand = random.randint(1,2)
                if which_side_rand == 1: #1 מסמל את צד שמאל
                    all_objects.append(SquareObject(self.left_side, self.starter_y_for_objects, self.screen))

                if which_side_rand == 2: #2 מסמל את צד ימין
                    all_objects.append(SquareObject(self.right_side, self.starter_y_for_objects, self.screen))

            for singleObject in all_objects:
                singleObject.moveDown()
            #time.sleep(speed)

            if(time.time() - speed_time >= self.time_to_change_speed):
                speed_time = time.time()
                speed *= self.increase_speed_by

            if (self.emotion.getEmotion() == Emotion.HAPPY):
                self.player.moveleft()
                print("happy...")
            else:
                self.player.moveRight()
                print("sad...")

            pygame.display.update()
            self.clock.tick(60)

            self.screen.fill(self.WHITE)





#if _name_ == "_main_":
 #   c = Graphics(900,600,30,700,3,5,0.75,0.1)
  #  c.objectsManeger()
  #  c.playerManege("happy")