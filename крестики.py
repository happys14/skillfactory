board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3
def field(): # Вывод игрового поля

    print('_' * 12)

    for i in range(3):

        print('',board[i * 3] , '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('_' * 12)
def check_win(): # Проверка на победу
    win = False

    win_comb = (
        (0,1,2),(3,4,5),
        (6,7,8),(0,3,6),
        (1,4,7),(2,5,8),
        (0,4,8),(6,4,2)
    )

    for i in win_comb:
        if (board[i[0]] == board[i[1]] and board[i[1]] == board [i[2]] ):
            win = board[i[0]]

    return win
def step_game(step_player,char): # Ход
    if step_player > 9 or step_player < 1 or  board[step_player - 1] in ('X','O'):
        return False
    board[step_player - 1] = char
    return True
def start_game():     # Старт игры

    field()

    current_player = 'X'     # Текущий игрок

    num_step = 1             # Номер хода

    while (num_step < 10) and (check_win() == False):
        step_player = input('Ходит игрок -' + ' ' + current_player + ' , ''Введите номер клетки')
        if (step_game(int(step_player),current_player)):
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            field()
            num_step += 1
        else:

            print('Неверный ход. Повторите')
    if num_step == 10:
        print('Игра окончена. Ничья')
    else:
        print('Выиграл ' + check_win())
print(start_game())
