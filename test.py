import numpy as np


matrix = np.array([
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 0, 0, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 0, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]
              ])

def step( y_n, x_n, y_p, x_p, color, mtrx):
    # таблица координат вокруг центра
    tab_cells_yx = np.array([[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],
                    [-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]) + [y_n, x_n]
   # определяем на какое место вокруг центра указывает старая координата и какой её индекс в таблице
    c = 0
    find_p = False                      # фалс-ищем индекс предыдущей координаты, тру-ищем место для следующей
    for i in tab_cells_yx:
        if not find_p:                  # ищем индекс предыдущей координаты
            if np.array_equal([y_p, x_p],i):
                find_p = True
                c += 1
                continue
        else:                           # ищем место для следующей координаты
            # начиная с этого индекса ищем переход от клетки с нецелевым цветов к клетке с целевым
            if mtrx[tab_cells_yx[c-1][0]][tab_cells_yx[c-1][1]] != mtrx[i[0]][i[1]] and \
                    (mtrx[i[0]][i[1]] == color or mtrx[i[0]][i[1]] == 2):
                return i    # возвращаем следующую координату
        c += 1
    return -1
yx_start = [4, 1]
yx_curr = yx_start
yx_prev = [4, 2]

for i in range(18):
    matrix[yx_curr[0]][yx_curr[1]] = 2
    temp = step( yx_curr[0], yx_curr[1], yx_prev[0], yx_prev[1], 0, matrix )
    yx_prev = yx_curr
    yx_curr = temp

print(matrix)