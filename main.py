import math

# # Задаём значения
item_pool = {'В': (3,25),
             'П': (2,15),
             'Б': (2,15),
             "А": (2,20),
             "И": (1,5),
             "Н": (1,15),
             "Т": (3,20),
             "О": (1,25),
             "Ф": (1,15),
             "Д": (1,10),
             "Е": (2,20),
             "Р": (2,20)
             }

omg = [2*4, 20, 0]
taken = []
best = []
pipi = [0]

# # Вычитаем очки
for i in item_pool:
    omg[1] -= item_pool[i][1]

# # Функции
def dobavit(index):
    taken.append(index)
    omg[0] -= item_pool[index][0]
    omg[1] += 2 * item_pool[index][1]

def ubrat(index):
    taken.remove(index)
    omg[0] += item_pool[index][0]
    omg[1] -= 2 * item_pool[index][1]

def perebor():
    if omg[0] > 0:
        for index in item_pool:
            if (index not in taken) and (omg[0] - item_pool[index][0] >= 0):
                dobavit(index)
                perebor()
                ubrat(index)
    else:
        pipi[0] += 1
        if omg[1] > omg[2]:
            omg[2] = omg[1]
            del best[:]
            for i in taken:
                best.append(i)


# # Добавляем в рюкзак Ингалятор
dobavit("И")

perebor()

#print(pipi[0])
print('Максимальное количество очков равно ' + str(omg[2]) + '\n')

# # Отображение таблицей
visual = [[0 for x in range(4)] for y in range(2)]
best1 = []

for a in best:
    for i in range(item_pool[a][0]):
        best1.append(a)

for a in range(len(best1)):
    visual[math.floor(a / 4)][a - 4 * math.floor(a / 4)] = best1[a]

for y in range(len(visual)):
    for x in range(len(visual[y])):
        print(' [' + visual[y][x] + '] ', end='')
    print()