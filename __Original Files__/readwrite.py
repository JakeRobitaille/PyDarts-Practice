def writeTo(file, info):
    a = open(file, 'a')
    a.write(info)
    a.close()


def readFrom(file):
    r = open(file, 'r')
    fileOutput = r.read()
    print(fileOutput)
    r.close()


def clearHistory(file, type):
    bullContent = 'Darts Thrown, Darts Hit, Singles, Doubles, Misses, Average Hit %, Points Out of Total, Date\n'
    doubleContent = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, Bull, Date\n'
    tripleContent = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, Date\n'
    randOutContent = 'Random Number, Out In 3?, Darts to Out, Date\n'
    
    ch = open(file, 'w')  
  
    if type == 'bulls':
        ch.write(bullContent)
    elif type == 'doubles':
        ch.write(doubleContent)
    elif type == 'triples':
        ch.write(tripleContent)
    elif type == 'randout':
        ch.write(randOutContent)
    else:
        print('There is no type specified.')
    
    ch.close()