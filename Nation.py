# 국가 클래스 만들기
"""
    초기화 : 국가명, 인구, 수도
    show() 메서드 만들기 ---> "국가 클래스 메소드입니다" 출력하기

    국가 클래스를 상속받아 대한민국 클래스 만들기
"""


class Nation:
    def __init__(self, **kwargs):
        self.name = "대한민국"
        self.population = 0
        self.capital = "서울"

        if "name" in kwargs:
            self.naem = kwargs.get("name")
        if "population" in kwargs:
            self.population = kwargs.get("population")
        if "captial" in kwargs:
            self.capital = kwargs.get("capital")

    def show(self):
        print("국가명{}".format(self.name))
        print("인구{}".format(self.population))
        print("수도{}".format(self.capital))
        print("*" * 30)


# 붕어빵기계 클래스를 상속받은 마켓 굿즈


class Capital(Nation):  # 괄호 안에 있는 게 부모 클래스
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self.maker_price = self.price + margin

    def show(self):
        print()


korea = Nation
