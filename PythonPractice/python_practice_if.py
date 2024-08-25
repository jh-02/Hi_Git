stock_price = 3000
if stock_price < 2000 :
    print("주가가 2000보다 작네요!")
elif stock_price <= 3000 :
    print("주가가 3000보다 작거나 같네요!")

stock_rate = 2.5
if stock_rate > 2.5 :
    print("2.5보다 크네요!")
elif stock_rate >= 2.5 :
    print("2.5 이상이네요")


stock_name = "키움증권"

if stock_name == "대신증권" or stock_name == "키움증권" :
    print("대신증권이거나 키움증권이네요!")
elif stock_name == "네이버증권" or stock_name == "카카오증권" :
    print("네이버증권 또는 카카오증권 이네요!")

stock_price = 1000
if stock_price < 900 and stock_price > 2000 :
    print("주식가격이 900원보다 작거나 200원보다 크네요")
elif stock_price > 500 and stock_price < 2000 :
    print("500원보다 크고 2000원보다 작네요")
else :
    print("포함되는게 없네요")

stock_name = ("삼성전자")
if stock_name in ["엘지전자", "애플", "삼성전자"] :
    print("삼성전자가 존재한다")

# 섞어보기
if (stock_name in ["엘지전자", "애플", "삼성전자"]
        and (stock_name == "홈즈" or stock_name == "삼성전자")) :
    print("리스트에 포함되어 있으면서")
    print("회사이름은 홈즈이거나 삼성전자입니다.")