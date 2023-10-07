n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    try:
        question, answer = input().split()
        question_numbers = set(map(int, question.split()))

        if answer == 'YES':
            possible_numbers.intersection_update(question_numbers)
        else:
            possible_numbers.difference_update(question_numbers)
    except EOFError:
        break

print(*sorted(possible_numbers))
