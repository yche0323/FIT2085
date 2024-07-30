def cal(a: int) -> int:
    if a == 0:
        return a
    else:
        a -= 1
        return cal(a)


print(cal(3))
