# a_dict = {"종목명": "섬광글라스", "등락율(%)": 0.0, "고가대비(%)":-0.97, "보유수량":0, "현재가": 41050, "(최우선)매도호가": 41050}

# print(a_dict.keys())

# print("키 : %s, 값 : %s" % ("종목명", a_dict.get("종목명")))
# print("키 : %s, 값 : %s" % ("종목명", a_dict["종목명"]))

# for key in a_dict.keys() :
#     print(key)
#     print(a_dict[key])

# for key, value in a_dict.items() :
#     print("키: %s, 값 : %s" % (key, value))

# a_dict.update({"종목명":"키움증권"})
# a_dict.update({"보유수량":5, "현재가":5000})
# a_dict.update({"없는 키" : 1491591})
# print(a_dict)

# a_dict["종목명"] = "대신증권"
# print(a_dict)

# a_dict["없는키2"] = 1234
# print(a_dict)


# b_dict = {"123456" :{"종목명": "섬광글라스", "등락율(%)": 7.0, "고가대비(%)":-0.97, "보유수량":0, "현재가": 41050, "(최우선)매도호가": 41050} }

# print(b_dict["123456"]["종목명"])
# print(b_dict.get("123456").get("종목명"))
# print(b_dict["123456"].keys())

# #1
# for key in b_dict.keys() :
#     print(key)
#     print(a_dict["종목명"])
#     if b_dict[key]["등락율(%)"] > 3.0 :
#         print("매수가 되었습니다.")

# for value in b_dict.keys() :
#     if b_dict[value]["현재가"] > 5000 and b_dict[value]["등락율(%)"] > 5.0 :
#         print("%s -- 매수\n\t상세 데이터 --> %s" % (b_dict[value]["종목명"], b_dict[value]))

# c_dict = {"키움증권" : 5000, "카카오" : 3000, "네이버" : 2000, "애플" : 1000000}
# a_plus = 0
# for value in list(c_dict.keys()) :
#     a_plus = a_plus + c_dict[value]
#     if value == list(c_dict.keys())[-1] :
#         print(a_plus) 


# my_account = 1110000

# for value in c_dict.keys() :
#     if value == "키움증권" :
#         my_account -= c_dict[value]*5
#     elif value == "카카오" :
#         my_account -= c_dict[value]*2
#     elif value == "네이버" :
#         my_account -= c_dict[value]*5

# print("남은 금액은 %s 원입니다." % my_account)

# ee_bool = True

# while ee_bool :
#     c_dict["키움증권"] = c_dict["키움증권"] + 1000

#     if c_dict["키움증권"] == 10000 :
#         c_dict.update({"키움증권":0})
#         break
# print(c_dict)
b_dict = {"종목명":"섬광글라스", "등락율" : 0.0, "고가대비" : -0.97, "보유수량" : 0, "현재가" : 41050, "(최우선)매도호가" : 41050}
a_dict = {"123456" : b_dict }
print(a_dict)

# print(len(a_dict))

# print("키 : %s , 값 : %s" % ("종목명", a_dict["123456"]["종목명"]))

# for key in a_dict.keys() :
#     print(key)
#     print(a_dict[key])

# for key, value in a_dict.items() :
#     print("키 : %s, 값 : %s" % (key, value))

b_dict.update({"종목명": "대신증권"})
a_dict.update({"123456" : b_dict})
print(a_dict)
b_dict.update({"보유수량" :5, "현재가" :5000})
a_dict.update({"123456" : b_dict})
print(a_dict)
b_dict.update({"없는키":1000})
a_dict.update({"123456" : b_dict})
print(a_dict)

for key in a_dict.keys() :
    print(a_dict[key])
    print(a_dict.keys())
    print(len(a_dict[key]))
    # print(key)
    if a_dict[key]["등락율"] > 3.0 :
        print("매수가 되었습니다.")