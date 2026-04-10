#==============================================
'''
a = 1
b = 2
ex = 3
c = a+b
d = b - a
e = a * b
f = b / a
g = b // a # 나눗셈 후 소수점 버림
h = b % a # 나누기 후 나머지 값만 저장
i = b ** ex # 거듭제곱
print('='*20)
print(f'a = {a}')
print(f'b = {b}')
print(f'ex = {ex}')
print('='*20)
print(f'a + b = {c}')
print(f'b - a = {d}')
print(f'a * b = {e}')
print(f'b / a = {f}')
print(f'b // a = {g}')
print(f'b % a =  {h}')
print(f'b ** ex =  {i}')
print('='*20)
'''
#==============================================
'''
a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))
c = a+b
print("{} + {} = {}".format(a, b, a+b))
print(f"{a} + {b} = {c}")
'''
#==============================================
'''
a = int(input('첫 번째 정수를 입력하세요 : '))
b = float(input('두 번째 정수를 입력하세요 : '))
print("{} + {} = {}".format(a, b, a+b))
'''
#==============================================
'''
money = int(input('투입한 돈: '))
price = int(input('물건값: '))
num = money-price
FH = num//500
OH = (num%500)//100
print(f'거스름돈: {num}원')
print(f'500원의 갯수: {FH}')
print(f'100원의 갯수: {OH}')
'''
#==============================================
print('안녕하세요?')
name = input('이름이 어떻게 되시나요? ')
print(f'만나서 반갑습니다. {name}씨')
print(f'이름의 길이는 다음과 같군요: {len(name)}')
age = int(input('나이가 어떻게 되시나요? '))
print(f'내년이면 {age+1}이 되시는군요')