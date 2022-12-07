print('Welcome to the tip calculator ')
total_bill = float(input('What is the total bill? $'))
percentage_tip = float(input('What percentage tip would you like to give? 10, 12, or 15? '))
people_split = int(input('How many people to split the bill? '))

tip = total_bill * (percentage_tip / 100)

each_person_pay = round((total_bill / people_split) + tip / people_split, 2)

print(f'Each person should pay ${round(each_person_pay, 2)}')