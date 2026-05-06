#playing the game rock,paper and sciccors using computer and user input

import random

choices = ['rock','paper','sciccors']

computer = random.choice(choices)

player_1 = input('enter your choice')

#allowing the computer to pick randomly form the choices given


print(f'computer choice is {computer}')
print(f'your choice is {player_1}')

#comparing computer and player_1

if computer == player_1:
    print ('its a draw')
#rock and paper
elif computer =='rock' and player_1 == 'paper':
    print ('computer loses:player_1 wins')
    
elif computer =='paper' and player_1 == 'rock':
    print('you lose:computer wins')

# sciccors and paper
elif player_1 == 'sciccors' and computer == 'paper':
     print ('computer loses : player_1 wins') 

elif player_1 == 'paper' and computer == 'sciccors':
     print ('You lose : computer wins') 

#sciccors and rock

elif player_1 == 'sciccors' and computer == 'rock':
     print ('computer win : player_1 lose') 

elif player_1 == 'rock' and computer == 'sciccors':
     print ('You win : computer loses') 
else:
    print("invalid")
  





