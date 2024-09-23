def print_month_calender(month, year, start_day_of_week,days_in_month):
  current_day_of_week = 0
  print(f'{month:>14} {year:>8}\n')
  print('{:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}'.format('S','M','T','W','Th','F','Sa'))
  print()
  while current_day_of_week < start_day_of_week:
    print('{:3} '.format(' '),end='')
    current_day_of_week = (current_day_of_week + 1) % 7

  for d in range(1, days_in_month +1):
    print('{:3} '.format(d),end='')
    
    current_day_of_week = (current_day_of_week + 1) % 7

    if (current_day_of_week % 7 == 0):
      print()
      print()
