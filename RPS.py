import random


def player(prev_play, opponent_history=[]):
    if prev_play == "":
        return random.choice(["R", "P", "S"])

    if len(opponent_history) == 0:
        return random.choice(["R", "P", "S"])

    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1

    most_freq_move = max(move_counts, key=move_counts.get)

    if most_freq_move == "R":
        return "P"

    elif most_freq_move == "P":
        return "S"

    elif most_freq_move == "S":
        return "R"

    return random.choice(["R", "P", "S"])
