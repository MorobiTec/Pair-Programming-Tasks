import random as rd
num = rd.randint(1,100)
guess_count = 0

while True : 
    print('Guess a  number between 1 and 100')
    guess = int(input('Enter a number : '))
    guess_count +=1
    
    if guess == num : 
        print('Congratulations. Total Try = {}'.format(guess_count))
        break
    elif guess < num : 
        print('Higher!')
    else : 
        print('Lower!')