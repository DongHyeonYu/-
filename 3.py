import random
while 1:
    print("숫자 야구 게임을 시작합니다. ")
    n = int(random.random()*1000)
    S = 0 
    B = 0
    while 1:
        print("숫자를 입력해주세요 : ", end='')
        a = input()
        for i, j in zip(str(n), a):
            if i == j:
                S+=1
            else:
                B+=1
                    
        if S ==0:
            print(f"{B}B")
        elif B ==0:
            print(f"{S}S")
            if S == 3:
                print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
                break
        else:
            print(f"{B}B {S}S")
        S = 0
        B = 0
            
    print("게임을 새로 시작하려면 Y, 종료하려면 N을 입력하세요")
    new = input()
    if new == "N":
        break
#ggasdfa
