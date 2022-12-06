import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

CHOICE = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSOR',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSOR',
}

OUTCOME = {'X': -1, 'Y': 0, 'Z': 1}
POINTS = {'ROCK': 1, 'PAPER': 2, 'SCISSOR': 3, 'WIN': 6, 'DRAW': 3, 'LOSS': 0}

player_score = 0
opponent_score = 0

win_total = 0
loss_total = 0
draw_total = 0


def getOutcome(a, b):
    if a == b:
        return 0
    if a == 'ROCK' and b == 'PAPER':
        return -1
    if a == 'ROCK' and b == 'SCISSOR':
        return 1
    if a == 'PAPER' and b == 'ROCK':
        return 1
    if a == 'PAPER' and b == 'SCISSOR':
        return -1
    if a == 'SCISSOR' and b == 'ROCK':
        return -1
    if a == 'SCISSOR' and b == 'PAPER':
        return 1


def getPlayerChoice(opponent, outcome) -> str:
    if outcome == 0:
        return opponent
    if outcome == -1:
        if opponent == 'ROCK':
            return 'SCISSOR'
        if opponent == 'PAPER':
            return 'ROCK'
        if opponent == 'SCISSOR':
            return 'PAPER'
    if outcome == 1:
        if opponent == 'ROCK':
            return 'PAPER'
        if opponent == 'PAPER':
            return 'SCISSOR'
        if opponent == 'SCISSOR':
            return 'ROCK'


for index, value in enumerate(lines):
    opponent_choice, player_choice = value.split(" ")

    opponent_choice = CHOICE[opponent_choice.strip()]
    outcome = OUTCOME[player_choice.strip()]
    # player_choice = CHOICE[player_choice.strip()]

    # outcome = getOutcome(player_choice, opponent_choice)
    player_choice = getPlayerChoice(opponent_choice, outcome)

    if outcome == 0:
        draw_total += 1
        player_score += POINTS[player_choice] + POINTS['DRAW']
        opponent_score += POINTS[opponent_choice] + POINTS['DRAW']
    elif outcome == 1:
        win_total += 1
        player_score += POINTS[player_choice] + POINTS['WIN']
        opponent_score += POINTS[opponent_choice] + POINTS['LOSS']
    else:
        loss_total += 1
        player_score += POINTS['LOSS'] + POINTS[player_choice]
        opponent_score += POINTS[opponent_choice] + POINTS['WIN']

print(f"Player Score is {player_score}")
