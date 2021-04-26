import sys

def MOP_case1(SuperPower_Heros, nb_of_switches):
    positive_nums = [i for i in SuperPower_Heros if i>=0]
    negative_nums = [i for i in SuperPower_Heros if i<0]
    positive_nums.sort()
    negative_nums.sort()

    maximum_overall_power = 0
    #print(positive_nums,negative_nums)
    if nb_of_switches < len(negative_nums):
        for i in range(nb_of_switches):
            maximum_overall_power = maximum_overall_power + (-1)*negative_nums[i]
        for j in range(len(negative_nums) - nb_of_switches):
            maximum_overall_power = maximum_overall_power + negative_nums[j+nb_of_switches]
        for k in positive_nums:
            maximum_overall_power = maximum_overall_power + k
    if nb_of_switches == len(negative_nums):
        for i in range(nb_of_switches):
            maximum_overall_power = maximum_overall_power + (-1)*negative_nums[i]
        for k in positive_nums:
            maximum_overall_power = maximum_overall_power + k

    if nb_of_switches > len(negative_nums):
        for i in range(len(negative_nums)):
            maximum_overall_power = maximum_overall_power + (-1)*negative_nums[i]
        remaining = nb_of_switches - len(negative_nums)
        if remaining%2 == 0:
            for x in positive_nums:
                maximum_overall_power = maximum_overall_power + x
        if remaining%2 != 0:
            for i in range(len(positive_nums)):
                if i == 0:
                    maximum_overall_power = maximum_overall_power + (-1)*positive_nums[i]
                else:
                    maximum_overall_power = maximum_overall_power + positive_nums[i]

    print(maximum_overall_power)

def MOP_case2(SuperPower_Heros, nb_of_switches):
    positive_nums = [i for i in SuperPower_Heros if i>=0]
    negative_nums = [i for i in SuperPower_Heros if i<0]
    positive_nums.sort()
    negative_nums.sort()

    maximum_overall_power = 0
    #print(positive_nums,negative_nums)
    if nb_of_switches < len(negative_nums):
        for i in range(nb_of_switches):
            maximum_overall_power = maximum_overall_power + (-1)*negative_nums[i]
        for j in range(len(negative_nums) - nb_of_switches):
            maximum_overall_power = maximum_overall_power + negative_nums[j+nb_of_switches]
        for k in positive_nums:
            maximum_overall_power = maximum_overall_power + k
    if nb_of_switches == len(negative_nums):
        for i in range(nb_of_switches):
            maximum_overall_power = maximum_overall_power + (-1)*negative_nums[i]
        for k in positive_nums:
            maximum_overall_power = maximum_overall_power + k

    if nb_of_switches > len(negative_nums):
        for i in range(len(negative_nums)):
            maximum_overall_power = maximum_overall_power + (-1)*negative_nums[i]
        remaining = nb_of_switches - len(negative_nums)
        #if remaining < len(positive_nums):
        for i in range(remaining):
            maximum_overall_power = maximum_overall_power + (-1)*positive_nums[i]
        for i in range(len(positive_nums) - remaining):
            maximum_overall_power = maximum_overall_power + positive_nums[i+remaining]            
    print(maximum_overall_power)    

def MOP_case3(SuperPower_Heros, nb_of_switches):
    length = []
    for i in range(len(SuperPower_Heros) - nb_of_switches + 1):
        temp = SuperPower_Heros.copy()
        s = 0
        for j in range(nb_of_switches):
            temp[j + i] = (-1)*temp[j + i]
        for k in range(len(temp)):
            s = s  + temp[k]
        length.append(s)
    #print(max(length))
    return max(length)
    
def MOP_case4(SuperPower_Heros):
    length = []
    for i in range(len(SuperPower_Heros)):
        length.append(MOP_case3(SuperPower_Heros, i))
    print(max(length))


try:
    SuperPower_Heros = [int(x) for x in input('Enter integers: ').split()]
    if not SuperPower_Heros:
        raise ValueError
except ValueError:
    print('Incorrect input. Enter negative/positive intergers only.')
    sys.exit()
Heros_count = len(SuperPower_Heros)

try:
    nb_of_switches = int(input("Enter a non-negative integer: "))
    if nb_of_switches < 0:
        raise ValueError
    if nb_of_switches > Heros_count:
        raise ValueError
except ValueError:
    print('Incorrect input. Enter integer greater than 0 and less than ', Heros_count)
    sys.exit()
    
MOP_case1(SuperPower_Heros, nb_of_switches)
MOP_case2(SuperPower_Heros, nb_of_switches)
print(MOP_case3(SuperPower_Heros, nb_of_switches))
MOP_case4(SuperPower_Heros)