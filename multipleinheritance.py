class parent1:
    def sum(self,a,b):
        print(a+b)
        
class parent2:
    def mul(self,a,b):
        print(a*b)
        
class derive(parent1,parent2):
    def div(self,a,b):
        print (a/b)
        
d=derive()
d.sum(10,20)
d.mul(2,4)
d.div(9,3)
