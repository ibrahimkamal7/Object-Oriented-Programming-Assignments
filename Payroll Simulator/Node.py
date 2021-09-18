#Ibrahim Kamal
#ik363
#Node Class
#A portion of the code is taken from the code provided in the class
#Medlock, A(2019). LinkedListDemo[Source Code]

class Node:
    
    def __init__(self , employee , nextEmployee = None):#constructoe
        
        self.employee = employee
        self.nextEmployee = nextEmployee
    
    #getter methods
    def getEmployee(self):
        
        return self.employee
        
    def getEmployeeID(self):
        
        return self.employee.employeeID
    
