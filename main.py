# Крестики-нолики

# Делаем поле
board = [' ' for _ in range(9)]

# Отображения поля
def print_board():
    print('---------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|', end='')
        print('   ', i*3+1, '|', i*3+2, '|', i*3+3, '|')
        print('-------------')

# проверка победителя
def check_win(player):
    # проверка рядов
    for i in range(3):
        if board[i*3] == board[i*3 + 1] == board[i*3 + 2] == player:
            return True
    # проверка вертикаль
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # проверка диагональ
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# пошла жара
def play_game():
    current_player = 'X'
    while True:
        print_board()
        position = int(input("Куда ходить- (1-9): ")) - 1
        if position >= 0 and position < 9:
            if board[position] == ' ':
                board[position] = current_player
                if check_win(current_player):
                    print_board()
                    print("Игрок", current_player, "выйграл!")
                    break
                elif ' ' not in board:
                    print_board()
                    print("Ничья")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Ходи правельно")
        else:
            print("Ходи как положено")

# включаем отопление
print("Первый ходит Х")
play_game()
