for i in range(0,10,1) :
    print("%s 일째 복역 중입니다." % (i+1))
    if i == 4 :
        print("사면되었습니다.")
        print("%s 일 복역 후 자유가 되었습니다." % len(range(0,i+1,1)))
        break


# print("%s 일 동안 복역해서 자유가 되었습니다." % len(range(0,10,1)))
# print("%s 일 동안 복역해서 자유가 되었습니다." % len(range(0,10,1)))

count = 0
for i in range(0,10,1) :
    count += 1
    print(count)


for i, value in enumerate(['키움', '삼성', '카카오']) :
    print("%s 순번과 %s 값" % (i, value))
