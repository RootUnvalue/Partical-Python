#24
def sum_num(a, b):
    '''a, b 두 개의 매게변수를 받고 합을 반환하는 함수'''
    return a + b

def sub_num(a, b):
    '''a, b 두 개의 매게변수를 받고 차를 반환하는 함수'''
    return a - b

def div_num(a, b):
    '''a, b 두 개의 매게변수를 받고 나눗셈 결과를 반환하는 함수'''
    return a / b

def mul_num(a, b):
    '''a, b 두 개의 매게변수를 받고 곱을 반환하는 함수'''
    return a * b

a, b = map(int, input('두 수를 입력하세요: ').split())
print(a, ' + ', b, ' = ', sum_num(a, b))
print(a, ' - ', b, ' = ', sub_num(a, b))
print(a, ' / ', b, ' = ', div_num(a, b))
print(a, ' * ', b, ' = ', mul_num(a, b))

print()
print(sum_num.__doc__)
print(sub_num.__doc__)
print(div_num.__doc__)
print(mul_num.__doc__)
