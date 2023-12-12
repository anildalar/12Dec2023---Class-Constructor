

# 1. Class Defination
class Parent():
    #1.1 Property=Variable
    bloodGroup='' # Define property
    
    #1.2 Constructor is a special Function/Method
    def __init__(self,bg=''):
        if bg != '':
            self.bloodGroup = bg # Property value initialization
        else:
            self.bloodGroup = 'B+ve'
        
        pass
    
    #1.3 Method = Function
    def myMethod(self):
        print(f"My Blood group is  {self.bloodGroup}")
        pass
    pass



# 2. Create Class Object
ceo = Parent('O+ve') 
#2.1 Call the method with class object
ceo.myMethod()