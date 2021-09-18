#Ibrahim Kamal
#ik363
#Employee Class

class Employee:
    
    def __init__(self, employeeID , hourlyPay):#constructor to initialize the attributes
        self.employeeID = employeeID 
        self.hourlyPay = hourlyPay
        self.hours = 0.0
        self.wage = 0.0

    #setter methods
    def setHoursWorked(self , hours):
        
        self.hours = hours

    def setHourlyPay(self , hourlyPay):
        
        self.hourlyPay = hourlyPay

    def setWage(self):
        
        self.wage = self.hours * self.hourlyPay
    
    #getter methods
    def getID(self):
        
        return self.employeeID
        
    def getHourlyPay(self):
        
        return self.hourlyPay
    
    def getHoursWorked(self):
        
        return self.hours
    
    def getWage(self):
        
        return self.wage

    def __str__(self):
        
        return "Employee ID: {}\nHourly Rate: $ {}\nHours Worked: {}\nGross Wages: $ {}\n".format(str(self.getID()) , str(self.getHourlyPay()) , str(self.getHoursWorked()), str(self.getWage()))
