class CreateBusiness:
    def __init__(self):         # Default Var
        self.name = None        # 사업체 이름
        self.StartPrice = 10000 # 시작 가격 (Won)
        self.StartStaff = 50    # 시작 직원 수 (명)
    
    def show(self): # 출력
        print(f"이름 : {self.name}") # 이름
        print(f"시작 가격 : {self.StartPrice}") # 시작가격 
        print(f"시작 직원 : {self.StartStaff}명") # 시작 직원수