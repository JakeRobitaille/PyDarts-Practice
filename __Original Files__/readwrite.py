import json

# The process for opening a JSON file and returning it as a Python Dict
def getFromFile():
    try:
        r = open('game-stats.json', 'r')
    except:
        createFile()
        
    r = open('game-stats.json', 'r')
    json_data = json.load(r)
    r.close()
    return json_data

# Creates a .json file if none exists
def createFile ():
    x = open('game-stats.json', 'x')
    content = {
        "Bulls" : [],
        "Doubles" : [],
        "Triples" : [],
        "RandOut" : []
    }
    baseInfo = json.dumps(content, indent=2, separators=(',', ' : '))
    x.write(baseInfo)
    x.close()

def writeTo(type, info):
    fileData = getFromFile()
    w = open('game-stats.json', 'w')
    fileData[type].append(info)
    toAdd = json.dumps(fileData, indent=2, separators=(',', ' : '))
    w.write(toAdd)
    w.close()

# The process of reading out from and closing a file
def readFrom(game):
    json_read = getFromFile()
    i = 1
    
    print(game.upper(), '\n')
    for g in json_read[game]:
        print(f'GAME {i}:')
        print(g, '\n')
        i += 1    
    
def writeOver(type):
    manipulateFile = getFromFile()
    o = open('game-stats.json', 'w')
   
    if type == 'all':
        manipulateFile["Bulls"].clear()
        manipulateFile["Doubles"].clear()
        manipulateFile["Triples"].clear()
        manipulateFile["RandOut"].clear()
    else:
        manipulateFile[type].clear()
            
    toAdd = json.dumps(manipulateFile, indent=2, separators=(',', ' : '))
    o.write(toAdd)
    o.close