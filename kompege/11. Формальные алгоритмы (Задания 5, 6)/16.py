max_d = float('-inf')
min_d = float('inf')
for i in range(1000):
    d = i
    n = 1
    while d // n > 0:
        d = d - 2
        n = n + 3
    if n == 46:
        min_d = min(min_d, i)
        max_d = max(min_d, i)

print(max_d + min_d)
