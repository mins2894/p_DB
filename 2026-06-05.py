'''
for i in range(2, 10):
    guli=""
    for n in range(1, 10):
        guli+=str(f'{i}*{n}={n*i}\n')
    print(guli)
print()
'''
#==========================================
'''
num = int(input('원하는 단은: '))
for i in range(1, 10):
    print(f'{num}*{i}={num*i}\n')
'''
#==========================================
'''
scr=[90,26,67,45,80]
num = 0
for i in scr:
    num = num+1
    if i < 60:
        continue
    print(f'{num}번 학생, {i}점으로 합격입니다. 축하합니다!')
''' 
#==========================================
scr=[26,90,67,45,80]
num = 0
for i in scr:
    num = num+1
    if i >= 60:
        print(f'{num}번 학생, {i}점으로 합격입니다. 축하합니다!')
    break