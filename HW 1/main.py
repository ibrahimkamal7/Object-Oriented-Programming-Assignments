#Author: Ibrahim Kamal
#Lecture Section: 172-A
#Lab Section: 172-064
#Homework Assignment 1

from question import *

if __name__ == '__main__':
    
    #creating question objects
    question1 = question()
    question2 = question()
    question3 = question() 
    question4 = question()
    question5 = question()
    question6 = question()
    question7 = question()
    question8 = question()
    question9 = question()
    question10 = question()
    
    #question object stored in a list
    prompts = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]
    
    #lists to store question prompts, answer choices, and the correct choice
    questions=["In chess, which piece can move only diagonally?","In chess, which piece can move only horizontally and vertically?","Whon won the main event of Wrestlemania 35?","Who defeated Undertaker at Wrestlemania for the first time?","Who founded Facebook?","Who founded Microsoft?","When was Harvard founded?","When was Stanford founded?","Who is the richest man in the world?","For whose murder was Mohammad Bin Salman accused of?"]
    ch1=["1. Bishop","1. Bishop","1. Becky Lynch","1. John Cena","1. Mark Zuckerberg","1. Mark Zuckerberg","1. 1885","1. 1636","1. Bill Gates","1. Jamal Khashoggi"]
    ch2=["2. Rook","2. Rook","2. Seth Rollins","2. Roman Reigns","2. Jeff Bezos","2. Steve Jobs","2. 1636","2. 1500","2. Larry Page","2. Donald Trump"]
    ch3=["3. Queen","3. Queen","3. Brock Lesnar","3. Brock Lesnar","3. Steve Jobs","3. Bill Gates","3. 1891","3. 1891","3. Jeff Bezos","3. Narendra Modi"]
    ch4=["4. Pawn","4. Pawn","4. Ronda Rousy","4. Seth Rollins","4. Bill Gates","4. Jeff Bezos","4. 1900","4. 1885","4. Mark Zuckerberg","4. Bill Gates"]
    cc=[1,2,1,3,1,3,2,4,3,1]
    
    player1_points = 0
    player2_points = 0
    
    turn = 1
    
    print("Welcome to the Python general knowledge quiz!")
    print("--------------------------------------------"+"\n")
    print("Rules of the quiz are as follows:"+"\n")
    print("This is a two player multiple choice quiz. Each player has to answer 5 question with multiple choices. Every time a player answers correctly, he/she will gain 1 point. There is  no negative marking for answering incorrectly. Players have to take turn one by one."+"\n")
               
    #function to set question prompts, answer choice, and the correct choice. It also validates user input.
    def userChoice(turn, i):
        
        print("Player",turn,"here is your question:")
        print()
        prompts[i].setQuestionPrompt(questions[i])
        prompts[i].setC1(ch1[i])
        prompts[i].setC2(ch2[i])
        prompts[i].setC3(ch3[i])
        prompts[i].setC4(ch4[i])
        prompts[i].setCorrectChoice(cc[i])
        print(prompts[i].__str__())
 
        bool=True
        while bool:
            try:
                choice_user = int(input("Enter your answer:"))
                userPoints(choice_user, turn, i)
                bool = False
            except ValueError:
                print("Error! Enter a valid choice between 1 and 4")
    
    #function to increment player points if the entered answer is correct
    def userPoints(choice_user, turn, i):
        
        global player1_points
        global player2_points
        while choice_user < 1 or choice_user > 4:
            print("Error! Enter a valid choice between 1 and 4")
            choice_user = int(input("Enter your answer:"))
        if choice_user == prompts[i].getChoice() and turn == 1:
            print("Excellent! You score!\n")
            player1_points += 1
        elif choice_user == prompts[i].getChoice() and turn == 2:
            print("Excellent! You score!\n")
            player2_points += 1
        else:
            print("That is incorrect. Better luck with the next question.\n")
    
    #loop for carrying out the game
    i = 0
    while i < 10:
        if turn == 1:
            userChoice(turn, i)
            turn = 2
        else:
            userChoice(turn, i)
            turn = 1
        i += 1
        
    #printing the final score and the winner
    print("And the final scores are:")
    print("Player 1:", player1_points)
    print("Player 2:", player2_points)
    
    if player1_points > player2_points:
        print("Player 1 Wins!")
    elif player1_points < player2_points:
        print("Player 2 Wins!")
    else: 
        print("The game is tied.")



    

