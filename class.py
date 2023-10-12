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
    
a1=Grade("나영", 89)
a1.grade()
print(a1)