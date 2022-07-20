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

    def __init__(self, x_o):
        self.x_o = x_o

    def set_x(self, arr1, arr2, arr3): #list_possibilities_2

        input_field = int(input())
        if input_field == 1:
            if arr1[0] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr1[0] = self.x_o
                self.occupied_x1 = True
                #self.remove_possibilities(list_possibilities_2, input_field)
                #print(list_possibilities_2)
        elif input_field == 2:
            if arr1[1] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr1[1] = self.x_o
                self.occupied_x2 = True
        elif input_field == 3:
            if arr1[2] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr1[2] = self.x_o
                self.occupied_x3 = True
        elif input_field == 4:
            if arr2[0] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr2[0] = self.x_o
                self.occupied_x4 = True
        elif input_field == 5:
            if arr2[1] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr2[1] = self.x_o
                self.occupied_x5 = True
        elif input_field == 6:
            if arr2[2] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr2[2] = self.x_o
                self.occupied_x6 = True
        elif input_field == 7:
            if arr3[0] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr3[0] = self.x_o
                self.occupied_x7 = True
        elif input_field == 8:
            if arr3[1] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr3[1] = self.x_o
                self.occupied_x8 = True
        elif input_field == 9:
            if arr3[2] == self.x_o:
                print("Dieses Feld ist bereits belegt!")
            else:
                arr3[2] = self.x_o
                self.occupied_x9 = True
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

        print(arr1)
        print(arr2)
        print(arr3)


    def remove_possibilities(self, list_possibilities_2, input_field):
        #for i in range(len(list_possibilities_2)):

        #c = False
        #for i in range(len(list_possibilities_2)):
        for i in range(len(list_possibilities_2)):
            # i gibt index zurück
            #arr = []
            #print(list_possibilities_2[i])
            #print(list_possibilities_2[i])
            for j in list_possibilities_2[i]:
                #j gibt value zurück
                #print(j)
                #print(list_possibilities_2[i][j])
                if list_possibilities_2[i][j] == input_field:
                    c = True
                    #print("du arsch")
                    #print(len(list_possibilities_2[i]))
                    #arr = np.append(arr, list_possibilities_2[i])
                    #list_possibilities_2.pop()
                    #print(arr)
                    #np.delete(list_possibilities_2, 0)
                    #list_possibilities_2 = np.delete(list_possibilities_2, )
            if c:
                list_possibilities_2.pop(i)


            print(i)
            #print(list_possibilities_2)
            #print(list_possibilities_2)
            #print(len(list_possibilities_2))
            #print(list_possibilities_2.size)
            #print(arr)
        #for y in range(len(list_possibilities_2)):
         #   if np.array_equal(arr, list_possibilities_2):
          #      np.delete(list_possibilities_2, )