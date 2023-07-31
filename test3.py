# 1:  Write a program to print a string formed with the first 2 and the last 2 characters
# of the given string. Assume the size of given string is always greater than or equal to 4.

string = input("enter a string: ")
if len(string) >= 4:
    res = string[:2] + string[-2:]
    print(res)
else:
    print("error")


# 2: Write a program to check if a word is present in the given string. 
# For example, if the word 'orange' is present in the "This is orange juice".

string = " This is orange juice"
word = 'orange'
if word in string:
    print("word is present" ,word)
else:
    print("word is not present")


# 3: Write a program that will print whether the number is a single digit number or
# double digit number or big number. If given number is one digit number,
# print "Single digit number".
# If given number is two digit number, print "Double digit number". 
# If number is three digit number or bigger, print "Big number".

num = int(input("enter a num: "))
if num < 10:
    print("single digit number")
elif num < 100:
    print("two digit number")
else:
    print("big number")

#  4: Write a program that takes a list and splits into smaller lists of given size.
#  For example, if lst = [1, 2, 3, 4, 5, 6], size = 2, it should return [[1, 2], [3,4], [5,6]]
#  and if lst = [1,2,3,4,5,6,7,8,9], size = 4 then it should return [[1,2,3,4],[5,6,7,8],[9]]. 

def split_list(lst,size):
    for i in range(0,len(lst),size):
        lst1 = [1, 2, 3, 4, 5, 6]
        size1 = 2
        result1 = split_list(lst1,size1)
        print(result1)
        
        lst2 = [1,2,3,4,5,6,7,8,9]
        size2 = 4
        result2 = split_list(lst2,size2)
        print(result2)


# 5: Write a program to print a list with all duplicates in the given list. 
# For example, if lst=[1, 3, 2, 1, 2, 5, 6] it should return [1, 2].

lst=[1, 3, 2, 1, 2, 5, 6]
for i in range(1,7):
    if lst.count(i) == 2:
        print("duplicates in list: ",i,end=" ")


# 8: Write a program to display the elements of list thrice if it is a number and 
# display the element terminated with ‘#’ if it is not a number. For example,
# if the content of list is [‘41’, ‘DHRUVA’, ‘GURU’, ‘13’, ‘ZARA’]
# The output should be
# 414141
# DHRUVA#
# GURU#
# 131313
# ZARA#

lst = ['41', 'DHRUVA', 'GURU', '13', 'ZARA']
result = []
for item in lst:
    if item.isdigit():
        result.append(item * 3)
    else:
        result.append(item + '#')
    print(result)
