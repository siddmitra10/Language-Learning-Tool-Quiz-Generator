'''
===============================================================================
Program Description 
    gives the user an option to quit at point in the quiz
Author:         Siddharth Mitra, mitra30
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
