a_tuple = ("키움증권", "대신증권", "네이버증권")
print(type(a_tuple))

a_len = len(a_tuple)
print(a_len)

print(a_tuple[1])

for value in a_tuple :
    print(value)


for index, value in enumerate(a_tuple) :
    print(index, value)
    print(value)

kiwoom_count = 0
for value in a_tuple :
    if value == "키움증권" :
        kiwoom_count += 1

print("키움종목 매수량 : %s" % kiwoom_count)
