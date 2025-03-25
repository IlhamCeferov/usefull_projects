import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        try:
            dice_count = int(input('How many dice you want to roll?: '))
            if dice_count > 0:
                for i in range(dice_count):
                    dice = random.randint(1, 6)
                    print(f'({dice})')
        except ValueError:
            print('Invalid number choose again!')
    elif choice == 'n': 
        print('Thanks for playing')
        break
    else:
        print('Invalid choice!')