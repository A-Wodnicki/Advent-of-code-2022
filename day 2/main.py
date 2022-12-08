def main():
    with open('example.txt', 'r') as data:
        '''
        Get all moves and responses
        For example: [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
        '''
        games = [x.split(' ') for x in data.read().splitlines()]

    '''
    strat 1
    X - rock
    Y - paper
    Z - scissors
    My total: 9241
    '''
    strat_1_score = 0

    '''
    strat 2
    X - lose
    Y - draw
    Z - win
    My total: 14610
    '''
    strat_2_score = 0

    rewards = {
        'rock': 1,
        'paper': 2,
        'scissors': 3,
        'lose': 0,
        'draw': 3,
        'win': 6
    }

    for move, response in games:
        if move == 'A':
            if response == 'X':
                strat_1_score += rewards['rock'] + rewards['draw']
                strat_2_score += rewards['scissors'] + rewards['lose']
            elif response == 'Y':
                strat_1_score += rewards['paper'] + rewards['win']
                strat_2_score += rewards['rock'] + rewards['draw']
            else:
                strat_1_score += rewards['scissors'] + rewards['lose']
                strat_2_score += rewards['paper'] + rewards['win']

        elif move == 'B':
            if response == 'X':
                strat_1_score += rewards['rock'] + rewards['lose']
                strat_2_score += rewards['rock'] + rewards['lose']
            elif response == 'Y':
                strat_1_score += rewards['paper'] + rewards['draw']
                strat_2_score += rewards['paper'] + rewards['draw']
            else:
                strat_1_score += rewards['scissors'] + rewards['win']
                strat_2_score += rewards['scissors'] + rewards['win']

        elif response == 'X':
            strat_1_score += rewards['rock'] + rewards['win']
            strat_2_score += rewards['paper'] + rewards['lose']
        elif response == 'Y':
            strat_1_score += rewards['paper'] + rewards['lose']
            strat_2_score += rewards['scissors'] + rewards['draw']
        else:
            strat_1_score += rewards['scissors'] + rewards['draw']
            strat_2_score += rewards['rock'] + rewards['win']

    print(f'* {strat_1_score}')
    print(f'** {strat_2_score}')


if __name__ == '__main__':
    main()
