#부동산 정보 입력 클래스. 부동산 정보 클래스는 위치, 평수, 건물의 종류, 가격, 건물이 지어진 년도 정보를 갖는다.
# 또한, 정보 확인 함수를 사용하면 부동산 객체에 포함된 속성 정보를 화면에 출력한다.

class 부동산 :
    def __init__(self,위치,평수,건물의종류,가격,제작년도):
        self.a_위치 = 위치
        self.a_평수 = 평수
        self.a_건물의종류 = 건물의종류
        self.a_가격 = 가격
        self.a_제작년도 = 제작년도
    def print_부동산(self):
        print(self.a_위치,self.a_평수,self.a_건물의종류,self.a_가격,self.a_제작년도)

A아파트 = 부동산("수원","10평","원룸","1000원","2024년")

