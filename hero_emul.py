import pygame
import random
# import time         # temp

# -----------------------ЦВЕТА
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
# -----------------------РАЗМЕРЫ ЭКРАНА
DIS_WIDTH = 200
DIS_HEIGHT = 100

SNAKE_BLOCK = 10        # -----------------------РАЗМЕР БЛОКА
SNAKE_SPEED = 15        # -----------------------СКОРОСТЬ ИГРЫ

class Simul():
    def __init__(self):
        pygame.init()
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
        pygame.display.set_caption('Sim')

    # ------------------------вывод сообщения
    def message(self, msg, color):
        self.dis.fill(BLUE)
        m = self.font_style.render(msg, True, color)
        self.dis.blit(m, [DIS_WIDTH / 6, DIS_HEIGHT / 3])
        pygame.display.update()

    # ------------------------Обработка клавиш управления
    def key_dir_proc(self):
        x = 0
        y = 0
        g = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # - системное сообщение о выходе
                g = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -SNAKE_BLOCK
                elif event.key == pygame.K_RIGHT:
                    x = SNAKE_BLOCK
                elif event.key == pygame.K_UP:
                    y = -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    y = SNAKE_BLOCK
                elif event.key == pygame.K_q:
                    # self.sim_quit()
                    g = True
        return x, y, g

    # -----------------------обработка меню стоп-старт
    def menu_start(self):
        self.message("C-Again or Q-Quit", RED)
        while True:
            for event in pygame.event.get():    # опрашиваем клавиши Q C
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        return True             # QUIT
                    if event.key == pygame.K_c:
                        return False            # not QUIT

    # --------------------ГЛАВНЫЙ ЦИКЛ
    def sim_loop(self, flag_info, matrix_size, hero_xy, food_xy, hero_direct, condition, quit_sim):
        matrix_size[0] = DIS_WIDTH                              # размеры в драйвер для формирования матрицы
        matrix_size[1] = DIS_HEIGHT
        sim_over = False
        sim_menu = False
        x1 = DIS_WIDTH / 2
        y1 = DIS_HEIGHT / 2
        x = x1
        y = y1
        x1_change = 0
        y1_change = 0
        food_x = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
        food_y = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
        clock = pygame.time.Clock()

        while not sim_over:                                     # пока симуляция глобально не завершена
            key_data = self.key_dir_proc()                      # опрос клавиатуры
            x1 = x + key_data[0]                                # новые координаты до проверки
            y1 = y + key_data[1]
            if key_data[2]:                                     # если выход в меню-старт
                sim_over = self.menu_start()

            flag_info = False                                   # запретить доступ другому потоку
            if hero_direct[0] == 1:
                y1 = y - SNAKE_BLOCK
            if hero_direct[0] == 2:
                x1 = x + SNAKE_BLOCK
            if hero_direct[0] == 4:
                y1 = y + SNAKE_BLOCK
            if hero_direct[0] == 8:
                x1 = x - SNAKE_BLOCK
            hero_direct[0] = 0
            flag_info = True                                    # разрешить доступ другому потоку

            # проверка координат hero на столкновения со стеной
            if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
                pass        # здесь возможно какая нибудь реакция на столкновение
            else:
                x = x1      # ввод новых проверенных координат
                y = y1

            # отрисовка кадра
            self.dis.fill(BLUE)
            pygame.draw.rect(self.dis, BLACK, [x, y, SNAKE_BLOCK, SNAKE_BLOCK])
            pygame.draw.rect(self.dis, GREEN, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])   # еда

            pygame.display.update()
            # если встретились с едой
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
                food_y = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            clock.tick(SNAKE_SPEED)

        # ---------------------------------------
        quit_sim[0] = True
        self.sim_quit()

    def sim_quit(self):
        pygame.quit()
        quit()
