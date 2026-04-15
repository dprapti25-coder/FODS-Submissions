'''Calculates Grade based on average of 6 subjects.'''
marks = []
for i in range(6):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total = sum(marks)
avg = total / 6
percentage = avg

if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

print("Total:", total)
print("Average:", avg)
print("Percentage:", percentage)
print("Grade:", grade)