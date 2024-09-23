def med(x):
  length = len(x)
  x.sort()
  middle = length / 2
  if length % 2 == 0:
    print((x[int(middle - 0.5)] + x[int(middle + 0.5)]) / 2)
  else:
    print(x[int(middle)])