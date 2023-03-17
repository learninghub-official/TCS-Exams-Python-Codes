class Service:
    def __init__(self,serviceId,regNo,model,mileage,isInsured,paymentRecvd):
        self.serviceId = serviceId
        self.regNo = regNo
        self.model = model
        self.mileage = mileage
        self.isInsured = isInsured
        self.paymentRecvd = paymentRecvd


class ServiceCentre:
    def __init__(self,mileagedict,serviceList):
        self.mileagedict = mileagedict
        self.serviceList = serviceList
    def getTotalPaymentOfInsuredCars(self,ManufacturerName,stateCode):
        for i in serviceList:
            if

serviceList = []
n = int(input())
for i in range(n):
    serviceId = int(input())
    regNo = input()
    model = input()
    mileage = int(input())
    isInsured = input()
    paymentRecvd = float(input())
    Serviceobj = Service(serviceId,regNo,model,mileage,isInsured,paymentRecvd)
    serviceList.append(Serviceobj)

m = int(input())
for i in range(m):
    ManufacturerName = input()
    stateCode = int(input())

mileagedict = {}
for i in serviceList:
    mileagedict[i.model] = i.mileage
print(mileagedict)



mName = input()
statename = input()

'''

4
101
MA1234
Tata Indica
15
yes
2500
102
MA472367
Honda City
18
yes
35000
103
UK4321
Honda Bravo
17
yes
5600
104
MA2221
Tata Nano
12
yes
2300
5
Tata Indica
15
Tata Nano
12
Honda City
20
Honda bravo
17
Hyundai Accent
18
tata 
ma

Output:
MA TATA 4800.0
103#UK4321#Honda Bravo#17
101#MA1234# ata indica#15
104#MA2221#Tata Nano#12

 '''