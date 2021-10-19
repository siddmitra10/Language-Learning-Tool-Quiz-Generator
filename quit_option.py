'''
===============================================================================
ENGR 133 Program Description 
    gives the user an option to quit at point in the quiz
    
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
def quit_option(name_of_input):
    import sys # imports sys module
    if name_of_input=='quit':
        print(f'\n-------------------------------------------------------\nThank you for playing the game.\nSee you another time\n-------------------------------------------------------\n')
        sys.exit()#if input if quit, then quits runing the script
    elif name_of_input=='exit':
        print(f'\n-------------------------------------------------------\nThank you for playing the game.\nSee you another time\n-------------------------------------------------------\n')
        sys.exit()#if input if exit, then quits runing the script
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''