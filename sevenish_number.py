"""
Let's define a "sevenish" number to be one which is either a power of 7, 
or the sum of unique powers of 7. 
The first few sevenish numbers are 1, 7, 8, 49, and so on. 
Create an algorithm to find the nth sevenish number.
"""

def sevenish_number(n):
    list = [1]   #create a list to contain sevenish numbers
    temp_list = []
    multiple_factor = 1  #keep track of current highest power of n
    while len(list) < n:    #add current highest power of n to list
        list.append(7**multiple_factor)
        for number in list[:-1]:    #add the sum of the current highest power of n and all the previous list elements to a temporary list
            if len(list) + len(temp_list) < n:   #check only  elements in list
                temp_list.append(number+7**multiple_factor)
            else:
                break
        list = list + temp_list 
        temp_list = []
        multiple_factor = multiple_factor + 1
    print(list)
    print("The " + str(n) + "th sevenish number is " + str(list[-1]))
    return list[-1]

sevenish_number(5)
