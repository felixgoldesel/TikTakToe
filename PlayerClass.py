import numpy as np


class Player:
    # wichtig für feststellung ob eine 3er linie gebildet werden kann
    occupied1 = False
    occupied2 = False
    occupied3 = False
    occupied4 = False
    occupied5 = False
    occupied6 = False
    occupied7 = False
    occupied8 = False
    occupied9 = False

    occupied_x1 = False
    occupied_x2 = False
    occupied_x3 = False
    occupied_x4 = False
    occupied_x5 = False
    occupied_x6 = False
    occupied_x7 = False
    occupied_x8 = False
    occupied_x9 = False
    win_player = False
    draw = False

    def __init__(self, x_o, list_possibilities):
        self.list_possibilities = list_possibilities
        self.x_o = x_o

    def set_sign(self, arr1, arr2, arr3):

        input_field = int(input())
        if input_field == 1:
            if arr1[0] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr1[0] = self.x_o
                self.occupied_x1 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 2:
            if arr1[1] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr1[1] = self.x_o
                self.occupied_x2 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 3:
            if arr1[2] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr1[2] = self.x_o
                self.occupied_x3 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 4:
            if arr2[0] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr2[0] = self.x_o
                self.occupied_x4 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 5:
            if arr2[1] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr2[1] = self.x_o
                self.occupied_x5 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 6:
            if arr2[2] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr2[2] = self.x_o
                self.occupied_x6 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 7:
            if arr3[0] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr3[0] = self.x_o
                self.occupied_x7 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 8:
            if arr3[1] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr3[1] = self.x_o
                self.occupied_x8 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        elif input_field == 9:
            if arr3[2] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr3[2] = self.x_o
                self.occupied_x9 = True
                self.remove_possibilities(self.list_possibilities, input_field)
        else:
            print("Diese Eingabe ist nicht möglich")

        if self.occupied_x1 and self.occupied_x2 and self.occupied_x3 is True:
            self.win_player = True
        elif self.occupied_x1 and self.occupied_x4 and self.occupied_x7 is True:
            self.win_player = True
        elif self.occupied_x1 and self.occupied_x5 and self.occupied_x9 is True:
            self.win_player = True
        elif self.occupied_x2 and self.occupied_x5 and self.occupied_x8 is True:
            self.win_player = True
        elif self.occupied_x3 and self.occupied_x5 and self.occupied_x7 is True:
            self.win_player = True
        elif self.occupied_x3 and self.occupied_x6 and self.occupied_x9 is True:
            self.win_player = True
        elif self.occupied_x4 and self.occupied_x5 and self.occupied_x6 is True:
            self.win_player = True
        elif self.occupied_x7 and self.occupied_x8 and self.occupied_x9 is True:
            self.win_player = True

        if not self.list_possibilities:
            self.draw = True
            print("Unentschieden!")

        print(arr1)
        print(arr2)
        print(arr3)

    def remove_possibilities(self, list_possibilities, input_field):
        temp = []

        for possibility in self.list_possibilities:

            for number in possibility:
                if number == input_field:
                    temp.append(possibility)
                    continue

        self.list_possibilities = [element for element in self.list_possibilities if element not in temp]
        #print(self.list_possibilities)
        return self.list_possibilities

