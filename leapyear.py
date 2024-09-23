# year = int(input('Enter a year after 1752 to see if it is a leap year: '))
# leap_year = False

# if year % 400 == 0:
#   leap_year = True
# elif year % 100 == 0:
#   leap_year = False
# elif year % 4 == 0:
#   leap_year = True

# print(leap_year)

def leap_year(year):
  if year < 1752:
    return False
  elif year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False
