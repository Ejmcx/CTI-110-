

#Elijah Mcarthur Burnside
# 10/4/2026
#P2HW1
# Travel Expense

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
print("---------Travel Expenses---------")
print(f"{'Destination:':<25}{destination}")
print(f"{'Total Estimated Expenses:':<25}${total_expenses:>10.2f}")
print(f"{'Food:':<25}${food:>10.2f}")
print(f"{'Accommodation:':<25}${accommodation:>10.2f}")
print(f"{'Gas:':<25}${gas:>10.2f}")
print("---------------------------------")
print(f"{'Remaining Budget:':<25}${remaining_budget:>10.2f}")
