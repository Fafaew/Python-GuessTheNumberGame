from random import randint
computer = randint(0, 10)
print('Hi! My name is Alicia and i just thought on a number beteween 0 and 10. Can you guess what number did i think?')
hit = False
guess = 0
while not hit:
    player = int(input('What is yout guess? '))
    guess += 1
    if player == computer:
        hit = True
    else:
        if player < computer:
            print('up')
        elif player > computer:
            print('Down')
print(' You did it! Found the right answer with {} attempts'.format(guess))