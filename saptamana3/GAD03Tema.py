def your_func(*args, **kwargs):
    result = 0
    for x in args:
        if isinstance(x, int):
            result += x
    return result


def suma0_n(num):
    if not isinstance(num, int):
        return 0
    if num == 0:
        return 0
    return num + suma0_n(num - 1)


def suma0_n_pare(num):
    if not isinstance(num, int):
        return 0
    if num == 1:
        return 1
    if num % 2 == 0:
        return num + suma0_n(num - 2)
    else:
        return num - 1 + suma0_n(num - 3)


print(your_func(2, 4, "abc", param_1=2))
print(suma0_n(5))
print(suma0_n_pare(50))
