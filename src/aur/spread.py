def obtain_total_spread(chosen_seed_array):

    adaptive_gains = [row[1] for row in chosen_seed_array]

    total_spread = max(adaptive_gains) - min(adaptive_gains)

    return total_spread