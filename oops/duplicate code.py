class faculty:
    def __init__(self,collagename,collageaddress,collagepincode):
        self.name=collagename
        self.address=collageaddress
        self.pincode=collagepincode

    def view(self):
        print(self.name,self.address,self.pincode)

class peoples(faculty):



