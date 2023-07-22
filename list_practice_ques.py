""" 1: Write a program that uses list and range to create the list [3,6, 9, . . . , 99] ."""
l = []
for  i in range(3,100,3):
    l.append(i)
print(l)

""" 2: Write a program to convert a list of characters into a single string.
# Sample Input
 ['a', 'b', 'c', 'd']
# Expected Output
 abcd  """
l = ['a','b','c','d']
s = ''.join(l)
print(s)

for x in l:
    print(x,end='')


""" 3: Write a program to read a string from the user and print the list of characters in the string.
# Sample Input
 abcd
# Expected Output
 ['a', 'b', 'c', 'd']"""
l = "abcd"
print(list(l))



""" 5: Write a Python program to find common items from two lists.
# Sample Input
 color1 = ["Red", "Green", "Orange", "White"]
 color2 = ["Black", "Green", "White", "Pink"]
# Expected Output
 ['Green', 'White']
 """
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
l = []
for i in color1:
    if i in color2:
        l.append(i)
print(l)


"""
 5: Write a Python program to get the difference between the two lists.
# Sample Input
 list1 = [1, 2, 3, 4]
 list2 = [1, 2]
# Expected Output
 [3,4]
"""
list1 = [1, 2, 3, 4]
list2 = [1, 2]
l = []
for i in list1:
    if i not in list2:
        l.append(i)
print(l)


""" 6: Write a Python program to get the largest number from a list.
# Sample Input
 list1 = [1, 2, -8, 0]
# Expected Output
 2  """
l = [1,2,-8,0]
print(max(l))
l.sort()
print("largest number" ,l[-1])


""" 7: Write a Python program to find the second smallest number in a list.
# Sample Input
 list1 = [1, 2, -8, -2, 0]
# Expected Output
 -2  """
l = [1, 2, -8, -2, 0]
l.sort()
print("smallest number", l[1])


""" 8: Write a Python program to remove duplicates from a list.
# Sample Input
 list1 = [10,20,30,20,10,50,60,40,80,50,40]
# Expected Output
 [10, 20, 30, 50, 60, 40, 80] """
l = [10,20,30,20,10,50,60,40,80,50,40]
l1 = []
for  i in l:
    if i not in l1:
        l1.append(i) 
print(l1)
print(list(set(l)))


""" 9: Write a Python program to sum all the items in a list.
# Sample Input
 list1 = [1, 2, -8]
# Expected Output
 -5 """
l = [1, 2, -8]
s = 0
for i in l:
    s += i
print("sum of number" ,s)
print(sum(l))



""" 10: Write a Python program to multiply all the items in a list.
# Sample Input
 list1 = [1, 2, 3, 4]
# Expected Output
 24  """
l = [1, 2, 3, 4]
m = 1
for i in l:
    m *= i
print("multiply of list" ,m)



""" 11: Write a program to find difference between sum of even indexed and odd indexed numbers in a list of numbers. 
[Note:- Consider 0th index as even indexed]
# Sample Input
 list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# Expected Output
 -10
"""
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
even = sum(list1[::2])
odd = sum(list1[1::2])
print(even - odd)


"""
    12: Write a program to print the list of numbers which are greater than the average of numbers in the following list.
# Sample Input
 list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# Expected Output
 [9, 13, 12, 7]
"""
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
avg = sum(list1)/len(list1)
l = []
for i in list1:
    if i > avg:
        l.append(i)
print(l)




""" 13: Write a program to print a new list containing squares of each element in the following list.
# Sample Input
 list1 = [3, 7, 11, 12, 17, 21]
# Expected Output
 list2 = [9, 49, 121, 144, 289, 441] """
l = [3, 7, 11, 12, 17, 21]
l1 = []
for i in l:
    l1.append(i**2)
print(l1)
    


""" 14: Write a program to know how many times an element occurred in the list.
# Sample Input
 list1 = [5, 10, 15, 20, 25, 50, 20]
 element = 20 # Expected Output
 2  """
l = [5, 10, 15, 20, 25, 50, 20]
print(l.count(20))
c = int(input("enter c: "))
print(l.count(c))



""" 15: Given a Python list, write a program to find the value 20 in the list, and if it is present, 
replace the first occurrence of a value with 200.
# Sample Input
 list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected Output
 list1= [5, 10, 15, 200, 25, 50, 20] """
l = [5, 10, 15, 20, 25, 50, 20]
l[3] = 200
print(l)



"""
    17: Two lists are given below. Write a program to create a third list by picking an odd-index 
    element from the first list and even index elements from second.
# Sample Input
 list1 = [3, 6, 9, 12, 15, 18, 21]
 list2 = [4, 8, 12, 16, 20, 24, 28]
# Expected Output
 list3 = [6, 12, 18, 4, 12, 20, 28]
"""
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
odd_l1 = list1[1::2]
even_l2 = list2[::2]
odd_l1.extend(even_l2)
print(odd_l1)



""" 18: Write a program to add 7000 after 6000 in the following list.
# Sample Input
 list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected Output
 list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40] """
l1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
l1[2][2].insert(2,7000)
print(l1)


#### ------ lists pdf -------

""" 1. Write a program that accepts a list from the user and print the alternate element of the list."""
l = []
num = int(input("enter no of iterations: "))
for i in range(num):
    n = int(input("enter n: "))
    l.append(n)
print(l)
print(l[::2])



""" 2. Write a program that accepts a list from the user. 
Your program should reverse the content of the list and print it. 
Do not use the reverse() method."""
l = []
num = int(input("enter no of iterations: "))
for i in range(num):
    n = int(input("enter n: "))
    l.append(n)
print(l)
print(l[::-1])



""" 3. Find and display the largest number of a list without using built-in function max(). """
l = []
num = int(input("enter no of iterations: "))
for i in range(num):
    n = int(input("enter n: "))
    l.append(n)
    l.sort()
print(l)
print("largest number is",l[-1])














    
    




