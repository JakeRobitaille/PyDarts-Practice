import bulls
import doublestriples
import randout
import stats
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
        stats.addInfo('bull-games.json', bulls.BULLS().practice_bulls())
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playBulls()
     
# Plays Doubles practice and appends the info on a csv file      
def playDoubles():
    cls()
    answer = basicGameMenu()
    if answer == '1':
       cls()
       doublestriples.DUB_TRIP().dart_track('double', '../tracking-files/doubles.csv')
       endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playDoubles()

# Plays Triples practice and appends the info on a csv file      
def playTriples():
    cls()
    answer = basicGameMenu()
    if answer == '1':
        cls()
        doublestriples.DUB_TRIP().dart_track('triple', '../tracking-files/triples.csv')
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playTriples()
  
# Gives random out to get in 3 darts and appends the info on a csv file
def play3Out():
    cls()
    answer = basicGameMenu()
    if answer == '1':
        cls()
        randout.rand_out().three_out('../tracking-files/random-out.csv')
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        play3Out()
        
# Gives random out to throw for until you get it and appends the info on a csv file
def playUntilOut():
    cls()
    answer = basicGameMenu()
    if answer == '1':
        cls()
        randout.rand_out().until_out('../tracking-files/random-out.csv')
        endOfMenu()
    elif answer == '2':
        cls()
        mainMenu()
    else:
        print('\nThat is not an option...\n')
        endOfMenu()
        playUntilOut()
    
def historyMenu():
    def outputProcess(file):
        cls()
        # readwrite.readFrom(file)
        endOfMenu()
        historyMenu()
    
    cls()
    print('''Which practice stats would you like to view?
All practices are formatted as a CSV (comma seperated values) file.
          1) Bulls
          2) Doubles            
          3) Triples
          4) Random Out (ALL)
          
          5) Clear History
          6) Back''')
    answer = input('\nYour Choice (1-6) ------------> ')
    
    if answer == '1':
        outputProcess('../tracking-files/bulls.csv')
    elif answer == '2':
        outputProcess('../tracking-files/doubles.csv')
    elif answer == '3':
        outputProcess('../tracking-files/triples.csv')
    elif answer == '4':
        outputProcess('../tracking-files/random-out.csv')
    elif answer == '5':
        clearHistoryMenu()
    elif answer == '6':
        cls()
        mainMenu()
    else:
        print('\nThat is not a valid option, try again...\n')
        endOfMenu()
        historyMenu()
     
def clearHistoryMenu():
    def clearHistoryProcess(file, type):
        cls()
        # readwrite.clearHistory(file, type)
       
        if type == 'bulls':
            fileType = 'BULLS'
        elif type == 'doubles':
            fileType = 'DOUBLES'
        elif type == 'triples':
            fileType = 'TRIPLES'
        elif type == 'randout':
            fileType = 'RANDOM OUT'
        else:
            print('There is no type specified.')
            
        print(f'\n-- YOUR {fileType} FILE HAS BEEN OVERWRITTEN! --\n')
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
        clearHistoryProcess('../tracking-files/bulls.csv', 'bulls')
    elif answer == '2':
        clearHistoryProcess('../tracking-files/doubles.csv', 'doubles')
    elif answer == '3':
        clearHistoryProcess('../tracking-files/triples.csv', 'triples')
    elif answer == '4':
        clearHistoryProcess('../tracking-files/random-out.csv', 'randout')
    elif answer == '5':
        cls()
        # readwrite.clearHistory('../tracking-files/bulls.csv', 'bulls')
        # readwrite.clearHistory('../tracking-files/doubles.csv', 'doubles')
        # readwrite.clearHistory('../tracking-files/triples.csv', 'triples')
        # readwrite.clearHistory('../tracking-files/random-out.csv', 'randout')
        print('\n-- ALL FILES HAVE BEEN OVERWRITTEN!! --\n')
        endOfMenu()
        mainMenu()
    elif answer == '6':
        cls()
        historyMenu()
    else:
        print('\nThat is not a valid option, try again...\n')
        endOfMenu()
        clearHistoryMenu()
        
    historyMenu()
        
# Runs the menu
mainMenu() 