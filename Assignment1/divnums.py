'''Numbers divisible by 9 but not 6 in user range.'''
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    if num % 9 == 0 and num % 6 != 0:
        print(num)