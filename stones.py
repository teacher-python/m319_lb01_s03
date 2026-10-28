"""Turns stones between a lower and an upper limit."""


def main():
    """
    turns stones between a lower and an upper limit
    :return: list of stones ("green" or "blue")
    """

    stones = []    # DO NOT change the name of this variable. MUST BE the list statement

    lower_limit = int(input('Untere Limite: '))
    upper_limit = int(input("Obere Limite: "))
    for i in range(upper_limit):
        stones.append('green')

    day = 1
    while day <= upper_limit:
        print(f'Tag={day}')
        number = day
        while number < upper_limit:
            print(f'Nummer={number}')
            if stones[number] == 'blue':
                stones[number] = 'green'
            else:
                stones[number] = 'blue'
            number += day
        day += 1

    blue_stones = 0
    for i in range(lower_limit, upper_limit):
        blue_stones += 1 if stones[i] == 'blue' else 0
    print(f'{blue_stones} blaue Steine')
    return stones      # DO NOT change, must be the last line of this function
