import pygame
from data import *   #імпорти
from util import *
import time
pygame.init()     #ініцилізація біліотеки

#налаштування вікна
window = pygame.display.set_mode((set_win["WIDTH"], set_win["HEIGHT"]))
pygame.display.set_caption("CsGo2.0")
amount = None
#функція запуску
def play():
    kills = 0
    game = True
    clock = pygame.time.Clock()    #налаштування вікна
    clock.tick(set_win["FPS"])
    respawn = time.time()
    ninja = Player(350, 350, ninja_stay_withgun_image, ninja_run_withgun1_image, ninja_run_withgun2_image, speed = 5)     #гравець
    respawn = time.time()   #стартове значення таймера
    bot = Bot(350, 0, 40, 80, zombie_run1_image, zombie_stay_image, zombie_run2_image, speed = 4)
    lose = False

    #ігровий цикл
    while game:
        
        events = pygame.event.get()
        window.blit(bg_image, (0, 0))
        window.blit(ninja.IMAGE_NOW, (ninja.x, ninja.y))
      
        #window.blit(bot.IMAGE1, (bot.x, bot.y))
        ninja.move(ninja.x, ninja.y)
        
        #time1 = time.time()   #якась глупость
        #time2 = time.time()   #якась глупость
        if ninja.SHOT == True:
            for bullet in ninja.BULLET:
                bullet.x += bullet.X
                bullet.y +=  bullet.Y
                window.blit(bullet.IMAGE, (bullet.x, bullet.y))
                for bot in bots_list:
                    if bot.colliderect(bullet):
                        bots_list.remove(bot)
                        ninja.BULLET.remove(bullet)
                        kills += 1
                        ninja.SHOT = False
                        break
                if bullet.x > set_win["WIDTH"] or bullet.y > set_win["HEIGHT"] or bullet.x < 0 or bullet.y < 0:
                    ninja.BULLET.remove(bullet)
                    ninja.SHOT = False
        
           
        font_kills = pygame.font.SysFont("Arial", 30)
        render_kills = font_kills.render("Вбивства", True, (0, 0, 0))
        font_kills_value = pygame.font.SysFont("Arial", 30)
        render_kills_vlaue = font_kills_value.render(str(kills), True, (0,0,0))
        font_lose = pygame.font.SysFont("Arial", 30)
        render_font_lose = font_lose.render("Програш", True, (255, 0, 0))
        window.blit(render_kills, (550, 0))
        window.blit(render_kills_vlaue, (670, 0))
        if lose:
            window.blit(render_font_lose, (350, 350))
            pygame.display.flip()
            time.sleep(2)
            game = False
        #блітаєм ботіков
        for bot in bots_list:
            window.blit(bot.IMAGE1, (bot.x, bot.y))
            bot.step(ninja)
            if bot.colliderect(ninja):
                lose = True  
       #if ninja.SHOT == True:
       #    for bullet in ninja.BULLET:
       #        bullet.x += bullet.X
       #        bullet.y += bullet.Y
       # print(len(bots_list))
             #призив ботіков
        if time.time() - respawn >= 0.5:    #умова таймера
            bots_list.append(Bot(350, 0, 40, 80, zombie_run1_image, zombie_stay_image, zombie_run2_image, speed = 4))   #призив ботов в пехоту
            respawn = time.time()   #старт таймера
        
        for event in events:    #івенти
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ninja.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    ninja.MOVE["DOWN"] = True
                if event.key == pygame.K_a:
                    ninja.MOVE["LEFT"] = True

                if event.key == pygame.K_d:
                    ninja.MOVE["RIGHT"] = True


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    ninja.MOVE["UP"] = False

                if event.key == pygame.K_s:
                    ninja.MOVE["DOWN"] = False
                if event.key == pygame.K_a:
                    ninja.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                    ninja.MOVE["RIGHT"] = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not ninja.SHOT:
                ninja.SHOT = True
                ninja.BULLET.append(Bullet(ninja.x,ninja.y, 20, 10))
                x,y = event.pos
                ninja.BULLET[-1].make_angle(x, y,ninja.x,ninja.y)

        pygame.display.flip()
        clock.tick(set_win["FPS"])

play()