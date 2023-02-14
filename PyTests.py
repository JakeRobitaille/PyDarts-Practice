def is_hit():
    throwCounter = 1
    # hit = False
            
    # while True:
    #     answer = input(f'Did you hit it? Y / N \n')
    #     if answer == 'n' or 'N':
    #         throwCounter += 1
    #         print(throwCounter)
    #     elif answer == 'y' or 'Y':
    #         print('Good Job!')
    #         break
    #     else:
    #         print('That is not a valid answer, try again:')

    answer = input(f'Did you hit it? Y / N \n')
    print(f'''{answer}
          {type(answer)}''')
    if answer == 'n':
        print('')
        throwCounter += 1
        print(throwCounter)
    elif answer == 'y':
        print('Good Job!')
    else:
        print('That is not a valid answer, try again:')
            
    print(throwCounter)

is_hit()