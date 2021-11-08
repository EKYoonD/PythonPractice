n, m = map(int, input().split())
min_data = 0

for i in range(n):
    data = list(map(int, input().split()))
    if min_data < min(data):
        min_data = min(data)
    # min_data = max(min_data, min(data)) 하는 방법도 있음 -> 더 큰걸 return 해주니까

print(min_data)