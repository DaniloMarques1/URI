tot = int(input())
p = list(map(int, input().split()))

print(p.index(min(p)) + 1)