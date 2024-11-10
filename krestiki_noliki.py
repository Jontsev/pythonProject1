# Функция для отображения игрового поля
def display_board(board):
    """ отображает текущее состояние игрового поля """
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')
    print()

# Функция для ввода игроком позиции
def player_input(player, board):
    """ запрашивает у текущего игрока позицию для хода и обновляет поле """
    while True:
        try:
            position = int(input(f"Игрок {player}, выберите позицию (1-9): ")) - 1
            if 0 <= position <= 8:
                if board[position] == ' ':
                    board[position] = player
                    break
                else:
                    print("Позиция уже занята. Попробуйте снова.")
            else:
                print("Недопустимая позиция. Введите число от 1 до 9.")
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 9.")

# Функция для проверки победы
def check_win(board, player):
    """ проверяет, есть ли выигрышная комбинация для игрока """
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальные линии
        [0, 4, 8], [2, 4, 6]              # диагональные линии
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Функция для проверки ничьей
def check_draw(board):
    """ проверяет, заполнено ли всё поле (ничья) """
    return ' ' not in board

# Основная функция игры
def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    while True:
        display_board(board)
        player_input(current_player, board)
        if check_win(board, current_player):
            display_board(board)
            print(f"Игрок {current_player} победил!")
            break
        if check_draw(board):
            display_board(board)
            print("Ничья!")
            break
        # Смена игрока
        current_player = 'O' if current_player == 'X' else 'X'

main()
# Массивы - list[] это списки
# Кортежи - tuple[,] Неизменяемый и работает быстрее списка
# Множества - set{} Изменяемый. Неупорядочен, не повтяоряются элементы, нельзя получить элемент по индексу, можно перебором
# Словарь - dict{:} Ключ:Значение. Ключи уникальны, а Значение - нет.