import random

white_possibilities = list(range(1,70))
red_possibilities = list(range(1,27))

tickets_per_drawing = 1
num_drawings = 1

total_spent = 0
total_earned = 0

times_won = {
    "5+P" : 0,
    "5" : 0,
    "4+P" : 0,
    "4" : 0,
    "3+P" : 0,
    "3" : 0,
    "2+P" : 0,
    "1+P" : 0,
    "P" : 0,
    "0" : 0
}

def calc_win_amt(my_numbers:dict, winning_numbers:dict) -> int:
    win_amt = 0

    white_matches = len(my_numbers['whites'].intersection(winning_numbers['whites']))
    power_match = my_numbers['red'] == winning_numbers['red']

    if white_matches == 5:
        if power_match:
            win_amt = 2_000_000_000
            times_won["5+P"] += 1
        else:
            win_amt = 1_000_000
            times_won["5"] += 1

    return win_amt

for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibilities, k=5))
    red_drawing = random.choice(red_possibilities)

    winning_numbers = {
        'whites' : white_drawing,
        'red' : red_drawing
    }

    for ticket in range(tickets_per_drawing):
        total_spent += 2
        my_whites = set(random.sample(white_possibilities, k=5))
        my_red = random.choice(red_possibilities)

        my_numbers = {"whites" : my_whites, "red" : my_red}

        #calc_win_amt()
