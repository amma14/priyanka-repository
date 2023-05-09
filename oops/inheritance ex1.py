# multilevel inheritance:multilevel inheritance means one parent class derives from child class and cl
# hild class derives from another child class

class grandparent:
    def method1(self):
        print('i am a grandparent')

class parent(grandparent):
    def method2(self):
        print('i am a parent')

class child(parent):
    def method3(self):
        print('i am a child')

child1=child()
child1.method3()
child1.method2()
child1.method1()


# MRO:method resolution order


# 4.heirarichal inheritance:heirarichal inheritance means one parent class derives from more than one child class

class parent:
    def method1(self):
        print('i am a parent')

class child1(parent):
    def method2(self):
        print('i am a child1')


class child2(parent):
    def method3(self):
        print('i am a child2')


child1=child1()
child1.method2()
child1.method1()

child2=child2()
child2.method3()
child2.method1()









