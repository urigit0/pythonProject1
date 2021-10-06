import snake_emul
import ii_controll
# import time
from threading import Thread

flag_info = True                                # флаг доступа к инфе
snake_list_buff = []                            # буффер змеи
snake_food = []
snake_direct = [0]

def start():
        # поток симуляции
        thread_sim = Thread(target=snake_emul.game_loop, args=(flag_info, snake_list_buff, snake_food, snake_direct))
        thread_sim.start()
        # поток управления
        thread_ctrl = Thread(target=ii_controll.start, args=(flag_info, snake_list_buff, snake_food, snake_direct))
        thread_ctrl.start()
        # поток драйвера

        # закрытие потоков
        thread_sim.join()
        thread_ctrl.join()
        print('stop all')

