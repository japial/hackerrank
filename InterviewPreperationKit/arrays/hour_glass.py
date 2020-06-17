def hour_glass(arr):
    max_sum = -2147483648
    temp_sum = 0
    for i in range(6):
        for j in range(6):
            if j + 2 < 6 and i + 2 < 6:
                temp_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]+ arr[i + 2][j + 2]
                if temp_sum >= max_sum:
                    max_sum = temp_sum
            j += 1
        i += 1

    return max_sum


arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hour_glass(arr))
