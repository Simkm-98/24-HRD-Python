def max_two(i, j):
    if i > j:
        return i
    else:
        return j

def max_three(x, y, z):
    return max_two(max_two(x, y), max_two(y,z))

a = int(input("첫번째 수를 입력 : "))
b = int(input("두번째 수를 입력 : "))
c = int(input("세번째 수를 입력 : "))
max_num = max_three(a, b, c)

print(f"{a}, {b}, {c} 중 가장 큰 수는 : {max_num}")