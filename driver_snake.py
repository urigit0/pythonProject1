# интерфейс между управляющим потоком и потком симуляции на pygame
#import snake_emul
import hero_emul
import ii_controll
# import time
from threading import Thread
import time

flag_info = True                        # флаг доступа к инфе
hero_xy = []                            # кординаты хероу
food_xy = []                            # координаты фуда
hero_direct = [0]                       # сделать шаг
condition = 0
matrix = []
matrix_size = [0, 0]
flag_matrix_chang = False
quit_sim = [False]


def start():
        sim = hero_emul.Simul()
        # поток симуляции
        thread_sim = Thread(target=sim.sim_loop, args=(flag_info, matrix_size, hero_xy, food_xy, hero_direct, condition, quit_sim))
        thread_sim.start()

        # поток управления
        thread_ctrl = Thread(target=ii_controll.start, args=(flag_info, matrix, matrix_size, flag_matrix_chang,
                                                             hero_direct, condition, quit_sim))
        thread_ctrl.start()

        # поток драйвера
        while not quit_sim[0]:
            print('drv_loop')
            print(quit_sim[0])
            time.sleep(1)

        # закрытие потоков
        thread_sim.join()
        thread_ctrl.join()






