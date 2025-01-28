# Игру «Крестики-нолики».
# Консоль, куда будет выводиться ход игры.
# Тут делать красиво мы умеем с помощью форматированных строк.
# Неутолимое желание написать что-то реальное своими руками.
# Размер поля предполагается равным 3x3, есть возможность увеличить поле
# Критерии оценивания

# Функционал печати поля.
# 1 Создана функция, которая будет отображать текущее состояние игрового поля в консоли.
# 2 Функция проверки завершенности игры.
# 3 Разработана функция, которая будет проверять текущее состояние игрового поля и определять, завершилась ли игра (например, кто-то выиграл или ничья).
# 4 Проверка корректности ввода.
# Обеспечена проверка корректности ввода пользователем координат для хода.
# Кодстайл. Использованы понятные имена переменных и функций, добавлены комментарии
# для пояснения сложных участков кода.
# Пользовательский интерфейс.
# Разработан пользовательский интерфейс, который позволит игрокам взаимодействовать с игрой.

def game_field(leight=3)->list: # Формирование игрового поля по умолчанию 3 клетки
    board =  ([i+2 * j+1 for j in range(leight)] for i in range(leight))
    return board


def display_field(field:list): #
     for i in list(field):
         print('-' * (len(field) *5))
         print(f'|{i}|')

def input_simbol():
    count = 0
    while True:
        line = int(input('В какую строку введем символ 1-2-3... : '))
        column = int(input('В какой столбец введем символ 1-2-3... :'))
        if len(field) <line or len(field) < column: # проверка на превышение координат поля
            print('введеные координаты клетки за пределами игрового поля')
            continue
        if (field[line - 1][column - 1] == '0' or field[line - 1][column - 1] == 'x' ): # Проверка на занятость клетки
            print('Данная клетка занята')
            continue
        if count % 2 == 0:
            field[line - 1][column-1] = '0'
            display_field(field)
            verefication_viktory()
        else:
            field[line-1][column-1] = 'x'
            display_field(field)
            verefication_viktory()
        count +=1
        if count == (len(field) * len(field)): # Проверка на заполнение игрового поля, выход с цикла, ничья
            print('Ничья')
            break

def verefication_viktory():
    for i in range(len(field)): # проверка победы строка
        if len(set(field[i])) == 1:
           print ('Победа 1')
    list_out = []
    for i in range(len(field)):
        list_out.append(field[i][i]) # проверка победы диагональ( лево - верх -> право - низ)
    if len(set(list_out)) == 1:
        print ('Победа 2')
    list_out = []
    for i in range(len(field)): # проверка победы диагональ( лево - низ -> право -верх)
        list_out.append(field[i][-(i+1)])
    if len(set(list_out)) == 1:
        print ('Победа 3')
    list_out =[]
    for i in range(len(field)): # проверки победу столбец
        for j in range(len(field)):
            list_out.append(field[j][i])
        if len(set(list_out)) == 1:
            print ('Победа 4')
        list_out = []
    return True



if __name__ == '__main__':
    field =  list(game_field(5))
    print(display_field(field))
    sumbol_board = input_simbol()


