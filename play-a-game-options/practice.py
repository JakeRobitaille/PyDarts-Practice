# Function to create the lists of numbers
bull = 25
def dart_numbers(dartMult):
    elemList = []
                 
    for i in range (20):
        elemList.append((i + 1) * dartMult)
    else:
        elemList.append(bull * dartMult)
        if dartMult >= 3:
            elemList.pop()
            
    return elemList
        
doubles = dart_numbers(2)
triples = dart_numbers(3)

class DARTS_DOUBLES(self, ):

# # Function to keep track of hits
# def dart_hits(target):
#     for i in target:
#         dartHit = False
#         throwCount = 1
#         while dartHit == False:
#             print(f"Throw: {throwCount}")
#             answer = input("Hit? Y / N")
#             if answer == 'y' or 'Y':
#                 dartHit = True
#                 return throwCount
#             else:
#                 throwCount += 1