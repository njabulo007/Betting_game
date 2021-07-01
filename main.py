from random import randint
from time import sleep
                                                                
 #Project ID: hello-app-312708
money = 100
age = int(input('Enter your age to continue : '))
sleep(1)
if (age) >= 18:
    print('You are old enough to play')
    sleep(1)
    print('')
    print('You have R100 to play with')
    sleep(1)
    print('')
    print('Betting with R1 will pay R15')
    print('______________________________________________________________')
    sleep(1)
while money > 0:
    random_number = randint(1, 16)
    if int(age) < 18:
        print('Sorry 18+ players only')
        break
    print('')
    bet_input = input('Try your luck and enter a number from [1 to 15] : ')
    print('')
    sleep(2)
    bet_amount = input('Enter the amount you are betting with -R')
    print('')
    possible_win = int(bet_amount) * 15
    sleep(2)
    if int(bet_amount) > money:
        print('Insufficient funds')
    print('Possible win is R' + str(possible_win) + ' good luck')
    sleep(3)
    print('')
    print('            [' + str(random_number) +']')
    print('')
    if int(bet_input) != random_number:
        money = money - int(bet_amount)
        print('Number ' + str(random_number) + ' came out, sorry you lost')
        print('')
        print('+-+-+-+-+-+-+-+-+-+')
        print('Your money now R' + str(money))
        print('+-+-+-+-+-+-+-+-+-+')
    if int(bet_input) == random_number:
        money = money + int(bet_amount) * 15
        print('Number ' + str(random_number) + 'came out, sorry you lost')
        print('')
        print('+-+-+-+-+-+-+-+-+-+')
        print('Your money now ' + money)
        print('+-+-+-+-+-+-+-+-+-+')  