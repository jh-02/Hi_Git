def english() :
    print("영어과 입니다")
    print("영어과에서 영어 공부 합니다")

english()

def math(name, current = 0, value = 0) :
    print("수학과 입니다.")
    print("%s, %s, %s 학생이 전학 왔습니다." % (name, current, value))
    print(current)

math(name="원빈")

def math1(name, eng) :
    print("수학과 입니다.")
    print("%s 은 수학과입니다" % name)
    eng(name = "현빈")

math1(name="원빈", eng = math)

def stock() :
    name = "프로그램동산"
    return name

namee = stock()

print(namee)

def school() :
    name = "광희"
    money = 5000

    return name, money

n,p = school()
t = list(school())
print(n)
print(p)
print(t)


def school1() :
    name = "광희"
    money = 5000

    return name

n = school1()
print(n)

#sample
def condition(name = None, current = 0) :
    if current > 5000 :
        print("종목이름 : %s, 현재가 : %s" % (name, current))

condition(name = "삼성", current = 50000)

a_dict = {"종목명":"삼성", "현재가":50000}
condition(name = a_dict["종목명"], current = a_dict["현재가"])
