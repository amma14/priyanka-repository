class School:
    def __init__(self,schoolname,schooladdress,schoolpincode):
        self.name=schoolname
        self.address=schooladdress
        self.pincode=schoolpincode

    def display(self):
        print(f'this is parent class:,{self.name},{self.address},{self.pincode}')


class Student(School):
    def __init__(self,schoolname,schooladdress,schoolpincode,studentname,studentrollno):
        School.__init__(self,schoolname,schooladdress,schoolpincode)
        self.sname=studentname
        self.rollno=studentrollno

    def view(self):
        print(f'this is child class:{self.name},{self.address},{self.pincode},{self.sname},{self.rollno}')


object=Student('narayana','hydarabad',533445,'priyanka',504)
object.view()

