from functions import get_size, get_drink_type, get_cup_type, order_latte, order_brew, print_message


def coffee_bot():
  print('\t\t\t****************************\t\t\t')
  print('\t\t\t**  Welcome to the cafe!  **')
  print('\t\t\t****************************\t\t\t')
  print('\n\n\n')

  order_drink = 'y'

  drinks = []

  while order_drink == 'y':
    size = get_size()
    drink_type = get_drink_type()
    cup_type = get_cup_type()

    drink = '{} {}'.format(size, drink_type)
  
    order_message = "Alright, that's a {} in a {}!".format(drink, cup_type)
    print(order_message)

    drinks.append(drink)

    while True:
      order_drink = input('Would you like to order another drink?\n[y] \n[n] \n> ')

      if order_drink == 'y' or order_drink == 'n':
        break
  
  print('Okay, so I have:')
  for drink in drinks:
    print('- {}'.format(drink))

  name = input('Can I get your name please? \n> ')

  thank_message = 'Thanks, {}! Your drink will be ready shortly.'.format(name)
  print(thank_message)

# Run coffee bot
coffee_bot()

