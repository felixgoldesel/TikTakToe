from PlayerClass import Player
import numpy as np

list_row1 = []
list_row2 = []
list_row3 = []

column = 3
for i in range(column):
    list_row1.append(' ')
    list_row2.append(' ')
    list_row3.append(' ')

arr1 = np.array(list_row1)
arr2 = np.array(list_row2)
arr3 = np.array(list_row3)


def main(turn=1):
    player1 = Player(x_o='X', list_possibilities=[[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9]])
    player2 = Player(x_o='O', list_possibilities=[[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9]])
    while player1.win_player is False and player2.win_player is False and player1.draw is False and player2.draw is False:
        if turn % 2 == 1:
            print("Spieler 1 ist dran: Setze dein Zeichen (1-9)")
            player1.set_sign(arr1, arr2, arr3)
            turn += 1
            if player1.win_player:
                print("Spieler 1 gewinnt!")
        elif turn % 2 == 0:
            print("Spieler 2 ist dran: Setze dein Zeichen (1-9)")
            player2.set_sign(arr1, arr2, arr3)
            turn += 1
            if player2.win_player:
                print("Spieler 2 gewinnt!")


if __name__ == "__main__":
    main()



