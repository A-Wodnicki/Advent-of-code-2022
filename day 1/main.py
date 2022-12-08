def main():
    with open('data.txt', 'r') as data:
        """
        Get all calories grouped by elves
        For example: [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
        """
        elves_calories = [list(map(int, line.split())) for line in data.read().split('\n\n')]
    """
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    Your puzzle answer was 72511.
    """
    print(f'* {max(sum(calories) for calories in elves_calories)}')
    """
    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    Your puzzle answer was 212117.
    """
    print(f'** {sum(sorted([sum(calories) for calories in elves_calories], reverse=True)[:3])}')


if __name__ == '__main__':
    main()
