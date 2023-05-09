class Employee:
    def __init__(self,emname,emno,emsalary,emplace):
        self.name=emname
        self.no=emno
        self.salary=emsalary
        self.place=emplace
    def order(self):
        print(self.name)
        print(self.no)
        print(self.place)
        print(self.salary)
    def order1(self):
        print(self.place)
        print(self.no)
        print(self.salary)

employee1=Employee('priyanka',143,300000,'bangalore')
employee2=Employee('priya',343,500000,'hydarabad')
employee1.order()
print()
employee2.order1()





class Sir:
    def __init__(self,sir_name,sir_phoneno,sir_address,sir_salary):
        self.name=sir_name
        self.phoneno=sir_phoneno
        self.address=sir_address
        self.salary=sir_salary
obj1=Sir('manisir',123456,'bangalore',400000)
obj2=Sir('ganeshsir',345678,'hyd',350000)
obj3=Sir('ganesh',340078,'mumbai',380000)
obj4=Sir('appu',34566900,'hyd1',390000)


priyaa=[obj1,obj2,obj3,obj4]
for i in priyaa:
    print(i.name)
    print(i.phoneno)
    print(i.salary)
    print(i.name)
    print()



















