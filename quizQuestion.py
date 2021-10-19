'''
===============================================================================
Program Description 
    Quizzes the user on one specific English word
Author:         Siddharth Mitra, mitra30
===============================================================================
'''
def quizQuestion(engWord,freWords):
    from quit_option import quit_option
    from hint import hint
    incorrect = False# controls what is printed if answer is correct or incorret
    i = 1# incrementation factor
    print (f"\n\n-------------------------------------------------------\nEnglish word: {engWord}")
    print ("Enter " + str(len(freWords)) + " equivalent French word(s).")# asks the user to enter equiivalent french words
    while (len(freWords) > 0 and incorrect == False):
      print("-------------------------------------------------------")
      print('Type "quit" or "exit" in case you want to quit the game')
      print("-------------------------------------------------------")
      freWord = input("Word [" + str(i) + "]: ")# asks user for their answer
      freWord=freWord.lower()# makes the input lower case so that it matches the answer format
      quit_option(freWord) # gives option to quit
      if (freWord in freWords):# checks if the answer is correct
         freWords.remove(freWord)# removes the answer from list of correct answers in case there are 2
         i += 1# incrementation for the while loop
      else:
         print ("Incorrect. Please try again.")
         hint(freWords)# gives hint to the user
         print("-------------------------------------------------------")
         print('Type "quit" or "exit" in case you want to quit the game')
         print("-------------------------------------------------------")
         freWord = input("Word [" + str(i) + "]: ") # asks user for their answer
         quit_option(freWord) # gives option to quit
         if (freWord in freWords): # checks if the answer is correct
             freWords.remove(freWord)# removes the answer from list of correct answers in case there are 2
             i += 1# incrementation for the while loop
         else:
             print('Sorry you are out of attempts')
             incorrect=True # depicts the answer is wrong
    if not incorrect:
      print ("Correct!")
      print("-------------------------------------------------------")
      return not incorrect
