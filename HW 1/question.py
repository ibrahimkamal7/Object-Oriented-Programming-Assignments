#Author: Ibrahim Kamal
#Lecture Section: 172-A
#Lab Section: 172-064
#Homework Assignment 1

class question:
    
    def __init__(self):
        self.__questionPrompt = ""
        self.__choice1 = ""
        self.__choice2 = ""
        self.__choice3 = ""
        self.__choice4 = ""
        self.__correctChoice = 0
    
    #Mutator Methods
    def setQuestionPrompt(self,q):
        self.__questionPrompt = q
    
    def setC1(self,c1):
        self.__choice1 = c1
        
    def setC2(self,c2):
        self.__choice2 = c2
        
    def setC3(self,c3):
        self.__choice3 = c3
        
    def setC4(self,c4):
        self.__choice4 = c4
        
    def setCorrectChoice(self,cc):
        self.__correctChoice = cc
    
    #method to return the question along with answer choices
    def __str__(self):
        ques = self.__questionPrompt + '\n' + self.__choice1 + '\n' + self.__choice2 + '\n' + self.__choice3 + '\n' + self.__choice4
        return ques
    
    #Accesoor Method
    def getChoice(self):
        return self.__correctChoice
    