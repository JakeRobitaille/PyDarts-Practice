import json

# The process for opening a JSON file and returning it as a Python Dict
def getFromFile():
    r = open('game-stats.json', 'r')
    json_data = json.loads(r)
    r.close()
    return json_data

def writeTo(type, info):
    fileData = getFromFile()
    a = open('game-stats.json', 'a')
        
    if type == 'bull':
        fileData["Bulls"].append(info)
    elif type == 'double':
        fileData["Doubles"].append(info)
    elif type == 'triple':
        fileData["Triples"].append(info)
    elif type == 'randout':
        fileData["RandOut"].append(info)
        
    toAdd = json.dumps(fileData, indent=2, separators=(',', ' : '))
    a.write(toAdd)
    a.close()

# The process of reading out from and closing a file
def readFrom(type):
    json_read = getFromFile()
    output = json.loads(json_read)
    
    if type == 'bull':
        print(output["Bulls"])
    elif type == 'double':
        print(output["Doubles"])
    elif type == 'triple':
        print(output["Triples"])
    elif type == 'randout':
        print(output["RandOut"])
    
    
    