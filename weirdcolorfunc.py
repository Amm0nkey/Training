

def cool_func(color, day, year=2022):
  if year != 2022:
    print(f'{color},{day},{year}')
    return False
  else:
    return f' '
    

if cool_func("red","today", 2023):
  print("it worked")
else:
  print("did not work")

print(cool_func('blue', 'yesterday', 2022) == True)