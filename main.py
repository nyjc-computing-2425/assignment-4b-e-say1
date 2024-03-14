

stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()


# Type your code below

symbol_count = False
stdform_list = list(stdform)
if stdform_list.count(".") <= 1 and stdform_list.count("x") <= 1 and stdform_list.count("^") <= 1:
  symbol_count = True

caret = stdform.find("^")
exponent = stdform[caret + 1:]
multiply = stdform.find("x")
significand = stdform[:multiply]

sig_valid = True
try:
  significand = float(significand)
except ValueError:
  sig_valid = False

exp_valid = True
try:
  exponent = int(exponent)
except ValueError:
  exp_valid = False



if symbol_count == True and sig_valid == True and exp_valid == True:
  print(f"This number in E notation is {significand}E{exponent}.")
else:
  print("Error converting to scientific E notation.")

