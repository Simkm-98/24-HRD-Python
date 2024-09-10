# 소비형 함수
# Consumer function

def function(param_name):
    result = param_name + 10
    print(result)

function(param_name=10)

# 생산형 함수
# Supplier

def supply_function() -> int:
    sum = 10 + 20
    print(sum)
    return sum

result = supply_function()
print(result)

# 함수형
# functional

def functional_function(param: int) -> int:
    result  = param + 1000
    return result

result = functional_function(param=100)
print(result)

# show, display function
def show_function():
    print("잔액 : 2000원")
    print("계좌 : 2090-10-222")
    print("계좌 입금 불가능")
    print("계좌 출금 불가능")

show_function()


def swaping_values(value1: int, value2: int) -> tuple:
    return (value2, value1)

result = swaping_values(1_234, 4_321)
print(result)