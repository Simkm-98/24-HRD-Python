def compute_mingong(x, y):
    if x > y:
        big = x
    else:
        big = y

    while True:
        if (big % x == 0) and (big % y == 0):
            result = big
            break
        big += 1

    return result

a = int(input("첫번째 수 입력 : "))
b = int(input("두번째 수 입력 : "))
print(f"{a} 와 {b} 의 최대공배수는 : {compute_mingong(a, b)}")
