# class B_school() :
#     def __init__(self) :
#         print("B 클래스 입니다.")
    
#     def stock(self, student_name) :
#         print("증권분석과 입니다.")
#         print(student_name)
#         return "증권"

# B_school().stock("원빈")

# bb = B_school()
# result = bb.stock("원빈")
# print(result)

# class C_school() :
#     def __init__(self) :
#         print("B 클래스 입니다.")
#         student_name = "현빈"
#         print(dir(self))
#         self.stock(student_name)
    
#     def stock(self, st) :
#         print("증권분석과 입니다.")
#         print("%s 전학생 입니다." % st)


# C_school()

print("*********************************************")
class D_school() :
    def __init__(self) :
        print("B 클래스 입니다.")
        self.student_name = "현빈"
        print(dir(self))
        self.stock()
        self.english()
    
    def stock(self) :
        print("증권분석과 입니다.")
        print("%s 전학생 입니다." % self.student_name)
    
    def english(self) :
        print("%s 영어과 입니다." % self.student_name)
    
    def france(self) :
        student_name1 = "원빈"
        return student_name1


D_school()

dd = D_school()

print(dd.student_name)

print(D_school().student_name)
print(D_school().student_name)

class A_school() :
    def __init__(self) :
        print("A 클래스 입니다.")

        bb = D_school()
        student_name2 = bb.france()
        self.student_name_a = bb.student_name
        print(self.student_name_a)
        print(student_name2)
    

A_school()

#상속
class Parent() :
    def __init__(self) :
        print("부모 클래스!")
        self.money = 500000000
    
    def book(self) :
        print("부모의 서재입니다.")
        self.money1 = 1000000

class Child1(Parent) : # 부모클래스 상속
    def __init__(self) :
        super().__init__() # 부모클래스를 상속만 한다고 해서 self가 공유되는건 아님. 무조건 self가 정의되어있는 함수를 콜한 후에 사용가능
        print("첫번째 자식입니다.")
        print(self.money)

class Child2(Parent) : # 부모클래스 상속
    def __init__(self) :
        print(dir(self))
        super().book() # 부모클래스를 상속만 한다고 해서 self가 공유되는건 아님. 무조건 self로 담는 함수를 콜한 후에 사용가능
        print("두번째 자식입니다.")
        print(self.money1)


Child1()
Child2()


