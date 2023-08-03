""" 1: Print all Pairs which make sum N for the given list.
e,g: l = [4, 3, 6, 8, 2, 9, 7,  5]
N = 10,
It should print (4, 6), (8, 2), (3, 7)   """

l =  [4, 3, 6, 8, 2, 9, 7,  5]
n = 10
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == n:
            print((l[i],l[j]),end=" ")


""" 2. 
10
10 9
10 9 8
10 9 8 7
10 9 8 7 6  """

for i in range(1,6):
    for j in range(10,10-i,-1):
        print(j,end=" ")
    print()


""" 3:  Merge the following lists
given 
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
output = [1, 3, 4, 7, 8, 9, 10]  """

l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
l1.extend(l2)
l1.sort()
print(l1)


""" 4: sort the following list without using sort() function
[1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]  """
