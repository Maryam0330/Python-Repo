class student:
    def __init__(self,PRN,name):
        self.PRN=PRN
        self.name=name

class BSC(student):
    def __init__(self,PRN,name,phy,chem,maths):
        super().__init__(PRN,name)
        self.phy=phy
        self.chem=chem
        self.maths=maths
    
    def calculate(self):
        return self.phy+self.chem+self.maths
        
class result(BSC):
    def __init__(self,PRN,name,phy,chem,maths):
        super().__init__(PRN,name,phy,chem,maths)
        
    def getcalmarks(self):
        return super().calculate()
  
a=result(28,"Maryam",80,85,90)
marks=a.getcalmarks()
print(marks)
