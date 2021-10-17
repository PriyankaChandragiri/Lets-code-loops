number1 = 0
print('1:', number1)
number2 = 1
for count in range(2, 101):
  print(count, ':', number1 + number2)
  number1 += number2
  number2 = number1 - number2