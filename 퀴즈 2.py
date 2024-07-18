#게임 캐릭터 만들기. 게임 캐릭터 생성 클래스는 아이디,성별, 직업 정보를 갖으며, 기본 공격 함수를 갖는다. 기본 공격 함수는 사용시 "공격"
# 문자열을 화면에 출력한다

class Uers :
    def __init__(self,id,sex,job):
        self.Uers_id = id
        self.Uers_sex = sex
        self.Uers_job = job
    def attack(self,you_id):
        print(self.Uers_id,"(이)가", you_id,"공격했다 !")

most = Uers("닉네임","남","전사")

most.attack("짱짱보스")