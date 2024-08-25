a_list = ["키움증권", "대신증권", "네이버증권", "이베스트", "손오공"]

a_len = len(a_list)


print(a_len)

a_list.append("카카오")
print(a_list)

del a_list[0]
print(a_list)
print(a_list[0])

for index, value in enumerate(a_list) :
    print("%s - %s" % (index, value))

cnt = 0
for value in a_list :
    print("%s-%s" % (cnt, value))
    cnt += 1

a_list = ["키움증권", "대신증권", "네이버증권", "이베스트", "손오공"]
check_stock = "키움증권"
cnt = 0
for value in a_list :
    if value == check_stock :
        del a_list[cnt]
        print(a_list)
    cnt += 1

b_list = ["오토", "구글", "페이스북", "애플", "오션"]

for value in b_list :
    a_list.append(value)

print(a_list)

for index, value in enumerate(b_list) :
    a_list[index] = value

print(a_list)

