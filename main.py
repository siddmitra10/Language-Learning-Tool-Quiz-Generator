'''
===============================================================================
Program Description 
    It is an interactive quiz for the students who want to learn, or 
    strengthen their French vocabulary skills.
    
Author:         Siddharth Mitra, mitra30
===============================================================================
'''
#_________This section is for importing all the necessary modules______________
import glob
import random
from makeVocabFile import makeVocabFile
from quizQuestion import quizQuestion
from createDict import createDict
from quit_option import quit_option
#______________________User Defined Function: main_____________________________
def main():
   fileList = glob.glob("*.txt") # searhes for all text files in the folder with extention '.txt'
   if len(fileList) == 0: #checks if there are no lists available 
      print ("There are no vocab lists available!")
      return
   print ("Welcome to the vocabulary quiz program. Select one of the following word lists:")
   i=1# incrementation factor
   while i<len(fileList): #iterates if the value of i is less that length of fileList
       for file in fileList: #iterates through every file in fileList
           filenames=file.strip('.txt')#removes '.txt' from names of file
           print (f"\t{i}. {filenames}")# indents and prints names of the file
           i+=1 # incrementation for the while loop
   print("-------------------------------------------------------")
   print('Type "quit" or "exit" in case you want to quit the game')
   print("-------------------------------------------------------")
   filename = input("Please make your selection: ") #asks user for name of the category as input and assigns it to filename
   quit_option(filename)#gives the option to quit
   filename=filename+'.txt'# adds '.txt' to filename
   while filename not in fileList: #iterates as long as the filename that user has input is not there in fileList
      print("\n\n-------------------------------------------------------")
      print('Type "quit" or "exit" in case you want to quit the game')
      print("-------------------------------------------------------")
      filename = input("Please make a valid selection: ") #again asks user for a valid input and assigns to filename
      quit_option(filename)#gives option to quit
      filename=filename+'.txt'#adds '.txt' to filename
   vocabDict = createDict(filename) #calls in fuction createDict with filename as value of keyword argument
   print("\n\n-------------------------------------------------------")
   print('Type "quit" or "exit" in case you want to quit the game')
   print("-------------------------------------------------------")
   noQs = input(str(len(vocabDict)) + " entries found.  How many words would you like to be quizzed on? ") #asks user for how many questions it wants to be quizzed on and assigns it to noQs
   quit_option(noQs)#gives option to quit
   while noQs=="":#iterates as long as user doesnt input anything
       print("Please type an input.")
       noQs=input("How many words would you like to be quizzed on? ")#again asks for no of questions and assigns to noQs
       quit_option(noQs)#gives option to quit
   try:
       noQs = int(noQs)#tries if the user input can be converted to int type
   except:
       while noQs.isalpha() or noQs.isalnum(): #runs if first condition is not runnable and iterates as long as the input contains an alphabet
           noQs=input('You input contains an alphabet. Please enter a number or type "quit" or "exit" in case you want to quit the game: ')#asks user for a valid input and assigns to noQs
           quit_option(noQs)#gives option to quit
           if noQs.isdigit():
               break#breaks out of the while loop if the input contains only a number
   noQs = int(noQs)# converts noQs to int type
   while(noQs < 1 or noQs > len(vocabDict)):#iterates if user input is less than zero or larger than no of available questions
      print("-------------------------------------------------------")
      print('Type "quit" or "exit" in case you want to quit the game')
      print("-------------------------------------------------------")
      noQs = input("Invalid input.  Please try again: ")#prompts user for a valid input and assigns to noQs
      quit_option(noQs)#gives option to quit
      noQs=int(noQs)#converts noQs to int type
   print('\n\n-------------------------------------------------------')
   print("Okay. So let's start the quiz.")
   print('-------------------------------------------------------')
   quizList = random.sample(vocabDict.keys(), noQs) #creates a list of random words from keys of vocabDict, same in number as noQs and assigns it to quizList
   numCorrect = 0#inital no. of correct questions
   incorrectDict = {} #dictionary for incorrect questions
   for word in quizList: #iterates through every word in quizlist
      if quizQuestion(word, vocabDict[word][:]) == True: #calls quizQuestion UDF and if function returns value 'True', add 1 to numCorrect
         numCorrect += 1#explained in previous comment
      else:
         incorrectDict[word] = vocabDict[word]#if answer is incorrect, assigns the word as key to english words and then adds it to incorrectDict
   print (f'You got {str(numCorrect)} out of {str(noQs)} correct.')#gives the user their score
   if numCorrect != noQs:#checks if the noQs is not equal to numCorrect
      filename = input("Enter an output file (or press enter to quit): ") #prompts user regaarding what they want to name their file and assigns it to filename
      if filename != "": #checks if user pressed enter when prompted for filename 
         makeVocabFile(filename, incorrectDict) #calls UDF makeVocabFile
      print('Thank you for playing the game.')
      print('-------------------------------------------------------')
   elif numCorrect==noQs: #checks if numCorrect is equal to noQs
      print('Congratulations! You got all correct! Keep up the good work!')
      print('-------------------------------------------------------')
   opinion=input('Do you want to play again ? ') #asks user if he/she wants to play again and assigns the input to opinion
   if opinion=='yes':#checks if opinion is 'yes'
      print('\n\n')
      main()#calls UDF main() 
   else: #executes the following code if opninion is not 'yes'
        print('-------------------------------------------------------')
        print('THANK YOU! Have a great day!')
        print('-------------------------------------------------------')
#______________________________________________________________________________
main() #calls the UDF main()

#______________________________________________________________________________
