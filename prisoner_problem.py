'''
There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

'''

def prisoner(N,k):

    prisoners = list(range(1,N+1))
    print(prisoners)
    order = []
    index = -1

    while len(order) < N:
        index = index + k   #cycle through multiplws of k
        if index < len(prisoners):
            order.append(prisoners[index])
            prisoners.remove(prisoners[index])
            index = index - 1 #correct index for the fact current index has been deleted
        elif index >= len(prisoners): # circle back on self
            while index >= len(prisoners):
                index = index - len(prisoners)
            order.append(prisoners[index])
            prisoners.remove(prisoners[index])
            index = index - 1 #correct index for the fact current index has been deleted
    print(order)

    return order[-1]

print(prisoner(9,3))
print(prisoner(5,2))

        




