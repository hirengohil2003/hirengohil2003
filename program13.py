#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

class bankAccount:
    def __init__(self, acc_num, name, balance):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance

    def deposite(self, deposite):
        self.balance = deposite + self.balance
        print("The Amount %d Is Suceessfully Credited In Your Ac No : %d" %
              (deposite, self.acc_num))
        print("The Current Balance Is :", self.balance)
        print("\n")

    def withdraw(self, withdraw):
        if(withdraw > self.balance):
            print("Withdrawal Error!!!!!!!!!")
            print("InSufficient Amount In Your Bank Account !!!!")
            print("\n")
        else:
            self.balance = self.balance - withdraw

            print("The Amount %d Is Successfully  Debited  From  Your Ac No : %d"%(withdraw,self.acc_num))
            print("The Current Balance Is :",self.balance)
            print("\n")
    def represent(self):
        print("The Account Holder's Name Is :",self.name)
        print("The Account Holder's Account Number Is : ",self.acc_num)
        print("The Total Balance Present Is : ",self.balance)


class_obj=bankAccount(2798100002762,"Hiren",51000)
class_obj.deposite(int(input("Enter Deposite Amount : ")))
class_obj.withdraw(int(input("Enter Withdraw Amount : ")))
class_obj.represent()

#------------------------------------------------------------------------------------
