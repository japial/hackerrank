import re

n = int(input())
for l in range(0, n):
    line = input()
    color = re.findall(r".(#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3})", line)
    for code in color:
        print(code)
