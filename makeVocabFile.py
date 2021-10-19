'''
===============================================================================
Program Description 
    This creates the new file for the user that contains answers to the 
    questions that the user got wrong

Author:         Siddharth Mitra, mitra30
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
