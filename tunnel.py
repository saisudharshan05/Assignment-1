import os.path
import sys
from collections import deque

def Get_Visibility_West(UpArray, DownArray, Present_Up, Present_Down):
    Visibility_lenth = 1
    for i in range(1, len(UpArray)):
        if Present_Up <= UpArray[i] and DownArray[i] <= Present_Down:
            Visibility_lenth = Visibility_lenth + 1
        else:
            Left_Wall = i
            break
    return [Visibility_lenth, Left_Wall]

def Create_Matrix(UpArray, DownArray):
    M_cols = len(UpArray)
    max_UpArray = max(UpArray)
    #min_DownArray = min(DownArray)
    M_rows = max_UpArray + 1 #- min_DownArray + 1
    M = [[0 for x in range(M_cols)] for y in range(M_rows)]
    #Now fill the existing data into M with UpArray
    for i in range(len(UpArray)):
        x = UpArray[i]
        for j in range(M_rows - x):
            M[j][i] = 1
        y = DownArray[i]
        for j in range(y):
            M[M_rows - j-1][i] = 1
    #Fill west with -1 amd east with -1
    for i in range(M_rows):
        if M[i][0] == 0:
            M[i][0] = -1
        if M[i][M_cols-1] == 0:
            M[i][M_cols-1] = -1
   
    return M
def GetInnerVisibility(M, UpArray, DownArray):
    M_cols = len(UpArray)
    max_UpArray = max(UpArray)
    #min_DownArray = min(DownArray)
    M_rows = max_UpArray +1 #- min_DownArray + 1
    s_length = 0
    L = {}
    L1 = []
    #print()
    #for i in range(max(UpArray) + 1):
    #   print(M[i])
    for i in range(M_rows):
        #Scanning through the row to get consecutive zeros
        s_length = 0
        for j in range(M_cols):
            if (M[i][j] == 0):
                s_length = s_length + 1
            else:
                if s_length > 0:
                    if M[i][j] == -1:
                        s_length = s_length + 1
                    L1.append(s_length)
                s_length = 0
        if M[i][0] == -1:
            L1.pop(0)
        L[i] = L1
        L1 = []
    return L
try:
    TunnelFile = input("Enter Tunnel File Name: ").strip()
except FileNotFoundError:
    print("File doesn't exist. Enter valid filename.")
    sys.exti()
   
try:
    with open(TunnelFile) as tFile:
        No_of_Lines = 0
        InputList = []
        for line in tFile:
            line1 = line.rstrip()
            if len(line1) != 0:
                No_of_Lines = No_of_Lines + 1
                InputList.append(line1)
    #print(InputList)
    if (No_of_Lines != 2):
        print("The file has more than two lines of data.")
        raise ValueError
    UpArray = []
    DownArray = []
    UpArray = [int(x) for x in InputList[0].split()]
    DownArray = [int(x) for x in InputList[1].split()]
    #print(UpArray)
    #print(DownArray)
   
    if len(UpArray) < 2:
        print("Tunnel heights must have atleast two integers.")
        raise ValueError
    if len(DownArray) < 2:
        print("Tunnel depths must have atleast two integers.")
        raise ValueError
    if len(DownArray) != len(UpArray):
        print("Number of Tunnel heights and depths must match.")
        raise ValueError
    for x,y in zip(UpArray, DownArray):
        if x <= y:
            print("Tunnel height must be greater than depth at a point.")
            raise ValueError
    #checking the distance of visibility from west
    Present_Up = UpArray[0]
    Present_Down = DownArray[0]
    #dist = Present_Up - Present_Down
    Visibility_lenth = 0
    left_wall = 0
    for x in range(UpArray[0], DownArray[0] , -1):
        Present_Up = x
        Present_Down = Present_Up - 1
        R = []
        R = Get_Visibility_West(UpArray, DownArray, Present_Up, Present_Down)
        if (Visibility_lenth < R[0]):
            Visibility_lenth = R[0]
        if (left_wall < R[1]):
            left_wall = R[1]
   
    print(f'The distance over which once can see into the tunnel when looking outside the tunnel from the west is: {Visibility_lenth}')
   
   
    M = Create_Matrix(UpArray, DownArray)
    for i in range(max(UpArray) + 1):
        print(M[i])
    Inner_Visibility = GetInnerVisibility(M, UpArray, DownArray)
    print(Inner_Visibility)
    Visibility_lenth = 0
    for i, j in Inner_Visibility.items():
        if len(j) != 0:
            if Visibility_lenth < max(j):
                Visibility_lenth = max(j)
    print(f'The maximum distance over which one can see into tunnel when being inside the tunnel is {Visibility_lenth}')
except ValueError:
    print("Invalid Input data.")
    sys.exit()