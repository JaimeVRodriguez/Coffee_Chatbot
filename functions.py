def get_size():
  res = input('What size drink can I get for you?\n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like?\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  
  if res == 'a':
    return order_brew()
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def get_cup_type():
  res = input('What type of cup would you like?\n[a] Plastic Cup \n[b] Reusable Cup \n> ')

  if res == 'a':
    return 'Plastic Cup'
  elif res == 'b':
    return 'Reusable Cup'
  else:
    print_message()
    return cup_type()

def order_latte():
  res = input('And what kind of milk for your latte?\n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

  if res == 'a':
    return 'Latte'
  elif res == 'b':
    return 'Non-fat Latte'
  elif res == 'c':
    return 'Soy Latte'
  else:
    print_message()
    return order_latte()

def order_brew():
  res = input('And what kind of brewed coffee?\n[a] Hot \n[b] Iced \n> ')

  if res == 'a':
    return 'Hot Brewed Coffee'
  elif res == 'b':
    return 'Iced Brewed Coffee'
  else:
    print_message()
    return order_brew()

def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha?\n[a] Sure! \n[b] Maybe next time! \n> ')
    
    if res == 'a':
      return 'Peppermint Mocha'
    elif res == 'b':
      return 'Mocha'

    print_message()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the cooresponding letter for your response.")

