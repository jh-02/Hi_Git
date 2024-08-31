class B_School() : # 클래스 이름의 첫글자는 대문자로 하기 (알아보기 쉽게)
    def __init__(self) :
        print("B 클래스 입니다")

        self.student_name = "원빈"
        # print(dir(self))
        self.stock()
        # print(dir(self))
        # self.stock1()
        # print(dir(self))

    def stock(self) :
        print("증권분석과 입니다.")
        self.student_name2 = "소지섭"
        print("%s 전학생 입니다." % self.student_name)
        # print(name)
        # return "증권"
    
    def stock1(self) :
        print("시장분석과 입니다.")
        self.student_name3 = "유재석"
        print("%s 전학생 입니다." % self.student_name2)


class A_school() :
    def __init__(self) :
        print("A 클래스 입니다.")

        self.student_name_a = bb.student_name
        print(self.student_name_a)
        self.student_name_a2 = bb.student_name3
        print(self.student_name_a2)


bb = B_School()
cc = B_School()
# print(bb.student_name3)

# A_school()

bb.stock1()

#상속
class Parent() :
    def __init__(self) :
        print("부모 클래스!")

        self.money = 50000000000000
        self.stock = 5
    
    def book(self) :
        print("부모의 서재입니다.")


class Child1(Parent) :
    def __init__(self) :
        super().__init__()
        print("첫번째 자식입니다.")
        print(self.money)

class Child2(Parent) :
    def __init__(self) :
        super().__init__()
        super().book()
        # print("두번째 자식입니다.")
        # print(self.money)

# Child1()
Child2()




# bb.stock()
# # bb.stock()
# # bb.stock1()

# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

# my_car = Car("red", "Sedan")  # `my_car`는 `Car` 클래스의 인스턴스
# print(my_car)
