

#Elijah Mcarthur Burnside
# 9/19/2026
#P1HW2
# Budgeting trip

budget = float(input("Enter your budget for the trip: "))
destination = input("Enter the travel destination: ")
accommodation = float(input("enter the estimated cost of accommodation: "))
food = float(input("enter the estimated cost of food: "))
gas = float(input("enter the estimated cost of gas: "))

#Calculate the total estimated cost of the trip
total_expenses = gas + accommodation + food

# subtract all expenses from the budget to determine if the trip is within the budget

remaining_budget = budget - total_expenses

#Display the results
print("---------Trip Budget Summary---------")
print("Destination:", destination)  
print("Total Estimated Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)
