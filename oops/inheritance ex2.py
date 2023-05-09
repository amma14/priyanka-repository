# hybrid inheritance:combination of more than one child class


class grandparent:
    def method1(self):
        print('i am grandparent')

class parent1(grandparent):
    def method2(self):
        print('i am a parent1')

class parent2:
    def method3(self):
        print('i am a parent2')

class child(parent1,parent2):
    def method4(self):
        print('i am a child')

child1=child()
child1.method4()
child1.method3()
child1.method2()
child1.method1()