import random

word_list = ['knife', 'bullet', 'coward', 'young', 'pistol', 'gallop', 'general', 'commander', 'knowledge', 'underdog', 'achieve', 'fighter', 'commonfolk', 'exclucive', 'service', 'physics', 'boulder', 'bravery', 'hillbilly', 'herald']

name = input('what is your name?: ')
print('Detective ' + name + ' we have to save this man who is wrongly\n accused!!!')

print('start searching for evidence! (enter a character): ')

word = random.choice(word_list)
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for characters in word:
      if characters in guesses:
        print(characters, end = ' ')
      
      else:
        print('_', end=' ')
        failed += 1
    print('')  
    if failed == 0:
      print('The mans innocence was proven.')

      break
    guess = input('Find some evidence quick!!: ')
    guesses += guess

    if guess not in word:
      turns -= 1
      print('wrong')
      if turns == 1:
        print('The Final Day Dawns...')
      else:
        print(f'{turns} days till execution...')

    if turns == 0:
      print('The rope is taught...')
      break