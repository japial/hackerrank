n = int(input())
list_item = []
for _ in range(n):
    line = input().split()
    command = line[0]
    items = line[1:]
    if command != "print":
        command += "(" + ",". join(items) + ")"
        eval("list_item."+command)
    else:
        print(list_item)
