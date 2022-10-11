import random
import os
import sys

game = True

board = {0: " ", 1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

players = {"Player 1": "", "Player 2": ""}

rounds = 1

check = 0


def show_round(rounds):
    if rounds % 1 == 0:
        print(f"\nROUND {int(rounds)}!")
    else:
        pass


def show_board(board):
    print("     |   |   ")
    print("   " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("     |   |   ")
    print("  --- --- ---")
    print("     |   |   ")
    print("   " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("     |   |   ")
    print("  --- --- ---")
    print("     |   |   ")
    print("   " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("     |   |   ")


def select_character(players):
    while True:
        players["Player 1"] = input("\nPLAYER 1, PLEASE SELECT YOUR CHARACTER [O/X]: ").capitalize()
        if players["Player 1"] == "X":
            players["Player 2"] = "O"
            print("\nPLAYER 1 IS 'X' AND PLAYER 2 IS 'O'!")
            break
        elif players["Player 1"] == "O":
            players["Player 2"] = "X"
            print("\nPLAYER 1 IS 'O' AND PLAYER 2 IS 'X'!")
            break
        else:
            print("\nSORRY, I DON'T UNDERSTAND!")


def choose_first():
    global check
    if random.randint(0, 1) == 0:
        print("\nPLAYER 1 STARTS!")
        check += 0
    else:
        print("\nPLAYER 2 STARTS!")
        check += 1


def select_move(check, board, available_moves, players):
    while True:
        if check % 2 != 0:
            move = input(f"\nPLAYER 1, PLEASE SELECT YOUR MOVE {available_moves}: ")
            if move.isdigit():
                if int(move) in available_moves:
                    board[int(move)] = players["Player 1"]
                    available_moves.remove(int(move))
                    break
                else:
                    print("\nSORRY, I DON'T UNDERSTAND!")
                    continue
            else:
                print("\nSORRY, I DON'T UNDERSTAND!")
                continue
        elif check % 2 == 0:
            move = input(f"\nPLAYER 2, PLEASE SELECT YOUR MOVE {available_moves}: ")
            if move.isdigit():
                if int(move) in available_moves:
                    board[int(move)] = players["Player 2"]
                    available_moves.remove(int(move))
                    break
                else:
                    print("\nSORRY, I DON'T UNDERSTAND!")
                    continue
            else:
                print("\nSORRY, I DON'T UNDERSTAND!")
                continue


def check_board(board, check):
    if board[1] == board[2] == board[3] == "O" or board[4] == board[5] == board[6] == "O" or board[7] == board[8] == \
            board[9] == "O" or board[1] == board[4] == board[7] == "O" or board[2] == board[5] == board[8] == "O" or \
            board[3] == board[6] == board[9] == "O" or board[1] == board[5] == board[9] == "O" or board[3] == board[
        5] == board[7] == "O":
        if players["Player 1"] == "O":
            print("\nCONGRATULATIONS! PLAYER 1 WINS!")
        else:
            print("\nCONGRATULATIONS! PLAYER 2 WINS!")
    elif board[1] == board[2] == board[3] == "X" or board[4] == board[5] == board[6] == "X" or board[7] == board[8] == \
            board[9] == "X" or board[1] == board[4] == board[7] == "X" or board[2] == board[5] == board[8] == "X" or \
            board[3] == board[6] == board[9] == "X" or board[1] == board[5] == board[9] == "X" or board[3] == board[
        5] == board[7] == "X":
        if players["Player 1"] == "X":
            print("\nCONGRATULATIONS! PLAYER 1 WINS!")
        else:
            print("\nCONGRATULATIONS! PLAYER 2 WINS!")
    elif len(available_moves) == 0:
        print("\nDRAW!")
    else:
        pass


print("+ + + + + + + +")
print("+ TIC-TAC-TOE +")
print("+ + + + + + + +\n")

print("WELCOME TO THE GAME!")

select_character(players)

print("\nLIST OF MOVEMENTS:\n")

show_board(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

choose_first()

while game:

    show_round(rounds)

    rounds += 0.5

    check += 1

    select_move(check, board, available_moves, players)

    print("\n")

    show_board(board)

    check_board(board, check)

    if board[1] == board[2] == board[3] == "O" or board[4] == board[5] == board[6] == "O" or board[7] == board[8] == \
            board[9] == "O" or board[1] == board[4] == board[7] == "O" or board[2] == board[5] == board[8] == "O" or \
            board[3] == board[6] == board[9] == "O" or board[1] == board[5] == board[9] == "O" or board[3] == board[
        5] == board[7] == "O" or board[1] == board[2] == board[3] == "X" or board[4] == board[5] == board[6] == "X" or \
            board[7] == board[8] == board[9] == "X" or board[1] == board[4] == board[7] == "X" or board[2] == board[
        5] == board[8] == "X" or board[3] == board[6] == board[9] == "X" or board[1] == board[5] == board[9] == "X" or \
            board[3] == board[5] == board[7] == "X" or len(available_moves) == 0:
        break

while True:
    answer = input("DO YOU WANT TO PLAY ONE MORE TIME (Y/N): ")
    if answer.capitalize() == 'T':
        sys.exit()
        break
    elif answer.capitalize() == "N":
        sys.exit()
        break
    else:
        print("SORRY, I DON'T UNDERSTAND!")