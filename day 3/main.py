def calculate_priority(item: str) -> int:
    # ord('a') returns 97
    lowercase_priority_fix = 96
    # ord('A') returns 65
    uppercase_priority_fix = 38
    return ord(item) - (lowercase_priority_fix if item.islower() else uppercase_priority_fix)


def main():
    with open('data.txt', 'r') as data:
        rucksacks = data.read().splitlines()

    '''
    Part one
    Find the item type that appears in both compartments of each rucksack. 
    What is the sum of the priorities of those item types?
    Your puzzle answer was 8053.
    '''
    priorities_1 = 0
    for rucksack in rucksacks:
        compartment_length = len(rucksack) // 2
        compartments = [rucksack[:compartment_length], rucksack[compartment_length:]]
        for item in set(compartments[0]):
            if item in compartments[1]:
                priorities_1 += calculate_priority(item)
                break
    print(f'* {priorities_1}')

    '''
    Part two
    Find the item type that corresponds to the badges of each three-Elf group. 
    What is the sum of the priorities of those item types?
    Your puzzle answer was 2425.
    '''
    priorities_2 = 0
    groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
    for group in groups:
        for item in set(group[0]):
            if all(item in set(rucksack) for rucksack in group[1:]):
                priorities_2 += calculate_priority(item)
                break
    print(f'** {priorities_2}')


if __name__ == '__main__':
    main()
