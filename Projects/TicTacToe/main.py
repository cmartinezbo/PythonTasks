import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def game_figures():
    while True:
        user_1 = input("Which one do you want? X or O?: ").upper()

        if user_1 != "X" and user_1 != "O":
            print("Type a valid option!")
        else:
            break
    user_2 = "O" if user_1 == "X" else "X"
    return user_1, user_2


def who_start():
    num_user_1 = 0
    num_user_2 = 1
    random_number = random.randint(0, 1)
    if random_number == num_user_1:
        print("Player 1 starts!")
        num_user_1 = True
        num_user_2 = False
    else:
        print("Player 2 starts!")
        num_user_1 = False
        num_user_2 = True
    return num_user_1, num_user_2


def match_dev(player_figure, board):
    while True:
        place_num = input("Write a place to move: ")
        if is_valid_int(place_num):
            place_num = int(place_num)
            if is_valid_place(place_num):
                break
            else:
                print("Type a number between 1 - 9!")
        else:
            print("Type a number!")

    board[place_num - 1] = player_figure
    print("\n")
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print("\n")


def is_valid_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def is_valid_place(number):
    return True if 1 <= number <= 9 else False


# DONE : Choose who's going to start (function)
# TODO : Game dev
# TODO : Winnings possibilities
# TODO: Loop Game Dev
# TODO: Check if the place is filled or empty

def game():
    players = game_figures()
    positions = who_start()
    count = 0
    if positions[0]:

        while count < 5:
            i = 0
            match_dev(players[i], board)
            match_dev(players[i + 1], board)
            count += 1

    else:
        while count < 5:
            i = 0
            match_dev(players[i + 1], board)
            match_dev(players[i], board)
            count += 1


game()
