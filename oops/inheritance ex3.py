class Faculty:
    def __init__(self,firstname,lastname,email,facultyid,salary,address,subjects):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.facultyid=facultyid
        self.salary=salary
        self.address=address
        self.subjects=subjects
    def getfullname(self):
        print(self.firstname+"+"+self.lastname)
    def changeaddress(self,newAddress):
        self.address=newAddress
        print()

