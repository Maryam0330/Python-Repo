class parent_class:
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2

    def add(self):
        print("Addition value 1:",self.value1)
        print("Addition value 2:",self.value2)
        print("Addition of two values is",self.value1+self.value2)
        
class child_class(parent_class):
    pass

a=child_class(30,40)
a.add()
