import bulls
import doublestriples
import randout
import readwrite
import os

cls = lambda: os.system('cls')

def mainMenu():
    while True:
        print('''What option would you like to choose?
          
            Practice Games:
            1) Bulls      (Specify a certain number of darts to shoot for bull)
            2) Doubles    (Shoot for each number in order until you hit the double)
            3) Triples    (Shoot for each number in order until you hit the triple)
            4) 3 Out      (Shoot 3 darts to get out on a random number)
            5) Until Out  (Shoot for a random number until you can get out)
              
            6) User History''')
    
        mainMenuOption = input('\nYour Choice (1-6) ------------> ')
    
        if mainMenuOption == '1':
            playBulls()
        elif mainMenuOption == '2':
            playDoubles()
        elif mainMenuOption == '3':
            playTriples()
        elif mainMenuOption == '4':
            play3Out()
        elif mainMenuOption == '5':
            playUntilOut()
        elif mainMenuOption == '6':
            historyMenu()
        else:
            print('\nThat is not a valid option, try again...\n')
            endOfMenu()

def basicGameMenu():
    print('''Would you like to:
          1) Play
          2) Go Back''')
    answer = input('\nYour Choice (1-2) ------------> ')
    return answer
        
def endOfMenu():
    input('######## click ENTER to continue ########')
    cls()
       
#  Plays Bulls practice and appends the info on a json file
def playBulls():  
    cls()  
    answer = basicGameMenu()
    if answer == '1':
        cls()
        bullGame = bulls.BULLS() 
        readwrite.writeTo('Bulls', bullGame.practice_bulls())
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playBulls()
     
# Plays Doubles practice and appends the info on a json file      
def playDoubles():
    cls()
    answer = basicGameMenu()
    if answer == '1':
       cls()
       doubleGame = doublestriples.DUB_TRIP()
       readwrite.writeTo('Doubles', doubleGame.dart_track('double'))       
       endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playDoubles()

# Plays Triples practice and appends the info on a json file      
def playTriples():
    cls()
    answer = basicGameMenu()
    if answer == '1':
        cls()
        tripleGame = doublestriples.DUB_TRIP()
        readwrite.writeTo('Triples', tripleGame.dart_track('triple'))        
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playTriples()
  
# Gives random out to get in 3 darts and appends the info on a json file
def play3Out():
    cls()
    answer = basicGameMenu()
    if answer == '1':
        cls()
        randGame = randout.rand_out()
        readwrite.writeTo('RandOut', randGame.three_out())
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        play3Out()
        
# Gives random out to throw for until you get it and appends the info on a json file
def playUntilOut():
    cls()
    answer = basicGameMenu()
    if answer == '1':
        cls()
        randGame = randout.rand_out()
        readwrite.writeTo('RandOut', randGame.until_out())
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playUntilOut()
    
def historyMenu():
    def outputProcess(game):
        cls()
        readwrite.readFrom(game)
        endOfMenu()
        historyMenu()
    
    cls()
    print('''Which practice stats would you like to view?
          1) Bulls
          2) Doubles            
          3) Triples
          4) Random Out (ALL)
          
          5) Clear History
          6) Back''')
    answer = input('\nYour Choice (1-6) ------------> ')
    
    match answer:
        case '1':
            outputProcess("Bulls")
        case '2':
            outputProcess('Doubles')
        case '3':
            outputProcess('Triples')
        case '4':
            outputProcess('RandOut')
        case '5':
            clearHistoryMenu()
        case '6':
            cls()
            mainMenu()
        case _:
            print('\nThat is not a valid option, try again...\n')
            endOfMenu()
            historyMenu()
     
def clearHistoryMenu():
    def clearHistoryProcess(type):
        cls()
        readwrite.writeOver(type)
            
        if type == 'all':
            print('\n-- ALL FILES HAVE BEEN OVERWRITTEN!! --\n')
        else:
            print(f'\n-- YOUR {type.upper()} GAMES HAVE BEEN OVERWRITTEN! --\n')
        endOfMenu()
        clearHistoryMenu()
        
    cls()
    print('''Which file history would you like to clear?
    ***THIS CAN NOT BE UNDONE!!***
          1) bulls.csv
          2) doubles.csv
          3) triples.csv
          4) random-out.csv
          5) ALL Files
          
          6) Back''')
    answer = input('\nYour Choice (1-6) ------------> ')
    
    if answer == '1':
        clearHistoryProcess('Bulls')
    elif answer == '2':
        clearHistoryProcess('Doubles')
    elif answer == '3':
        clearHistoryProcess('Triples')
    elif answer == '4':
        clearHistoryProcess('RandOut')
    elif answer == '5':
        clearHistoryProcess('all')
    elif answer == '6':
        cls()
        historyMenu()
    else:
        print('\nThat is not a valid option, try again...\n')
        endOfMenu()
        clearHistoryMenu()
        
    historyMenu()
        
# Runs the main application
mainMenu()