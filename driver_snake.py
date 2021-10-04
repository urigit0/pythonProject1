import snake_emul
import ii_controll
from threading import Thread

flag_info = True                                # флаг доступа к инфе
snake_list_buff = []                            # буффер змеи
snake_food = []
snake_direct = 0


def start():
        # поток симуляции
        thread1 = Thread(target=snake_emul.game_loop, args=(flag_info, snake_list_buff,
                                                            snake_food, snake_direct))
        thread1.start()
        # поток управления


        # поток драйвера


        # закрытие потоков
        thread1.join()



