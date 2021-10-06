import pygame
# import time
import random

pygame.init()

# -----------------------ЦВЕТА
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# -----------------------РАЗМЕРЫ ЭКРАНА
dis_width = 600
dis_height = 400

snake_block = 10        # -----------------------РАЗМЕР БЛОКА

snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')
clock = pygame.time.Clock()


# ------------------------СЧЕТ
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
# ------------------------ОТРИСОВКА змеи
def our_snake(s_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], s_block, snake_block])
# ------------------------СООБЩЕНИЕ
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def game_loop(flag_info, snake_list_buff, snake_food, snake_direct):
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []         # лист с координатами всех блоков змейки
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # *******************ГЛАВНЫЙ ЦИКЛ*********************************
    while not game_over:
        # *********************************обработка клавиатуры в случае конца игры
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                         # game_loop()
                         game_over = True
                         game_close = False
        # *********************************обработка клавиатуры
        if snake_direct[0] == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
        # обработка управляющей переменной
        else:
            if snake_direct[0] == 1:
                x1_change = -snake_block
                y1_change = 0
            if snake_direct[0] == 2:
                x1_change = snake_block
                y1_change = 0
            if snake_direct[0] == 4:
                y1_change = -snake_block
                x1_change = 0
            if snake_direct[0] == 8:
                y1_change = snake_block
                x1_change = 0

        snake_direct[0] = 0
        # проверка столкновений со стеной
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        # отрисовка кадра
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  # еда
        snake_head = []  # новая коорината головы
        snake_head.append(x1)
        snake_head.append(y1)
        # добавляем голову в конец списка

        snake_list.append(snake_head)
        # если длина не увеличилась удаляем поледний сегмент хвоста
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # если голова встретилась с хвостом
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        # отрисовка змеи
        our_snake(snake_block, snake_list)

        your_score(length_of_snake - 1)

        pygame.display.update()
        # если встретились с едой
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)
        if flag_info:
            flag_info = False
            snake_list_buff = snake_list[:]
            snake_food = [foodx, foody]
            flag_info = True
    pygame.quit()
    quit()

