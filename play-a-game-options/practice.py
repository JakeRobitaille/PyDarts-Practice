# Global variables to use
bull = 25

# Function to create the lists of numbers
def dart_numbers(dartMult):
    elemList = []
                 
    for i in range (20):
        elemList.append((i + 1) * dartMult)
    else:
        elemList.append(bull * dartMult)
        if dartMult >= 3:
            elemList.pop()
            
    return elemList
        
singles = dart_numbers(1)
doubles = dart_numbers(2)
triples = dart_numbers(3)
        