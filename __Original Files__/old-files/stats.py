import json
import readwrite

# These are the catigories to keep track of
bullContent = ['Darts Thrown', 'Darts Hit', 'Singles', 'Doubles', 'Misses', 'Average Hit %', 'Points Out of Total', 'Date']
doubleContent = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'Bull', 'Date']
tripleContent = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 'Date']
randOutContent = ['Random Number', 'Out in 3?', 'Darts To Out', 'Date'] 


# Handles adding game info to a JSON file 
def addInfo(type, info):
    json.dumps(readwrite.writeTo(type, info), indent=2, separators=(',' , ' : '))


def outputInfo(type):
    pass
    

# Handles erasing information
def deleteInfo(type):
    if type == 'bull':
        pass
    elif type == 'double':
        pass
    elif type == 'triple':
        pass
    elif type == 'randout':
        pass 
    elif type == 'all':
        pass