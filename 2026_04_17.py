'''
Clang = input('세상에서 가장 쉬운 프로그래밍 언어는?')
print(Clang == '파이썬')
isPy = input('파이썬에서 제곱 연산자는?')
print(isPy == '**')
Py_str = input('프로그래밍 언어에서 텍스트를 무엇이라고 부르는가?')
print(Py_str == '문자열')
'''
# ====================
'''
import datetime as sysdate
metday = sysdate.datetime(2022, 9, 1)
now = y = sysdate.datetime(2022, 9, 18)
past = now - metday
print(f'현재: {str(now)}')
print(f'만난 일:{str(metday)}')
print('만난 지:'+str(past.days)+'일 되었습니다.')
'''
# ====================
'''
first = input('이름의 첫 번째 글자를 입력하시오: ')
second = input('이름의 두 번째 글자를 입력하시오: ')
third = input('이름의 세 번째 글자를 입력하시오: ')
print(f'영어 이니셜은 {first[0]+second[0]+third[0]}입니다.')
'''