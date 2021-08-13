import random


def dev_board():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[7])


def game_figures():
    while True:
        user_1 = input("Which one do you want? X or O?: ").upper()

        if user_1 != "X" and user_1 != "O":
            print("Type a valid option!")
        else:
            break

    # user_2 = "O" if user == "X" else user_2 = "X"
    # return user_1, user_2


def is_valid_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
