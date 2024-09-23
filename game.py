import random

value = random.randint(1, 100)
response = int((input("1-100, take a guess >:] ")))

while response != value:
  if response > value:
    print('too high "overachiever" hahahahaha >:] ')
    response = int(input('\ntry again: '))
  elif response < value:
    print('undershooting is a sign of laziness! >:] ')
    response = int(input('\ntry again: '))
if response == value:
  print(f'you got lucky this time... {response} was the number...')