import numpy as np

liste_zeile1 = []
liste_zeile2 = []
liste_zeile3 = []

column = 3
for i in range(column):
    liste_zeile1.append(' ')
    liste_zeile2.append(' ')
    liste_zeile3.append(' ')

arr1 = np.array(liste_zeile1)
arr2 = np.array(liste_zeile2)
arr3 = np.array(liste_zeile3)

occupiedX1 = False
occupiedX2 = False
occupiedX3 = False
occupiedX4 = False
occupiedX5 = False
occupiedX6 = False
occupiedX7 = False
occupiedX8 = False
occupiedX9 = False
occupiedO1 = False
occupiedO2 = False
occupiedO3 = False
occupiedO4 = False
occupiedO5 = False
occupiedO6 = False
occupiedO7 = False
occupiedO8 = False
occupiedO9 = False

win = False
winS1 = False
winS2 = False
zug = 1
global_counter = 0

print("1 Spieler oder 2 Spieler?")
input_field = int(input())
# Spieler gegen Bot

if input_field == 1:
    while not win and global_counter != 9:
        print("bot")
        global_counter += 1

# Spieler gegen Spieler
elif input_field == 2:
    while not win and global_counter != 9:
        # Spieler 1
        if zug % 2 == 1:
            print("Spieler 1: Wo willst du dein Zeichen setzen (1-9)?")

            input_field = int(input())

            if input_field == 1:
                if arr1[0] == 'X' or arr1[0] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr1[0] = 'X'
                    occupiedX1 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 2:
                if arr1[1] == 'X' or arr1[1] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr1[1] = 'X'
                    occupiedX2 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 3:
                if arr1[2] == 'X' or arr1[2] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr1[2] = 'X'
                    occupiedX3 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 4:
                if arr2[0] == 'X' or arr2[0] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr2[0] = 'X'
                    occupiedX4 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 5:
                if arr2[1] == 'X' or arr2[1] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr2[1] = 'X'
                    occupiedX5 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 6:
                if arr2[2] == 'X' or arr2[2] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr2[2] = 'X'
                    occupiedX6 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 7:
                if arr3[0] == 'X' or arr3[0] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr3[0] = 'X'
                    occupiedX7 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 8:
                if arr3[1] == 'X' or arr3[1] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr3[1] = 'X'
                    occupiedX8 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 9:
                if arr3[2] == 'X' or arr3[2] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr3[2] = 'X'
                    occupiedX9 = True
                    zug += 1
                    global_counter += 1
            else:
                print("Diese Eingabe ist nicht möglich")

            if occupiedX1 and occupiedX2 and occupiedX3 is True:
                win = True
                winS1 = True
            elif occupiedX1 and occupiedX4 and occupiedX7 is True:
                win = True
                winS1 = True
            elif occupiedX1 and occupiedX5 and occupiedX9 is True:
                win = True
                winS1 = True
            elif occupiedX2 and occupiedX5 and occupiedX8 is True:
                win = True
                winS1 = True
            elif occupiedX3 and occupiedX5 and occupiedX7 is True:
                win = True
                winS1 = True
            elif occupiedX3 and occupiedX6 and occupiedX9 is True:
                win = True
                winS1 = True
            elif occupiedX4 and occupiedX5 and occupiedX6 is True:
                win = True
                winS1 = True
            elif occupiedX7 and occupiedX8 and occupiedX9 is True:
                win = True
                winS1 = True

            print(arr1)
            print(arr2)
            print(arr3)

        elif zug % 2 == 0:
            print("Spieler 2: Wo willst du dein Zeichen setzen (1-9)?")

            input_field = int(input())

            if input_field == 1:
                if arr1[0] == 'X' or arr1[0] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr1[0] = 'O'
                    occupiedO1 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 2:
                if arr1[1] == 'X' or arr1[1] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr1[1] = 'O'
                    occupiedO2 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 3:
                if arr1[2] == 'X' or arr1[2] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr1[2] = 'O'
                    occupiedO3 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 4:
                if arr2[0] == 'X' or arr2[0] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr2[0] = 'O'
                    occupiedO4 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 5:
                if arr2[1] == 'X' or arr2[1] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr2[1] = 'O'
                    occupiedO5 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 6:
                if arr2[2] == 'X' or arr2[2] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr2[2] = 'O'
                    occupiedO6 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 7:
                if arr3[0] == 'X' or arr3[0] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr3[0] = 'O'
                    occupiedO7 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 8:
                if arr3[1] == 'X' or arr3[1] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr3[1] = 'O'
                    occupiedO8 = True
                    zug += 1
                    global_counter += 1
            elif input_field == 9:
                if arr3[2] == 'X' or arr3[2] == 'O':
                    print("Dieses Feld ist bereits belegt!")
                else:
                    arr3[2] = 'O'
                    occupiedO9 = True
                    zug += 1
                    global_counter += 1
            else:
                print("Diese Eingabe ist nicht möglich")

            if occupiedO1 and occupiedO2 and occupiedO3 is True:
                win = True
                winS2 = True
            elif occupiedO1 and occupiedO4 and occupiedO7 is True:
                win = True
                winS2 = True
            elif occupiedO1 and occupiedO5 and occupiedO9 is True:
                win = True
                winS2 = True
            elif occupiedO2 and occupiedO5 and occupiedO8 is True:
                win = True
                winS2 = True
            elif occupiedO3 and occupiedO5 and occupiedO7 is True:
                win = True
                winS2 = True
            elif occupiedO3 and occupiedO6 and occupiedO9 is True:
                win = True
                winS2 = True
            elif occupiedO4 and occupiedO5 and occupiedO6 is True:
                win = True
                winS2 = True
            elif occupiedO7 and occupiedO8 and occupiedO9 is True:
                win = True
                winS2 = True
            print(arr1)
            print(arr2)
            print(arr3)

    if global_counter == 9:
        print("Es ist unentschieden!")
    if winS1 is True:
        print("Spieler 1 gewinnt!")
    elif winS2 is True:
        print("Spieler 2 gewinnt!")





