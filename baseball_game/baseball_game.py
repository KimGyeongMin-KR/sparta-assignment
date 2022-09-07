import random
from datetime import datetime
def baseball_game(num):
    start_time = datetime.now()

    ans=''
    cnt = 0
    for _ in range(num):
        ans += str(random.randint(0,9))
    while True:
        char = input()
        if char in ['exit',ans]:
            print(f'도전 횟수 : {cnt} 정답 : {ans}')
            break
        sbo = []
        if len(char) == len(ans):
            for i,j in zip(char,ans):
                if i == j:
                    sbo.append('s')
                elif i in ans:
                    sbo.append('b')
                else:
                    sbo.append('o')
            print(' '.join(sbo))
        else:
            print('자리수가 다름')
        cnt+=1
    end_time = datetime.now()
    print(end_time - start_time)
    print(datetime.now().strftime('%y-%m-%d %H:%M'))
    return
num = int(input('원하는 자리수 선택하세요'))
baseball_game(num)