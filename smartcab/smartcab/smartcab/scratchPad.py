class A:
    def __init__(self, name ='anu',age=5):
        print('Inside A')
        self.name = 'ANU'
        self.age = 10
class B(A):
    def __init__(self,name,age,Sex='M'):
        A.__init__(self,name,age)
        self.Sex =Sex
        print('Inside B')

Test_B = B('x','y')


# print(help(B))
print(Test_B.age)
