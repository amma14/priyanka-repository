# inheritance:inheritance means when one class derives from another class.......
# ability to use methods and attribute in newly created class from already created class is calss inheritance
# a child class will inherites the public and protected properties and methods is called inheritance



# there are 5 types
# 1.single inheritance
# 2.multipile inheritance
# 3.multilevel inheritance
# 4.hierarichal inheritance
# 5.hybrid inheritance



# 1.single inheritance:single inheritance means one parent class derives from one child class

class parent:
    def method1(self):
        print('i am a parent')

class child(parent):
    def method2(self):
        print('i am a child')

child1=child()
child1.method2()
child1.method1()



# 2.multiple inheritance:muliple inheritance means more than one parent class derives from one child class

class father:
    def method1(self):
        print('i am a father')

class mother:
    def method2(self):
        print('i am a mother')

class child(father,mother):
    def method3(self):
        print('i am a child')


child1=child()
child1.method3()
child1.method2()
child1.method1()

