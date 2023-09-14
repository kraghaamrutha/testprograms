""" 1. Write a program to remove all punctuations/symbols from a given string.
Input: Hello!!!, how are you? -Hope it's going well.
Expected Output: Hello how are you Hope its going well """

input_string = "Hello!!!, how are you? -Hope it's going well."
str = ""
for i in input_string:
    if i.isalpha() or i.isspace():
        str += i
print(str)


    
 

""" 2. Write a program that prompts the user to input a number and reverse its digits. 
For example, the reverse of 12345 is 54321; reverse of 5600 is 65. """

num = int(input("enter num: "))
rev = 0
while num > 0:
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10
print(rev)



""" 3. Write a program to return the number of negative numbers in the given list.
Sample Input: [5, -1, -2, 0, 3]
Expected Output: 2 """

list = [5, -1, -2, 0, 3]
negative_count = 0
for number in list:
    if number < 0:
        negative_count += 1
print(negative_count)


"""  4. Write a program to find the sum of the cube of elements in a list. The list is received as
an argument and it should return the sum."""

list = [2,3,5,7,9]
sum_cube_elements = 0
for number in list:
    sum_cube_elements += number ** 3
print(sum_cube_elements)


