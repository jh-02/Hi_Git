def prin() :
    print("테스트용 함수입니다.")
    print("테스트 한번 더할거에요")

a_dict = {"키움증권":{"가격":5000}, "대신증권":{"가격":1000} , "삼성전자":{"가격":80000}, "카카오":{"가격":20000}, "코카콜라":{"가격":60000}}

def best_price(dictionary) :
    key_list = list(dictionary.keys())
    best_old = dictionary[key_list[0]]["가격"]
    price = dictionary[key_list[0]]["가격"]
    for key in dictionary.keys() :
        price = dictionary[key]["가격"]
        if price >= best_old :
            best = key
            best_old = price
    
    return best

def minimum_price(dictionary) :
    key_list = list(dictionary.keys())
    mini_old = dictionary[key_list[0]]["가격"]
    price = dictionary[key_list[0]]["가격"]
    for key in dictionary.keys() :
        price = dictionary[key]["가격"]
        if price <= mini_old :
            mini = key
            mini_old = price
    
    return mini

        
print(best_price(a_dict))
print(minimum_price(a_dict))


