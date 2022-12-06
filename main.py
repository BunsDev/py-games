import random
import images

my_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.randint(0, 2)

print('You chose:')

if my_choice == 0:
    images.print_rock()
elif my_choice == 1:
    images.print_paper()
elif my_choice == 2:
    images.print_scissors()

print('Computer chose:')

if computer_choice == 0:
    images.print_rock()
elif computer_choice == 1:
    images.print_paper()
elif computer_choice == 2:
    images.print_scissors()

if (my_choice == 2 and computer_choice == 0):
    print('Computer won!')
    exit()
elif (my_choice == 0 and computer_choice == 2):
    print('You won!')
    exit()

if (my_choice > computer_choice):
    print('You won!')
elif (my_choice < computer_choice):
    print('Computer won!')
else:
    print('Draw')
