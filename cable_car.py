import os.path
import sys

from collections import defaultdict

def Check_Perfectride_getGoodRide(CC_master):
    car_diff = []
    perfect_ride = True
    for i in range(len(CC_master) - 1):
        car_diff.append(CC_master[i+1] - CC_master[i])
    for i in range(len(car_diff) - 1):
        if car_diff[i] != car_diff[i+1]:
            perfect_ride = False
    if perfect_ride == True:
        print("The given structure makes up for a perfect ride.")
        print("The length of the longest good ride is ",len(car_diff))
        print("The number of pillers to be removed to build a perfect ride is 0.")
    else:
        print("The given structure does not make up for a perfect ride.")
        p_ride = []
        From = []
        To = []
        #print(car_diff)
        present_diff = car_diff[0]
        f = 0
        temp = []
        temp.append(present_diff)
        for i in range(1,len(car_diff)):
            next_diff = car_diff[i]
            n = i
            if present_diff == next_diff:
                temp.append(next_diff)
                present_diff = next_diff 
            else:
                p_ride.append(temp)
                From.append(f)
                To.append(n)
                temp = []
                present_diff = next_diff
                temp.append(present_diff)
                f = n
                if i == len(car_diff)-1:
                    p_ride.append(temp)
                    From.append(f)
                    To.append(n)
                    break         
        #print(p_ride)
        #print(From)
        #print(To)
        longest_good_ride = 0
        for i in range(len(p_ride)):
            if len(p_ride[i]) > longest_good_ride:
                longest_good_ride = len(p_ride[i])
                f = From[i]
                t = To[i]
        print(f'The longest good ride is between the piller of height {CC_master[f]} and the piller of height {CC_master[t]}. It has a length of {longest_good_ride}.')
        
        #Removing pillers to get a Perfect ride
        dict_perfect_ride = {}
        car_diff_unique = []
        for x in car_diff:
            if x not in car_diff_unique:
                car_diff_unique.append(x)
        for x in car_diff_unique:
            dict_perfect_ride[x] = []
        M = max(CC_master)
        for x in car_diff_unique:
            #pass through the original pillars data and check for difference
            present_pillar = CC_master[0]
            temp = []
            y = 1
            #for y in range(1,len(CC_master)):
            while y < len(CC_master):
                next_pillar = CC_master[y]
                if next_pillar - present_pillar == x:
                    temp.append(present_pillar)
                    temp.append(next_pillar)
                    #present_pillar = next_pillar
                    while next_pillar < M+1:
                        z = next_pillar + x
                        y = y + 1
                        if z in CC_master:
                            temp.append(z)
                            next_pillar = z
                        else:
                            break
                    dict_perfect_ride[x].append(temp)
                    present_pillar = next_pillar
                else:
                    temp = []
                    #present_pillar = next_pillar
                    y = y + 1
        print(dict_perfect_ride)
        M = 0
        x_position = 0
        y_position = 0
        temp1 = 0
        for i,j in dict_perfect_ride.items():
            temp1 = i
            temp = 0
            for k in j:
                if len(k) > M:
                    M = len(k)
                    x_position = temp1
                    y_position = temp
                temp = temp + 1
        #print(M, x_position, y_position)
        #print(dict_perfect_ride[x_position][y_position])
        perfect_ride = dict_perfect_ride[x_position][y_position]
        removed_pillars = []
        removed_pillars_count = 0
        for i in CC_master:
            if i not in perfect_ride:
                removed_pillars.append(i)
                removed_pillars_count = removed_pillars_count + 1
        print(f'{removed_pillars_count} pillars to be removed to build a perfect ride.')
        #print(f'The removed pillars are {removed_pillars}')
                    

try:
    cable_car_file = input('Enter the cable car input filename: ')
    FN = open(cable_car_file)
except FileNotFoundError:
    print('File does not exist. Enter valid existing filename.')
    sys.exit()

CC_master = []
CC_temp = []
try:
    #Opening the cable car file and reading line by line and splitting values and storing in list CC_temp
    #CC_master will have all the car positions, as given in the file
    #with open(cable_car_file) as FN:
    for line in FN:
        CC_temp = list(int(x) for x in line.split())
        if len(CC_temp) > 0:
            CC_master.extend(CC_temp)
    #print(CC_master)
    #Checking that the number of car positions are atleast 2
    if len(CC_master) < 2:
        raise ValueError
    positive_nums = 0
    #Checking that there exists minimum 2 positive car positions and no position is 0
    zero_encountered = False
    for x in CC_master:
        if x == 0:
            zero_encountered = True
            break
        if x > 0:
            positive_nums = positive_nums + 1
    if zero_encountered == True:
        raise ValueError
    if positive_nums < 2:
        raise ValueError
    #Checking the increasing order of car position values
    for i in range(len(CC_master) - 1):
        if CC_master[i] > CC_master[i+1]:
            raise VaueError
    #Taking the diffrence of adjacent car positions and storing it in a list
    Check_Perfectride_getGoodRide(CC_master)
    
    
except ValueError:
    print("File must have at least 2 positive non-zero integers and must be in increasing order.")
    sys.exit()