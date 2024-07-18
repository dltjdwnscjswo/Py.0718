#문자 메세지 길이 판별 클래스. 문자메세지 기이에 따라 문자 요금이 결정되는 프로그램을 작성하시오.

# 문자메세지의 길이에 따라 부과되는 요금은, 클래스를 생성할 때 속성 정보로 갖게 된다. 또한, 요금이 부과될 문자 메세지의
# 길이를 정할수 있도록 설정하시오(속성정보)

# 이때, 사용자로부터 문자메세지를 입력 받아서 문자 요금을 반환하는 코드를 작성하시오.

class MessageLengthCharge:
    def __init__(self, unit_length, base_charge):
        self.unit_length = unit_length  # 한 글자당 요금
        self.base_charge = base_charge  # 기본 요금

    def calculate_charge(self, message):
        message_length = len(message)
        if message_length == 0:
            return self.base_charge
        else:
            total_charge = self.base_charge + message_length * self.unit_length
            return total_charge


# 사용 예시
if __name__ == "__main__":
    # 클래스 생성: 한 글자당 10원, 기본 요금 100원
    charge_calculator = MessageLengthCharge(unit_length=10, base_charge=100)

    # 사용자 입력 받기
    message = input("전송할 문자 메시지를 입력하세요: ")

    # 요금 계산
    charge = charge_calculator.calculate_charge(message)

    # 결과 출력
    print(f"입력한 문자 메시지 '{message}'의 요금은 {charge}원입니다.")