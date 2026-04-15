'''Calculates separate sums using a loop until user exits'''
pos_sum = 0
neg_sum = 0

while True:
    num = int(input("Enter number: "))
    
    if num > 0:
        pos_sum += num
    else:
        neg_sum += num

    choice = input("Continue? (y/n): ")
    if choice.lower() == 'n':
        break

print("Positive sum:", pos_sum)
print("Negative sum:", neg_sum)