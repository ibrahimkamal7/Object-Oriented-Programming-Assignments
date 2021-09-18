#Ibrahim Kamal
#ik363
#Main script to run the payroll simulator

from LinkedList import LinkedList
from Employee import Employee
from Node import Node
import time
#function to print the choices for the user
def userChoice():
    
    choices = ['\n*** CS 172 Payroll Simulator ***','a. Add a new employee to the list','b. Enter number of hours the employee worked to calculate his/her weekly wages','c. Display payroll for the employee(s)','d. Update the hourly pay of an employee','e. Remove an employee from the list','f. Quit the payroll simulator\n']
    for i in range(len(choices)):
        print(choices[i])

if __name__ == "__main__":
    
    print("Welcome!\nThis is a payroll simulator. You will be provided several options to choose from. If you choose \'f\' or any other character apart from the ones given in the options, the simulator will end. The simulator will go on until you choose to quit it.")
    userChoice()#displaying options
    employeeList = LinkedList()#creating object of the linked list class
    user = input("Enter your choice: ")#option selected by the user
    
    while True:
        
        if user == 'a':#adding a new employee
            
            employeeID = input('Enter the employee Id for the new employee: ') 
            
            #checking whether the employee with same id exists
            if employeeList.find(employeeID) != -1:
                print("Employee with same Id already exists.")
                
            else:
                bool = True
                while bool:
                    try:    
                        payRate = float(input('Enter the hourly pay for the employee: '))
                        #checking whether payrate is less than 6
                        while payRate < 6.00:
                    
                            if payRate < 0.00:
                                print("Hourly pay cannot be less than zero.")
                                payRate = float(input('Enter hourly pay: '))
                    
                            else:
                                print("Hourly pay must be greater than or equal to 6.")
                                payRate = float(input('Enter hourly pay: '))
                        bool = False
                    except:
                        print("Pay should be a floating point number.")
                #creating employee class object
                employee = Employee(employeeID , payRate)
                #adding the employee to the linked list
                employeeList.add(employee) 
            
        elif user == 'b':
            
            current = employeeList.head
            while current is not None:
                employeeID = current.getEmployeeID()
                #inputting the hours worked by each employee
                bool = True
                while bool:
                    try:#checking whether the pay is a floating point number or not
                        hoursWorked = float(input('Enter hours worked by Emp %s: ' % str(employeeID)))
                
                        while hoursWorked < 0.00:#verifying hours worked is not less than 0
                            print("Number of hours worked cannot be less than zero.")
                            hoursWorked = float(input('Enter hours worked by Emp %s: ' % str(employeeID)))
                        current.employee.setHoursWorked(hoursWorked)#setting the hours of the employee
                        current.employee.setWage()#calculating the wage
                        current = current.nextEmployee
                        bool = False
                    except:
                        print("Hours should be a floating point number.")
                
            print("Wages have been calculated for the employees in the list. Select \"Display Payroll\" to view them.")
            
        elif user == 'c':
            
            current = employeeList.head
            #displaying payroll for the employees present in the list
            if employeeList.empty():
                print("There are currently no employees in the list.")
                
            else:
                print('\n *** Payroll ***\n')
                while current is not None:
                    print(current.employee)
                    current = current.nextEmployee
                    
        elif user == 'd':
            
            employeeID = input('Enter the id of the employee: ')
            #checking whether the employee is in the list
            index = employeeList.find(employeeID)
            
            if index >= 0:
                employeee = employeeList[index]#accessing the information of the employee whose pay has to be updated
                #inputting new pay rate
                bool = True
                while bool:
                    try:#checking whether the pay is a floating point number or not
                        newPayRate = float(input('Enter new hourly pay for employee %s:' %(str(employeeID))))
                        #checking whether payrate is less than 6 or not
                        while newPayRate < 6.00:
                            if newPayRate < 0.00:
                                print("Hourly pay cannot be less than zero.\n")
                                newPayRate = float(input('Enter new hourly pay for employee %s:' %(str(employeeID))))
                            else:
                                print("Hourly pay must be greater than or equal to 6.\n")
                                newPayRate = float(input('Enter new hourly pay for employee %s:' %(str(employeeID))))
                        #updating pay    
                        employeee.setHourlyPay(newPayRate)#setting new pay for the user
                        employeee.setWage()#calculating new wage
                        print("Pay rate for employee %s updated sucessfully." % str(employeeID))
                        bool = False
                    except:
                        print("Pay should be a floating point number.")
                
            else:
                print('No employee with %s id was found.' % (str(employeeID)))
            
        elif user == 'e':
            
            if employeeList.empty():#checking whether the list is empty or not
                print("Employee List is empty.")
                
            else:
                #deleting an employee from the list
                employeeID = input('Enter the id of the employee: ')
                employeeList.delete(employeeID)
            
        else:
            #ending the program
            print("Terminating The simulator....")
            time.sleep(1)
            break
        
        userChoice()#displaying the choices till the user decides to quit the program
        user = input("Enter your choice:")#asking the user for the choice again
        print()


