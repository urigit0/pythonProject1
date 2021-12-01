
import time


def move(flag, mov):    # ожидание доступа к данным
    while not flag:
        print("wait")
        pass
    return mov


def start(flag_info, matrix, matrix_size, flag_matrix_chang, hero_direct, condition, quit_sim):
    pass
    hero_direct[0] = move(flag_info, 1)
    time.sleep(0.5)
    hero_direct[0] = move(flag_info, 2)
    time.sleep(0.5)
    hero_direct[0] = move(flag_info, 4)
    time.sleep(0.5)
    hero_direct[0] = move(flag_info, 8)
    time.sleep(0.5)
