import os.path    #імпорти
import pygame
set_win = {
    "WIDTH" : 700,
    "HEIGHT" : 700,     #данні вікна
    "FPS" : 60,
    "WIN_TITLE" : "CsGo2.0"
}

bots_list = list()     #cписок ботів


abs_path = os.path.abspath(__file__ + "/..") + "\\image\\"     #aбсолютний путь до моделей


#загрузка моделей
ninja_stay_image = pygame.transform.scale(pygame.image.load(abs_path + "ninja_stay.png"), (40, 80))
bg_image = pygame.image.load(abs_path + "background.png")
ninja_run1_image = pygame.transform.scale(pygame.image.load(abs_path + "ninja_run1.png"), (40, 80))
ninja_run2_image = pygame.transform.scale(pygame.image.load(abs_path + "ninja_run2.png"), (40, 80))
ninja_shot_image = pygame.transform.scale(pygame.image.load(abs_path + "ninja_shot.png"), (40, 80))
ninja_run_withgun1_image = pygame.transform.scale(pygame.image.load(abs_path + "ninja_run_withgun1.png"), (50, 80))
ninja_run_withgun2_image = pygame.transform.scale(pygame.image.load(abs_path + "ninja_run_withgun2.png"), (50, 80))
ninja_stay_withgun_image = pygame.transform.scale(pygame.image.load(abs_path + "ninja_stay_withgun.png"), (50, 80))
zombie_run1_image = pygame.transform.scale(pygame.image.load(abs_path + "zombie_run1.png"), (40, 80))
zombie_run2_image = pygame.transform.scale(pygame.image.load(abs_path + "zombie_run2.png"), (40, 80))
zombie_stay_image = pygame.transform.scale(pygame.image.load(abs_path + "zombie_stay.png"), (40, 80))
bullet_image = pygame.transform.scale(pygame.image.load(abs_path + "bullet.png"), (20, 10))