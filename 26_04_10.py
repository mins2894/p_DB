'''
정통과 이민수
'''
#=============================
''' #함수 정의(define)
def prt_addr(): #<~ 매개 변수(parameter) 
    print('경상북도 울릉군 울릉읍\n독도이사부길 63')
prt_addr() # <~ 인수, 및 함수 호출(함수 내부의 코드 실행)
'''
#=============================
'''
rad = int(input('원의 반지름을 입력하시오: '))
def calc(rad):
    area = 3.14 * rad ** 2
    return area
c_area = calc(rad)
print(f'원의 면적은: {c_area}')
'''
#=============================
'''
n1 = int(input('정렬할 숫자 1개를 입력하시오: '))
n2 = int(input('정렬할 숫자 1개를 입력하시오: '))
def sort(n1, n2):
    if n1 < n2:
        return n1, n2
    else:
        return n2, n1
prt_sort1 = sort(n1, n2)
prt_sort2 = sort(n1+10, n2-30)
print(prt_sort1,'\n', prt_sort2)
'''
#=============================
'''
n1 = int(input('사칙연산을 할 숫자 1개를 입력하시오: '))
n2 = int(input('사칙연산을 할 숫자 1개를 입력하시오: '))
def calc(n1, n2):
    return n1+n2,n1-n2,n1*n2,n1//n2
t1, t2, t3, t4 = calc(n1, n2)
print('='*20)
print(f'{n1} + {n2} = {t1}')
print(f'{n1} - {n2} = {t2}')
print(f'{n1} * {n2} = {t3}')
print(f'{n1} / {n2} = {t4}')
'''
#=============================
'''
print('='*20) # n2값이 0이 될때까지 반복
n1 = int(input('사칙연산을 할 숫자 1개를 입력하시오: '))
n2 = int(input('사칙연산을 할 숫자 1개를 입력하시오: '))
def calc(n1, n2):
    return n1+n2,n1-n2,n1*n2,n1//n2
print('='*20)
while True:
    t1, t2, t3, t4 = calc(n1, n2)
    print(f'{n1} + {n2} = {t1}')
    print(f'{n1} - {n2} = {t2}')
    print(f'{n1} * {n2} = {t3}')
    print(f'{n1} / {n2} = {t4}')
    n2 = n2 - 1
    print('='*20)
'''
#=============================
'''
print('='*20) # n2를 0으로 입력할 때 까지 반복
def calc(n1, n2):
    return n1+n2,n1-n2,n1*n2,n1//n2

    n1 = int(input('사칙연산을 할 숫자 1개를 입력하시오: '))
    n2 = int(input('사칙연산을 할 숫자 1개를 입력하시오: '))
    print('='*20)
    if n2 == 0:
        print('프로그램 종료')
        break
    t1, t2, t3, t4 = calc(n1, n2)
    print(f'{n1} + {n2} = {t1}')
    print(f'{n1} - {n2} = {t2}')
    print(f'{n1} * {n2} = {t3}')
    print(f'{n1} / {n2} = {t4}')
    print('='*20)
'''
#=============================
'''
import turtle as t
t = t.Turtle()
t.shape("turtle")

def squ(leng):
    for i in range(4):
        t.fd(squ)
        t.left(90)
squ(100)
squ(200)
squ(300)
t.done()
'''
#=============================
'''
import turtle as t
t = t.Turtle()
t.shape("turtle")
leng = int(input('반복 할 횟수를 입력하시오: '))
def squ(leng):
    for i in range(4):
        t.fd(squ)
        t.left(90)
for i in range(0)
    squ(leng)
    leng = leng - 100
'''
#=============================
'''
hour_p = float(input('시급을 입력하시오: '))
hour_w = int(input('근무 시간을 입력하시오: '))
def weekpay(hour_p, hour_w):
    if hour_w >= 38:
        wkp = hour_p*30 + 1.5 * hour_p * (hour_w-30)
    return wkp
print(f'주급은: {str(weekpay(hour_p, hour_w))}원 입니다.')
'''
#=============================
'''
파이썬 예제
'''
#=============================
'''
다음 파이썬을 만든 사람은?

하나를 선택하세요.
1. 마크 저커버그
2. 귀도 반 로섬 <<<
3. 스티브 잡스
4. 빌 게이츠
'''
#=============================
'''
파이썬의 기본 자료형 중 True와 False를 나타내는 자료형은 무엇인가?


답: (Boolean)
'''
#=============================

