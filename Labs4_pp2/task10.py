N, K = map(int, input().split())

strike_days = [0] * N

for i in range(K):
    a, b = map(int, input().split())
    for day in range(a - 1, N, b):
        strike_days[day] = 1

total_strikes = sum(strike_days)

print(total_strikes)