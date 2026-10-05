#Elijah Mcarthur Burnside
#10/4/2026
#P2HW2
#Propmt For Grades

#Grade for module 1
module1 = float(input("Enter Your Module 1 Grade: "))
module2 = float(input("Enter Your Module 2 Grade: "))
module3 = float(input("Enter Your Module 3 Grade: "))
module4 = float(input("Enter Your Module 4 Grade: "))
module5 = float(input("Enter Your Module 5 Grade: "))
module6 = float(input("Enter Your Module 6 Grade: "))

Grade = (module1, module2, module3, module4, module5, module6)

#calculate Results
lowest_grade = min(Grade)
Highest_grade = max(Grade)
sum_of_grades = sum(Grade)
average_grade = sum_of_grades / len(Grade) 

#Display Results
print("Lowest Grade: ", lowest_grade)
print("Highest Grade: ", Highest_grade)
print("Sum of Grades: ", sum_of_grades)
print("Average Grade: ", average_grade)