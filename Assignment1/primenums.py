'''Finds primes in a range, their count, and sum.'''
start = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0
total = 0

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            count += 1
            total += num

print("Count:", count)
print("Sum:", total)