a_dict = {"종목명": "섬광글라스", "등락율(%)": 0.0, "고가대비(%)":-0.97, "보유수량":0, "현재가": 41050, "(최우선)매도호가": 41050}

print(a_dict.keys())

print("키 : %s, 값 : %s" % ("종목명", a_dict.get("종목명")))
print("키 : %s, 값 : %s" % ("종목명", a_dict["종목명"]))

for key in a_dict.keys() :
    print(key)
    print(a_dict[key])

for key, value in a_dict.items() :
    print("키: %s, 값 : %s" % (key, value))

a_dict.update({"종목명":"키움증권"})
a_dict.update({"보유수량":5, "현재가":5000})
a_dict.update({"없는 키" : 1491591})
print(a_dict)

a_dict["종목명"] = "대신증권"
print(a_dict)

a_dict["없는키2"] = 1234
print(a_dict)


b_dict = {"123456" :{"종목명": "섬광글라스", "등락율(%)": 0.0, "고가대비(%)":-0.97, "보유수량":0, "현재가": 41050, "(최우선)매도호가": 41050} }

print(b_dict["123456"]["종목명"])
print(b_dict.get("123456").get("종목명"))
print(b_dict["123456"].keys())