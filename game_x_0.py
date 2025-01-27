# Игру «Крестики-нолики».
# Консоль, куда будет выводиться ход игры.
# Тут делать красиво мы умеем с помощью форматированных строк.
# Неутолимое желание написать что-то реальное своими руками.
# Размер поля предполагается равным 3x3.

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

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")