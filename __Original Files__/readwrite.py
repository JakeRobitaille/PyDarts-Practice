import json

# The process for opening a JSON file and returning it as a Python Dict
def getFromFile():
    r = open('game-stats.json', 'r')
    json_data = json.load(r)
    r.close()
    return json_data

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
        #       This prints the key value pairs on seperate lines
        # print('---------')
        # for key in g:
        #     print(f'{key} : {g[key]}')
        # print()
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