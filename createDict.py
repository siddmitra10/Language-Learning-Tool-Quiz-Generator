'''
===============================================================================
ENGR 133 Program Description 
    creates a dictionary of english and french word based on a file 
    containing vocabulary words.
    
Assignment Information
	Assignment:     Individual Project
	Author:         Siddharth Mitra, mitra30
	Team ID:        002-17
	
Contributor:    Name, login@purdue [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
def createDict(filename):
   vocabDict = {} # creates a new empty dictionary
   fd = open(filename, "r") # opens the file as read only type as fd
   for line in fd: #iterates through every line in fd
      line = line.strip() #strips all the empty spaces before and after the text
      tokens = line.split(":") # splits the text of the line at ':' and assigns the list to tokens
      engWord = tokens[0]#assigns the first element in the tokens to engWord 
      freWords = tokens[1]#assigns the second element in the tokens to freWords
      freWordList = freWords.split(",") # splits the text of the frewords at ',' and assigns the list to freWordList
      vocabDict[engWord] = freWordList# assigns engWord as key to freWordList and adds to vocabDict
   fd.close()# closes file
   return vocabDict  #returns vocabDict
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''