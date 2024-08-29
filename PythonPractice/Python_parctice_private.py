b = 0
tommorow = 0

a = {"종목명":"키움증권", "등락율(%)":3.0, "현재가":5000, "보유량":0}

my_account = 1000000
my_account_old = my_account
while 1 :
    if tommorow == 0 :
        if a["현재가"] >= 2000 : 
            a["현재가"] -= 110
        else :
            print("%s 종목의 가격이 %s 원 이므로 더이상의 주가 하락을 방지합니다." % (a["종목명"], a["현재가"]))
            
        if (my_account >= a["현재가"]) and (tommorow == 0) : # 구매 조건
            a["보유량"] += 1
            my_account -= a["현재가"]
            print("%s 를 %s 원에 구매하였습니다. 현재 보유 수량은 %s 개 입니다." % (a["종목명"], a["현재가"], a["보유량"]))
        else :
            tommorow = 1


    if (tommorow == 1) : # 판매 조건
        if a["현재가"] >= 1000 : 
            a["현재가"] -= 10
        else :
            print("%s 종목의 가격이 %s 원 이므로 더이상의 주가 하락을 방지합니다." % (a["종목명"], a["현재가"]))

        if (a["현재가"] < 1500) :
            a["보유량"] -= 1
            my_account += a["현재가"]
            print("%s 를 %s 원에 판매하였습니다. 현재 보유 수량은 %s 개입니다." % (a["종목명"], a["현재가"], a["보유량"]))
            if a["보유량"]  == 0 :
                break
        
    
print("거래가 끝났습니다.")
print(" 현재 계좌에 %s 원이 있습니다." % my_account)
print(" 손익은 %s 원입니다. " % (my_account - my_account_old))
print(" 현재 보유중인 주식 목록은 아래와 같습니다.")
print(a)