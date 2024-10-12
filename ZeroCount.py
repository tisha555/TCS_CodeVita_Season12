first, sec = map(int, input().split())

if sec == 0:
    print(first)
else:
    ans = first - sec
    result = ans // (sec + 1)
    if ans % (sec + 1) != 0:
        result += 1
    print((result), end = '')
