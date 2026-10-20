
# Elijah Mcarthur
# 10/19/2026
# P3HW2 - Salary Calculator

# Get employee information
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))

# Calculate regular and overtime pay
if hours > 40:
    overtime_hours = hours - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours

# Calculate pay
overtime_pay = overtime_hours * (rate * 1.5)
regular_pay = regular_hours * rate
gross_pay = regular_pay + overtime_pay

# Display results
print("-----------------------------------------------")
print(f"Employee name:    {name}")
print()
print(f"{'Hours Worked':<16}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay'}")
print("-" * 100)
print(f"{hours:<16.1f}{rate:<12.1f}{overtime_hours:<12.1f}${overtime_pay:<19.2f}${regular_pay:<19.2f}${gross_pay:.2f}")
