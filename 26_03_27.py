'''
정통과 이민수
'''
#(예제1)=======================
'''
x = int(input("값을 입력"))
if x>=1:
    print("x는 1 이상 크다.")
elif x==0:
    print("x는 0이다")
else:
    print("x는 0 미만으로 작다.")
'''
#(예제2)=======================
'''
score = int(input("성적을 입력하시오: "))
if score>=60:
    print("합격")
else:
    print("불합격")
'''
#(예제3)=======================
'''
num = int(input('양의 정수를 입력하시오: '))
if num%2==1:
    print("홀수입니다.")
elif num<=0:
    print("오류입니다, 양의 정수를 입력해주세요")
else:
    print("짝수입니다.")
'''
#(예제4)=======================
'''
num = int(input('정수를 입력하시오: '))
if num<0:
    print('음수입니다.')
elif num>0:
    print('양수입니다.')
    if num%2==1:
        print("홀수입니다.")
    else:
        print("짝수입니다.")
else:
    print('오류입니다.')
'''
#(예제5)=======================
'''
age = int(input('나이를 입력하시오: '))
if age>=15:
    print("본 영화를 관람하실 수 있습니다.")

else:
    print("본 영화를 관람하실 수 없습니다.")
'''
#(예제6)=======================
'''
import random as r
print("동전 던지기를 시작합니다.")
coin = r.randrange(2)
if coin == 1:
    print('앞면입니다.')
else:
    print('뒷면입니다.')
'''
#(예제7)=======================
'''
x = int(input("값을 입력"))
if x>=1:
    print("값은 양수입니다.")
elif x==0:
    print("값은 0 입니다.")
else:
    print("값은 음수입니다.")
'''
#(예제8)=======================
'''
num = int(input('정수를 입력하시오: '))
if num>=0:
    if num==0:
        print("0 입니다.")
    else:
        print('양수입니다')
else:
    print("음수입니다.")
'''
#(예제9)=======================
'''
id = 'ilovepython'
s = input('아이디를 입력하시오: ')
if s == id:
    print('환영합니다.')
else:
    print('아이디를 찾을 수 없습니다.')
'''
#(예제10)=======================
'''
for i in "Hello World!":
    print("i =",i)
'''
#(예제11)=======================
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
    print(x,'*',y,'=',x*y)
'''
