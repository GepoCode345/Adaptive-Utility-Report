import math


def percentile_count(percentile, number_of_seeds):
    
    if percentile > 100 or percentile < 0:
        raise ValueError(
            "Use a percentile value between 0 and 100 inclusive."
        )

    if number_of_seeds <= 0:
        raise ValueError(
            "Use a number of seeds greater than or equal to one."
        )

    decimal_seed_total = (percentile / 100) * number_of_seeds
    used_seeds = math.ceil(decimal_seed_total)

    return used_seeds


def chosen_seeds(percentile, gain_array):

    used_seeds = percentile_count(percentile, len(gain_array))

    sorted_gains = sorted(
        gain_array,
        key=lambda row: row[1],
        reverse=True
    )

    chosen_seed_array = sorted_gains[:used_seeds]

    return chosen_seed_array