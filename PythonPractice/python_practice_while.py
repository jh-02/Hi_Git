#cnt = 0
#
# while True :
#     print("마법을 쓰기 위해 %s 번째 시도를 하였다." % cnt)
#
#     if cnt == 1000 :
#         print("%s 번째 시도 끝에 마법을 써서 빠져나간다!" % cnt)
#         break
#     cnt += 1

######################################################################

# cnt = 0
#
# repeat_boolean = True
#
# while repeat_boolean :
#     print("아직은 while문 도는 중")
#
#     cnt += 1
#
#     if cnt == 100 :
#         repeat_boolean = False

######################################################################

stock_price = 1000
while stock_price != 1000000 :
    stock_price += 1000

    print("방금 %s 원을 더해서 %s 원이 되었다." % (1000, stock_price))
