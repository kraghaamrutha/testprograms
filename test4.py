""" 1. Write a program to add 7000 after 6000 in the following list.
# Sample Input
 list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected Output
 list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]  """
 
l1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
l1[2][2].insert(2,7000)
print(l1)

""" 2. Write a program to count the number of students has computers a one subject from the data given below.
students = [
 	("John", ["Computers", "Physics", “Maths”]), 
	("Wasim", ["Maths", "Computers", "Statistics"]), 
	("Naresh", ["Computers", "Accounting", "Economics"]), 
	("SaiTeja", ["English", "Accounting", "Economics", "Law"]), 
	("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])
	]  """
 

students = [ ("John", ["Computers", "Physics", "Maths"]), 
            ("Wasim", ["Maths", "Computers", "Statistics"]), 
            ("Naresh", ["Computers", "Accounting", "Economics"]), 
            ("SaiTeja", ["English", "Accounting", "Economics", "Law"]), 
            ("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])]
count = 0
for student, subjects in students:
    if "Computers" in subjects:
        count += 1
print(count)

    


""" 3. Write a program to find maximum and the minimum value in a set.
# Input
set1 = {5, 10, 3, 15, 2, 20}
# Expected Output
max = 20
min = 2    """

set1 = {5, 10, 3, 15, 2, 20}
print("max =" , max(set1))
print("min = " , min(set1))