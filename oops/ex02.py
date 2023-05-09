# to creat obtect:
class MyDetails:
    myname='priyaa'
    mynumber=9032973589
    myvillage='gollaprolu'
    mystudy='b.tech'
    myage=22
    print(myname,myvillage,mystudy,mynumber,myage)

MyDetails()
details1=MyDetails
print(details1.myname)
print(details1.mynumber)
details1.myage=20
print(details1.myage)
print(details1.myvillage)



class ClassName():
    def method1(self):
        print('this is oops concept')

# syntax:ClassName.methodname()

print(ClassName.method1(2))
ClassName.method1(2)



# init method():
# The init function is called every time an object is created from the class

# syntax:
# def__init__(self,parameter1,parameter2,parameter3,......parametern):
#         self.parameter1=parameter1
#         self.parameter2=parameter2
    














