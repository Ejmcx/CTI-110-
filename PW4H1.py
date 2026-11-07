#Elijah Mcarthur
#11/7/2026
#P4HW1


# PSEUDOCODE:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store valid scores.
# 3. Repeat for the number of scores requested.
# 4. Ask the user to enter a score.
# 5. Check if the score is between 0 and 100.
# 6. If invalid, display an error and ask again.
# 7. If valid, add the score to the list.
# 8. Find and display the lowest score.
# 9. Remove the lowest score from the list.
# 10. Calculate the average of the remaining scores.
# 11. Determine the letter grade.
# 12. Display the results.

# Ask how many scores the user wants to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list for scores
scores = []

# Collect scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    # Validate the score
    while score < 0 or score > 100:
        print("Invalid score.")
        print("Score should be between 0 and 100.")
        score = float(input(f"Enter score #{i + 1} again: "))

    # Add valid score to the list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

print("\nLowest score:", lowest_score)

# Create a modified list without the lowest score
scores.remove(lowest_score)

print("Score list after dropping lowest score:", scores)

# Calculate the average
average = sum(scores) / len(scores)

print(f"Average score: {average:.2f}")

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display letter grade
print("Letter grade:", grade)
