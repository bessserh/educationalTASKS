from random import randint
import time
import socket

board = [['-',  '-',  '-'], ['-',  '-',  '-'], ['-',  '-',  '-']]
is_x = True
counter = 0
stop = False
komp_play = []

def show(board):
    for i in board:
        print('|'.join(i))


def check_win(board):

    # строчки
    for line in board:
        if line[0] == 'X' and line[1] == 'X' and line[2] == 'X':
            return 'Xwin'
        elif line[0] == '0' and line[1] == '0' and line[2] == '0':
            return '0win'

    # столбцы
    for elem in range(len(board[0])):  # проверяем по 0-му элементу, т.к. длина всех элементов равна
        if board[0][elem] == 'X' and board[1][elem] == 'X' and board[2][elem] == 'X':
            return 'Xwin'
        elif board[0][elem] == '0' and board[1][elem] == '0' and board[2][elem] == '0':
            return '0win'

    # диагонали
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 'Xwin'
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 'Xwin'
    elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':
        return '0win'
    elif board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0':
        return '0win'


def print_result(check, two_players=True):

    global counter, stop, komp_play
    winner_x = '1-й Игрок тот шо X'
    winner_0 = '2-й Игрок тот шо 0'

    if two_players == False:
        if komp_play[1] == 'X':
            winner_x = '{}(играл "X")'.format(komp_play[0])
            winner_0 = '{}(играл "0")'.format(socket.gethostname())
        elif komp_play[1] == '0':
            winner_x = '{}(играл "X")'.format(socket.gethostname())
            winner_0 = '{}(играл "0")'.format(komp_play[0])


    if check == 'Xwin':
        print('----------РЕЗУЛЬТАТ----------')
        print('{} победил \n ПОЗДРАВЛЯЕМ'.format(winner_x))
        print('----------НАИГРАЛИСЬ----------')
        stop = True
        return True

    elif check == '0win':
        print('----------РЕЗУЛЬТАТ----------')
        print('{} победил \n ПОЗДРАВЛЯЕМ'.format(winner_0))
        print('----------НАИГРАЛИСЬ----------')
        stop = True
        return True
    elif counter == len(board)**2:
        print('----------РЕЗУЛЬТАТ----------')
        print("НИЧЬЯ")
        stop = True
        return True
    else:
        return False


def computer_move(board, symbol):
    # не успел дописать чтоб компьтер крыл там 2 заполнено
    global counter
    move_done = False
    print('Компьютер "{}": Думаю:'.format(socket.gethostname()), end='')
    delay = randint(0, 3)
    for i in range(delay):
        print('.', end='')
        time.sleep(1)
    print()
    counter += 1
    while not move_done and counter <= 9:
        x = randint(0, 2)
        y = randint(0, 2)

        if board[x][y] == '-':
            board[x][y] = symbol
            move_done = True
        else:
            continue

    return board


def player_move(board, symbol, name):
    global counter
    good_move = False
    try:
        print('{} Введите координаты'.format(name))
        x = int(input('Введите строку:')) - 1
        y = int(input('Введите столбец:')) - 1
        board[x][y]

    except ValueError:
        print('Это не число не может быть координатами')
    except IndexError:
        print('Выход за пределы доски, значения от 1 до 3-х')
    else:
        if board[x][y] is not '-':
            print('{} повнимательнее, тут уже занято'.format(name))
        else:
            board[x][y] = symbol
            good_move = True
            counter += 1

    return board, good_move


def single_player(board, symbol='X', name='ИГРОК'):
    global counter
    if symbol == 'X':
        flag_do = False
        if counter == 0:
            show(board)  # показ доски

        while not flag_do:
            move = player_move(board, symbol, name)
            if move[1] == True:
                board = move[0]
                print_result(check_win(board), False)
                if counter == 9:
                    flag_do = move[1]
                    return board

                board = computer_move(board, '0')
                show(board)     # показ доски
                print_result(check_win(board), False)
                flag_do = move[1]

    elif symbol == '0':
        flag_do = False


        board = computer_move(board, 'X')
        show(board)     # показ доски
        print_result(check_win(board), False)
        if counter == 9:
            return board

        while not flag_do:
            move = player_move(board, symbol, name)
            if move[1] == True:
                board = move[0]
                print_result(check_win(board), False)
                flag_do = move[1]


    return board


def two_players(board):

    global is_x, counter
    print_result(check_win(board))
    if counter == 0:
        show(board)
    try:
        if is_x:
            name = '1-й игрок тот шо Х'
        else:
            name = '2-й игрок тот шо 0'

        print('{} Введите координаты'.format(name))

        x = int(input('Введите строку:'))-1
        y = int(input('Введите столбец:'))-1
        board[x][y]
    except ValueError:
        print('Это не число не может быть координатами')
    except IndexError:
        print('Выход за пределы доски, значения от 1 до 3-х')
    else:
        if board[x][y] is not '-':
            print('{} повнимательнее, тут уже занято'.format(name))
        else:
            counter += 1
            if is_x:
                board[x][y] = "X"
                is_x = False
            else:
                board[x][y] = "0"
                is_x = True
            show(board)     # показ доски
            print_result(check_win(board))
    return board


print('---------------------------X&0 GAME----------------------------')
print('----------------cross/null(by Bes, built 1.1.2)----------------')
print()

while True:

    print('Выберите режим игры:')
    print('     (S) для игры с компьютером')
    print('     (M) для игры 2x игроков')
    print('     (E) для того чтоб выйти')
    choise = input('Сделайте Ваш выбор:')

    game_type = ''

    if choise == 'S' or choise == 's':
        print('Привет я компьтер, зовут меня "{}" давай ПОИГРАЕМ'.format(socket.gethostname()))
        while True:
            name = input('Напишите имя: ')
            print('"X" всегда ходит первый, "0" - второй!')
            ch_symbol = input('Чем будете играть: X или 0: ')

            print('Вас зовут {}, играете {}'.format(name, ch_symbol))
            yes = input('Все правильно (Y)es ?')
            if (yes == 'Y' or yes == 'y') and (ch_symbol == 'X' or ch_symbol == 'x' or ch_symbol == '0'):
                comp_play = (name, ch_symbol)

                if ch_symbol == 'X' or ch_symbol == 'x':
                    ch_symbol = 'X'
                break
            else:
                print('Неправильный ввод, или Вы сами отменили')
        game_type = 'single'
        komp_play = [name, ch_symbol]
    elif choise == 'M' or choise == 'm':
        print('Играют 2 игрока! 1-й: "X" в 2-й: "0" ')
        game_type = 'multi'
        time.sleep(3)
    elif choise == 'E' or choise == 'e':
        print('----------ВЫХОД----------')
        break
    else:
        continue



    while True:


        if game_type == 'multi':
            board = two_players(board)

        elif game_type == 'single':
            board = single_player(board, ch_symbol, name)


        if stop == True:
            break
        else:
            continue


    show(board)

    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    stop = False
    counter = 0

    print('(E) для того чтоб выйти или ANY KEY чтоб продолжить:')
    choise = input('Ваш выбор: ')
    if choise == 'E' or choise == 'e':
        break
    else:
        continue

print('---------------GOOD LUCK---------------')