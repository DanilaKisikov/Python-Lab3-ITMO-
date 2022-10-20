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

omg = [2*4, 20]
taken = []
best = []
pipi = [0, 0]

for i in item_pool:
    omg[1] -= item_pool[i][1]

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
        pipi[1] += 1
        if omg[1] > 0:
            print(str(taken) + '   ' + str(omg[1]))
            pipi[0] += 1

dobavit('И')

perebor()

print(pipi[0])
print(pipi[1])