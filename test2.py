" 1. What is the output of the following python code?"
print(1,2,3,4,sep='#',end='&')
# output : 1#2#3#4&


" 2nd : Which is the only string that Python considers as False when converting to boolean?"
s = ""
print(bool(s))
output = "empty Syntax" 

"3: What would be the output of this code if the user tried to enter 3 in the console? "
# choice = int(input('pick a number: '))
# if choice == 3:
#     print('good choice')
# else:
#     print('you could have chosen better')
# else:
#     print('no luck this time')

output = "error because here 2 else statements are there"
  

"""4. Given the following program:
answer_a = int(input('Try to guess the first number: '))
if answer_a == 8:
answer_b = int(input('Correct! Now, guess the second number: '))
if answer_b == 5:
print('You won!')
else:
print('You only got one number right. So close!')
else:
print('Wrong!')
What will happen when the user enters 8 and then 3?
"""
output = "Correct! Now, guess the second number: 3 , You only got one number right. So close!"


"""5. Write a python program to calculate and print out the average of a set of integers
"""
# num = int(input("enter num: "))
# num_res = num.split()
# print(sum(num_res))

# """ 6:  Write a python program to check whether the given integer is a multiple of 5."""
num = int(input("enter a integer: "))
if num % 5 == 0:
    print(num,"is multiple of 5")
else:
    print(num,"is not multiple of 5")
    
    
    
" 7:  slicing"  
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(ALPHABET[7:9])
print(ALPHABET[-3:-1])
print(ALPHABET[:3])
print(ALPHABET[-1:])
print(ALPHABET[14:-12])
print(ALPHABET[1:-1])
print(ALPHABET[0:5:2])
print(ALPHABET[::-1])
print(ALPHABET[5:2:-1])
print(ALPHABET[14:10:-2])

"8: 8. Write a program to replace whitespace with hyphen in any given string"
text = input("enter a text: ")
print(text.replace(" ","-"))

"""9. Consider an amusement park that charges different rates for different age groups:
● Admission for anyone under age 4 is free.
● Admission for anyone between the ages of 4 and 18 is Rs. 25.
● Admission for anyone age 18 or older is Rs. 40.
Write a program to print the admission price message."""
age = int(input("enter age: "))
if age <= 4  :
   print("Free")
elif age > 4 and age < 18:
    print("Amusement park charges Rs: 25")
else:
    print("Amusement park charges Rs: 40")