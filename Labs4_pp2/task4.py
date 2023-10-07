unique_numbers = set()

numbers = input().split()

for number in numbers:
    if number in unique_numbers:
        print("YES")
    else:
        unique_numbers.add(number)
        print("NO")
