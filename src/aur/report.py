from .gains import adaptive_gain, absolute_adaptive_gain
from .read_data import obtain_data_from_csv
from .spread import obtain_total_spread
from .percentile import chosen_seeds

def return_full_report(file_path, percentile, higher_is_better):

    data_array = obtain_data_from_csv(file_path)

    directional_gain_array = adaptive_gain(data_array, higher_is_better)

    gain_array = absolute_adaptive_gain(data_array)

    selected_seeds = chosen_seeds(percentile, gain_array)

    spread = obtain_total_spread(selected_seeds)

    total_seeds = len(gain_array)
    used_seeds = len(selected_seeds)

    effective_percentile = (used_seeds / total_seeds) * 100

    selected_gains = [row[1] for row in selected_seeds]
    percentile_upside = sum(selected_gains) / used_seeds

    directional_gains = [row[1] for row in directional_gain_array]

    wins = sum(gain > 0 for gain in directional_gains)
    win_rate = (wins / total_seeds) * 100

    mean_signed_gain = sum(directional_gains) / total_seeds

    seed_table = ""

    for row in selected_seeds:

        seed = row[0]
        absolute_gain = row[1]

        seed_table += f"{seed:<12}{absolute_gain:.2f}%\n"

    report = f"""
##################################################
              ADAPTIVE UTILITY REPORT
##################################################

Input file:               {file_path}
Requested percentile:     {percentile:.2f}%
Higher is better:         {higher_is_better}
--------------------------------------------------
EXPERIMENT SUMMARY
--------------------------------------------------

Total seeds analysed:     {total_seeds}
Seeds selected:           {used_seeds}
Effective percentile:     {effective_percentile:.2f}%

--------------------------------------------------
SELECTED SEEDS
--------------------------------------------------

Seed        Absolute Gain
--------------------------
{seed_table}

--------------------------------------------------
PERCENTILE PERFORMANCE
--------------------------------------------------

Percentile Upside:        {percentile_upside:.2f}%
Percentile Spread:        {spread:.2f}%

--------------------------------------------------
DIRECTIONAL PERFORMANCE
--------------------------------------------------

Mean Signed Gain:         {mean_signed_gain:.2f}%
Adaptive Wins:            {wins} / {total_seeds}
Adaptive Win Rate:        {win_rate:.2f}%

--------------------------------------------------
DEFINITIONS
--------------------------------------------------

Percentile Upside:
Mean adaptive gain magnitude among the selected
highest-gain seeds.

Percentile Spread:
Difference between the maximum and minimum gain
within the selected percentile.

Mean Signed Gain:
Mean directional adaptive gains across all paired
seeds. Positive values indicate an overall adaptive
gain; negative values indicate an overall fixed
gain.

Adaptive Win Rate:
Percentage of paired seeds for which the adaptive
model outperformed the fixed model.

##################################################
                  END OF REPORT
##################################################

   ####      ###    ###    ########
  ######     ###    ###    #########
 ###  ###    ###    ###    ###    ###
###    ###   ###    ###    ###    ###
##########   ###    ###    #########
##########   ###    ###    ########
###    ###   ###    ###    ###   ###
###    ###    ########     ###    ###
###    ###     ######      ###     ###
"""

    return report