n = int(input())
arr = map(int, input().split())
sorted_set = sorted(set(arr))
print(sorted_set[-2])