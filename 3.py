import random
while 1:
    print("숫자 야구 게임을 시작합니다. ")
    n = int(random.random()*1000) # 중복된 숫자가 들어가는 경우를 잡아내지 못합니다.
    S = 0  # S, B가 게임 관련 안쪽 루프에서만 사용되나 루프 바깥에서 선언하는 것은 이후 코드 가독성과 유지보수에 영향을 끼칠 수 있습니다.
    B = 0
    while 1:
        print("숫자를 입력해주세요 : ", end='') # 숫자 입력이 아닌 경우를 잡아내지 못합니다. 입력이 3글자인지 검증하지 않았습니다. 서로 다른 수 3개가 입력되었는지 검증하지 않았습니다.
        a = input()
        for i, j in zip(str(n), a):
            if i == j:
                S+=1
            else: # 볼 판정이 잘못 구현되었습니다.
                B+=1
                    
        if S ==0:
            print(f"{B}B") # OUT 관련 로직과 겹칠 수 있습니다.
        elif B ==0:
            print(f"{S}S")
            if S == 3:
                print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
                break
        else:
            # OUT 관련 로직이 없습니다.
            print(f"{B}B {S}S") 
        S = 0  # 안쪽 while 내부에서만 사용되는 변수 S, B의 scope를 명확히 하는 것이 좋아보입니다.
        B = 0
            
    print("게임을 새로 시작하려면 Y, 종료하려면 N을 입력하세요")
    new = input() # input의 파라미터로 입력을 받기 전에 보여줄 문자열을 먼저 출력할 수 있습니다.
    if new == "N": # 변수 인라인화가 가능하나, 선호에 따라 선택 가능합니다.
        break
#ggasdfa
