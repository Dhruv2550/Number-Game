import random
rounds = int(input('How many rounds do you want to play?'))
pscore = 0
cscore = 0
for x in range(rounds):
    computer = random.randint(1, 5)
    print(f'Round {x+1}')
    number = input('Guess the random number between 0 to 6\n')
    if number == computer:
        print('You guessed correctly')
        pscore = pscore + 1

    else:
        print('Try again')
        cscore = cscore + 1

print(f'{cscore} and {pscore}')





