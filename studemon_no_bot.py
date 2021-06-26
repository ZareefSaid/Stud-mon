'''
import random



player_health = 10

enemy_health = 10

randomnum = random.randrange(0, 6)

global forever

forever = 0

def game():
  global player_health

  global enemy_health

  global action

  global accuracy


  action = input('Would you like to Punch, Kick, Heal, or Run?\n')

  questions = ['1+1', '2+2', '3+3', '4+4','5+5', '6+6']

  if (action == 'Run'):
    quit()
  if randomnum == 0:
    correctanswer = '2'

  if randomnum == 1:
    correctanswer = '4'

  if randomnum == 2:
    correctanswer = '6'

  if randomnum == 3:
    correctanswer = '8'

  if randomnum == 4:
    correctanswer = '10'

  if randomnum == 5:
    correctanswer = '12'


  answer = input(f'{questions[randomnum]}\n')

  if answer == correctanswer:
    if action == 'Punch':
      print("Correct!")
      accuracy = random.randrange(1, 15)
      if accuracy != 15:
        enemy_health = enemy_health - 1
        print('You dealt 1 damage!')
        print(f'Your Health: {player_health}\nEnemys Health: {enemy_health}')
      else:
        print('Your attack missed!')
        print(f'Your Health: {player_health}\nEnemys Health: {enemy_health}')
    if action == 'Kick':
      print("Correct!")
      accuracy = random.randrange(1, 3)
      if accuracy == 1:
        enemy_health = enemy_health - 3
        print('You dealt 3 damage!')
        print(f'Your Health: {player_health}\nEnemys Health: {enemy_health}')
      else:
        print('Your attack missed!')
        print(f'Your Health: {player_health}\nEnemys Health: {enemy_health}')
    if action == "Heal":
      print("Correct!")
      player_health = player_health + 1
      print(f'Your Health: {player_health}\nEnemys Health: {enemy_health}')
  else:
    print("Incorrect")
    player_health = player_health - 1
    print(f'Your Health: {player_health}\nEnemys Health: {enemy_health}')

while (forever == 0):
  if (player_health <= 0):
    print('You Loose!')
    quit()
  if (enemy_health <= 0):
    print('You Win!')
    quit()
  if (player_health > 0 and enemy_health > 0):
    game()
'''