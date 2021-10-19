'''
===============================================================================
ENGR 133 Program Description 
    This creates the new file for the user that contains answers to the 
    questions that the user got wrong
    
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
def makeVocabFile(filename, vocabDict):
   filename=(filename)+('.txt')#uses input and appends '.txt' to it
   fd = open(filename, "w")#opens a new file as write only as fd
   fd.write('ENGLISH : FRENCH\n')# print those words in the newly made file 
   for engWord in vocabDict.keys():
      fd.write(engWord + " : ")# for every English Word that the user got wrong, prints in the word in the new file
      fd.write(str(vocabDict[engWord]).replace('[','').replace(']', '').replace("\', \'",",").replace("\'","")) #prints the correct french word in the file
      fd.write('\n')# moves the cursor to the next line in the new file
   fd.close()# closes the file
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''