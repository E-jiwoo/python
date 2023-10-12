'''
print("안녕하세요 %s에서 %s을 담당하고 있는 %d살 %s입니다" %("부소마", "학생", 17, "이지우"))
print("안녕하세요 %s에서 %s을 담당하고 있는 %d살 %s입니다" %("부소마", "학생", 17, "최지우"))
print("안녕하세요 %s에서 %s을 담당하고 있는 %d살 %s입니다" %("부소마", "학생", 17, "송지우"))
print("안녕하세요 %s에서 %s을 담당하고 있는 %d살 %s입니다" %("부소마", "학생", 17, "박지우"))
print("안녕하세요 %s에서 %s을 담당하고 있는 %d살 %s입니다" %("부소마", "학생", 17, "김지우"))

'''

#클래스 : 비슷한 작업을 반복하기도 편리하고, 관련된 정보를 한 곳에 모아서 관리하기 위한 툴
#객체 : 클래스를 이용해 만들어진 실체
#메소드(method) : 클래스 내부의 멤버로서 함수의 역할을 수행하는 것, 클래스 내부에서 특정 기능 수행을 담당

''' 
class 클래스 명:
    #생성자
    def __init__(self,...):
        속성 정의
'''

#__init__() : 인스턴스를 만들 때 실행되는 초기화 함수 = 생성자 / 객체가 처음 만들어지는 순간 딱 한번만 호출되며, 객체의 초기값을 설정하는 역할

class Bssm:
    def __init__(self, team, task, age, name):
        self.team = team
        self.task = task
        self.age = age
        self.name = name
    def intro(self):
        print("안녕하세요 %s에서 %s을 담당하고 있는 %d살 %s입니다" %(self.team, self.task, self.age, self.name))

a=Bssm("부소마","학생",17,"이지우")

a.intro()
        
# __str__() ; 인스턴스 자체를 출력할 때 문자열 형식을 지정해주는 함수

'''
Grade 클래스를 만들고, 클래스 안에 메소드를 정의해 다음 코드와 실행결과가 아래와 같이 나오도록 코딩

a1=Grade("나영", 89)
a1.s_grade()
print(a1)

90점 이상 : A
80점 이상 : B
'''

class Grade:
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def grade(self):
        if(self.score > 89):
            self.score='A'
        elif(self.score > 79):
            self.score='B'
        else:
            self.score='C'
    def __str__(self):
        return "%s : %c 등급" %(self.name, self.score)
    
a1=Grade("지우", 100)
a1.grade()
print(a1)

class FishCakeMaker:
    def __init__(self, **kwargs): #** : 가변인자 매개변수
        self.size=10
        self.flavor="팥"
        self.price=100

        if "size" in kwargs:
            self.size=kwargs.get("size") #kwargs 딕셔너리 안에 size라는 key값이 있니? 있다면 가져와서 size 변수에 그 해당하는 value값을 다시 대입하겠다
        if "flavor" in kwargs:
            self.flavor=kwargs.get("flavor")
        if "price" in kwargs:
            self.price=kwargs.get("price")
    
    def show(self):
        print("붕어빵 크기{}".format(self.size))
        print("붕어빵 종류{}".format(self.flavor))
        print("붕어빵 가격{}".format(self.price))
        print("*"*30)

fish1=FishCakeMaker()
fish2=FishCakeMaker(size=20, price=300)
fish3=FishCakeMaker(flavor="초코", size=15)
fish1.show()
fish2.show()
fish3.show()
        