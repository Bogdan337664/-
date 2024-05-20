import random
player_score = 0
pc_score = 0
while True:
    print('Make your move: choose r, p, or s. To quit the game, enter q')
    player_choice = input()
    if player_choice == 'q':
        break
    if player_choice != 'r' and player_choice != 's' and player_choice != 'p':
        print('Invalid input. Please try again.')
        continue
    pc_choice = random.randint(1, 3)
    if pc_choice == 1:
        pc_choice = 'r'
    elif pc_choice == 2:
        pc_choice = 's'
    else:
        pc_choice = 'p'
    
    if player_choice == 'r':
        if pc_choice == 'r':
            print('It\'s a tie')
        elif pc_choice == 's':
            print('You win')
            player_score += 1
        else:
            print('Computer wins')
            pc_score += 1
    elif player_choice == 's':
        if pc_choice == 'r':
            print('Computer wins')
            pc_score += 1
        elif pc_choice == 's':
            print('It\'s a tie')
        else:
            print('You win')
            player_score += 1
    else: #p
        if pc_choice == 'r':
            print('You win')
            player_score += 1
        elif pc_choice == 's':
            print('Computer wins')
            pc_score += 1
        else:
            print('It\'s a tie')
    
    print(f'Result: Your score {player_score}, PC score: {pc_score}')
