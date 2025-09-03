class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

acc1 = Account("123341","rao213")

print(acc1.acc_no)
print(acc1.__acc_pass)