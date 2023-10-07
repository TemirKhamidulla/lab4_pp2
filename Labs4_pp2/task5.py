N, M = map(int, input().split())

colors_ani = set()
colors_borya = set()

for i in range(N):
    color = int(input())
    colors_ani.add(color)

for i in range(M):
    color = int(input())
    colors_borya.add(color)

common_colors = colors_ani.intersection(colors_borya)

colors_only_ani = colors_ani.difference(colors_borya)

colors_only_borya = colors_borya.difference(colors_ani)

print(len(common_colors))
print(*sorted(common_colors))

print(len(colors_only_ani))
print(*sorted(colors_only_ani))

print(len(colors_only_borya))
print(*sorted(colors_only_borya))
