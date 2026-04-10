'''
정통과 이민수
'''

#(예제1)=======================
'''
for i in range(5): # range(start = 0, stop, step = 1)(미설정 시 기본값)
    print(f'{i+1}번째 반복됨')
'''
#(예제2)=======================
'''
for i in range(1, 6, 1):
    print(i,"\n",end= "")
'''
#(예제3)=======================
'''
num = int(input('점수를 입력하시오:\t'))
sum = 1
i = 0
for i in range(1, num+1):
    sum = sum*i
print(f'{num}! 값은 {sum}입니다.')
'''
#(예제4)=======================
'''
MPW = 'A1234'
a = 0
while a != 1:
    PW = input("비밀번호를 입력하시오: ")
    if PW == MPW:
        print('로그인 성공')
        a = 1
    else:
        print('로그인 실패')
        a = 0
'''
#(예제5)=======================
'''
count = 1
s = 0
while count <= 10:
    s = s+count
    count = count+1
print(s)
'''
#(예제6-1)=======================
'''
x = 1
y = 0
while x < 10:
    y = y + 1
    if y==10:
        x = x + 1
        y = 1
    if x == 10:
        break
    print(f'{x} * {y} = {x*y}')
'''
#(예제6-2)=======================
'''
dan = int(input('원하는 단을 입력하시오: '))
i = 1
while i <= 9:
    print(f'{dan}*{i}={dan*i}')
    i = i+1
'''
#(예제7)=======================
'''
import random as r
while True:
    rn1 = r.randrange(10)
    rn2 = r.randrange(10)
    rnsum = rn1 + rn2
    answer = int(input(f'{rn1} + {rn2} = '))
    if answer != rnsum:
        print(f'오답. 정답은 {rnsum}입니다.')
    else:
        print('정답입니다.')
'''

'''
Trt = 'Green'
out = 0
while out == 1:
    answer = input('색상을 입력하시오: ')
    if answer == Trt:
        out = 1
    else:
        out = 0
'''
#(예제9)=======================
'''
st = 'I love Python Programming'
for ch in st:
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        continue

    print(ch, end='')
'''
