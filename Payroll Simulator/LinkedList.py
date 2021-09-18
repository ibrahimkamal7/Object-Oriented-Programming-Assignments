#Ibrahim Kamal
#ik363
#Linked List Class
#A portion of the code is taken from the code provided in the class
#Medlock, A(2019). LinkedListDemo[Source Code]

from Node import Node
from Employee import Employee

class LinkedList:
    
    def __init__(self):#constructor
        
        self.head = None

    def empty(self):#checking whether linked list is empty or not
        
        if self.head == None:
            return True
        
        else:
            return False
        
    def __getitem__(self , counter):#overloadable function to access the information at the given index
        
        current = self.head
        for i in range(counter):
            current = current.nextEmployee
            
        return current.getEmployee()

    def add(self , employee):#function to add a new employee node
        
        newEmployee = Node(employee , None)
        if self.head is None:
            self.head = newEmployee
            
        else:
            current = self.head
            while current.nextEmployee != None:
                current = current.nextEmployee
            current.nextEmployee = newEmployee
        
    def find(self , employeeID): #function to find the index of the employee whose id is given
        
        current = self.head
        counter = 0
        
        while current is not None:
            if current.getEmployeeID() == employeeID:
                return counter
            else:
               current = current.nextEmployee
               counter += 1
               
        return -1

    def delete(self , employeeID):#function to delete an employee
        
        index = self.find(employeeID)
        current = self.head
        previous = None
        
        if index == -1:#displaying message if the employee is not found
            print('No employee with %s id was found.' % (str(employeeID)))
            return
        
        elif index == 0:#employee is found at the starting index
            self.head = current.nextEmployee
        
        else:
            #employee is found in the middle or the end of the list
            for i in range(index):
                previous = current
                current = current.nextEmployee
                
            previous.nextEmployee = current.nextEmployee
        
        print("Employee with id %s removed from the list." %(str(employeeID)))
