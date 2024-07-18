class 문자열계산 :
    def __init__(self,l, a,b):
        self.l = l
        self.a = a
        self.b = a
    def A_a(self, text):
        len_text = len(text)
        if len_text < self.l:
            result = self.a
            return result
        else:
            result = self.b
            return result




x = 문자열계산(10, "50원", "100원")

print(x.A_a("안녕하세요. 저는 이성준입니다."))