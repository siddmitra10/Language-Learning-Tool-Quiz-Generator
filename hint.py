'''
===============================================================================
ENGR 133 Program Description 
    It is user defined function that creates a hint to help the user guess the 
    answer
    
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
def hint(freWords):
    list_of_letters=list(freWords[0])# takes the first element of list of correct answers and converts its alphabets into a list and assigns it to list_of_letters
    hint=str(list_of_letters[0]+list_of_letters[1])# assigns first and second letter of list_of_letters as hint and converts it to string
    hint=hint.upper() #converts hint to uppercase
    print(f'Here is a hint to help you out - The answer starts with "{hint}"')
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''