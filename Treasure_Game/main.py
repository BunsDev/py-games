import util

util.entry_image()

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction_cross_road = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

# check if the user has typed in right or left
if (direction_cross_road != 'right' and direction_cross_road != 'left'):
    print('Don\'t try to be smart! Follow the game rules!')

if direction_cross_road == 'right':
    direction_mountain = input(
        'You come to a mountain. There is an a beast on the way! Type "kill" or "tame"\n').lower()

    if direction_mountain != 'kill' and direction_mountain != 'tame':
        print('You didn\'t make the right choice! Now start from the beginning')
        util.my_final_image()
        exit()

    if direction_mountain == 'tame':
        print('Amateur mistake, don\'t try to tame wild beasts! You died!')
        util.my_final_image()
        exit()

    elif direction_mountain == 'kill':
        direction_forest = input(
            'You killed the beast! Now you need to go through the mountain forest to search for the treasure! Be quiet! There is a sleeping dargon! Type "forward" to proceed the journey or "end" if you are a coward and what to go home\n').lower()
        if (direction_forest != 'end' and direction_forest != 'forward'):
            print('Wrong choice! Try again!')
            util.my_final_image()
            exit()

        if (direction_forest == 'end'):
            print('I am disappointed in you! Game over!')
            util.my_final_image()
            exit()

        elif (direction_forest == 'forward'):
            dragon_obstacle = input(
                'You really are a warrior and you went through the forest. However the dragon got awaken. This the the end!\n'
                'Type in "yes" if you liked the game so far or "no" if it is not good enough!\n')

            if (dragon_obstacle == 'yes'):
                print('Thanks for the good feedback. See you soon!')
            else:
                print('Changes will be made. Thanks for the feedback!')

elif direction_cross_road == 'left':
    direction_lake = input(
        'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

    # check if the user has typed in swim or wait
    if (direction_lake != 'swim' and direction_lake != 'wait'):
        print('You didn\'t make the right choice! Now start from the beginning')
        util.my_final_image()
        exit()

    if direction_lake == 'swim':
        print('You forgot you cannot swim! Game over!')
        util.my_final_image()
        exit()

    else:
        direction_island = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n').lower()
        if direction_island == 'red':
            print('You will not win! Game over!')
            util.my_final_image()
            exit()

        elif direction_island == 'blue':
            print('Hahaha wrong door! You died!')
            util.my_final_image()
            exit()

        elif direction_island == 'yellow':
            print('You found the treasure! You were lucky this time. See you soon!')
            util.my_final_image()
            exit()
        else:
            print('You chose a door that doesn\'t exist! Try again!')

util.my_final_image()