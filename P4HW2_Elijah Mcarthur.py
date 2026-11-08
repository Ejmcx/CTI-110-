#Elijah Mcarthur
#11/7/2026
#PH4W2
#Salary Calculator

# request employee info
name = input("Enter employee's name or 'done' to finish: ")

# Create accumulator variables for overtime pay, regular pay, gross pay and employee count
overtime_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    # add employee count plus 1
    employee_count += 1

    # asked for employee info
    hours = float(input(f"How many hours did {name} work this week? "))
    rate = float(input(f"What is {name}'s hourly pay rate? "))

    # evaluate overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    # Add to accumulator totals
    overtime_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display results for this employee
    print("---------------------------------")
    print("Employee Name:", name)
    print(f"Hours Worked: {hours:<15} Pay Rate: {rate:<12} Overtime Hours: {overtime_hours:<15} Overtime Pay: {overtime_pay:<15} Regular Pay: {regular_pay:<15} Gross Pay: {gross_pay:<12}")
    print("---------------------------------")

    name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: $", format(overtime_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))