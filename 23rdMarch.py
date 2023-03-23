class Account:
    def __init__(self, cardNumber, pin, balance, wAmount, accountType) :
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = balance
        self.wAmount = wAmount
        self. accountType = accountType
    def m1 (self, wAmount):
        if wAmount <= self.balance:
            nbalance = self.balance - uwAmount
            self.balance = nbalance
        return nbalance 
class ATM:
    def __init__(self,branch_name , accountList):
        self.branch_name = branch_name
        self.accountList = accountList
    def m2 (self, ucardNumber , upin, uwAmount ): 
        for i in self.accountList:
            if i.cardNumber == ucardNumber and i.pin == upin:
                call = i.m1 (uwAmount )
                print(f"{i.cardNumber} {call} {uwAmount}")
                break
        else:
            print ( "No account Exists")
    def m3 (self, uaccountType) :
        dic = {}
        for i in self.accountList:
            if i.accountType.lower () == uaccountType. lower ( ) :
                dic[i.cardNumber] = i.balance
        return dic
accountList = []
for i in range (int (input ( ) ) ) :
    cardNumber = int (input ( ))
    pin = int (input ( ))
    balance = float (input ( ))
    wAmount = float (input ( ) )
    accountType = input ( )
    objAccount = Account ( cardNumber, pin, balance, wAmount, accountType )
    accountList.append (objAccount)
ucardnumber = int (input () )
upin = int (input ( ))
uwAmount = float (input ( ) )
uaccountType = input ( )

objATM = ATM( 'Delhi' , accountList)
ans1 = objATM. m2(ucardnumber, upin, uwAmount )
ans2 = objATM.m3(uaccountType )
if ans1:
    print(ans1)

if ans2:
    for i in ans2:
        print(i,ans2[i])




"""
Input 2:
2
12345
12
30.0
10.0
salary
45678
98
400.0
200.0
salary
12345
12
10
salary

Output 2:
12345 20.0 10.0
12345 20.0
45678 400.0


Input 2:
2
12345
12
30.0
10.0
salary
45678
98
400.0
200.0
salary
34532
34
12
salary

Output 2:
No account Exists
12345 30.0
45678 400.0

"""