class Calculation:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a/b

print(Calculation.add(5,7))
print(Calculation.sub(4,9))
print(Calculation.mul(3,6))
print(Calculation.div(4,5))



object=Calculation
print(object.add(4,6))

