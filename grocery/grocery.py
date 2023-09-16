list = {}

while True:
    try:
        key = input().upper()
        if key in list:
            list[key] += 1
            continue
        else:
            list[key] = 1
            continue
    except EOFError:
        print()
        sort_list = sorted(list)
        for key in sort_list:
            print(list[key],key)
    break