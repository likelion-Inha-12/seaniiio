def func(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = ((d ** 0.5) - b) / (2 * a)
        x2 = ((-1) * (d ** 0.5) - b) / (2 * a)
        print(x1, x2)
    elif d == 0:
        print("중근을 갖습니다.")
    else:
        print("근이 존재하지 않습니다.")