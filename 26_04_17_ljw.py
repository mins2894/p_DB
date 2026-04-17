'''
20262421 정보통신공학과 이지우
'''
#=====================================================(리스트list)
#노트
'''
height = 
bts = []          #비어있는 리스트
bts2 = list()     #
bts = bts + ['rm']#리스트에 추가

bts = ['v', 'J-hope'] + ['RM', 'jungkook', 'jin'] 

nu = [10, 20, 30] + [40 + 50 + 60]

n= [0,1,2]*3         
print()

ss = [['k', 'l', 1], ["a", 2], ['s', 3]]      #리스트에 리스트 추가 가능

any()    #리스트에 참인원소 하나라도 있으면 참
all()    #모든원소가 참일시 참
nn = [200, 700, 500, 300, 400]
ien()    #리스트 길이 반환
max()    #최대값반환
min()    #
sum() 
sum() / len()
t_nn = list(10,20,30)

.append()       #리스트 뒤쪽에 추가
.insert()       #리스트 지정 위치에 추가


slist.insert(4, "oioi")   4다음에 oioi 추가

remove(), pop()메소드, del 명령사용

a = ['q', 'b'] 
a.remove("b")              #리스트에서 지우기

pop()    #

del a[0]

.sort()              #리스트 정렬
.sort(reverse=True)  #역순

a2 = sorter(a)



'''




#========================================================
#첫 번째 예제
'''
fruits = []

name = input("좋아하는 과일 이름을 입력하시오: ")
fruits.append(name)
name = input("좋아하는 과일 이름을 입력하시오: ")
fruits.append(name)
name = input("좋아하는 과일 이름을 입력하시오: ")
fruits.append(name)

name = input("과일의 이름을 입력하세요: ")

if name in fruits:
    print("이 과일은 당신이 좋아하는 과일입니다.")
else:
    print("이 과일은 당신이 좋아하는 과일이 아닙니다.")
'''
#=========================================================
#두 번째 예제
'''
population = ['Seoul', 9765, 'Busan', 3441, 'Incheom', 2954]

print('서울 인구', population[1])

print('인천 인구', population[-1])

cities = population[0::2]
print('도시 리스트: ', cities)

pops = population[1::2]
print("인구의 합: ", sum(pops))
'''
#=========================================================
#세 번째 예시
'''
lst = [0, 10, 20, 30, 40, 50]
lst5 = lst.pop()
print(lst5, lst)
lst1 = lst.pop(1)
print(lst1, lst)
'''
#=========================================================
#네 번째 예시

import random

quotes = []

quotes.append('꿈을 지녀라. 그러면 어려운 현실을 이길수 있다.')
quotes.append('언제나 현재에 집중할수 있다면 행복할것이다.')
quotes.append('고생없이 얻을수 있웅 진실로 귀중한 것은 하나도 없다')


print('#########################')
print('# 오늘의 명언 #')
print('#########################')
print('')

dailyQuote = random.choice(quotes)

print(dailyQuote)

#=========================================================
#다섯 번째 예시



















    
