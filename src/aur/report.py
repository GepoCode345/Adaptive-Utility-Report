from .gains import adaptive_gain
from .read_data import obtain_data_from_csv
from .spread import obtain_total_spread
from .percentile import chosen_seeds

def return_full_report(file_path, percentile):

    data_array = obtain_data_from_csv(file_path)

    gain_array = adaptive_gain(data_array)

    selected_seeds = chosen_seeds(percentile, gain_array)

    spread = obtain_total_spread(selected_seeds)

    total_seeds = len(gain_array)
    used_seeds = len(selected_seeds)

    effective_percentile = (used_seeds / total_seeds) * 100

    selected_gains = [row[1] for row in selected_seeds]
    percentile_upside = sum(selected_gains) / used_seeds

    seed_table = ""

    for row in selected_seeds:

        seed = row[0]
        gain = row[1]

        seed_table += f"{seed:<12}{gain:.2f}%\n"


    report = f"""
##################################################
              ADAPTIVE UTILITY REPORT
##################################################

Input file:               {file_path}
Requested percentile:     {percentile:.2f}%

--------------------------------------------------
EXPERIMENT SUMMARY
--------------------------------------------------

Total seeds analysed:     {total_seeds}
Seeds selected:           {used_seeds}
Effective percentile:     {effective_percentile:.2f}%

--------------------------------------------------
SELECTED SEEDS
--------------------------------------------------

Seed        Gain
--------------------------
{seed_table}
--------------------------------------------------
PERCENTILE PERFORMANCE
--------------------------------------------------

Percentile Upside:        {percentile_upside:.2f}%
Percentile Spread:        {spread:.2f}%

--------------------------------------------------
DEFINITIONS
--------------------------------------------------

Percentile Upside:
Mean adaptive gain magnitude among the selected
highest-gain seeds.

Percentile Spread:
Difference between the maximum and minimum gain
within the selected percentile.

##################################################
                  END OF REPORT
##################################################

  ###   #   #  ####
 #   #  #   #  #   #
 #####  #   #  ####
 #   #  #   #  #  #
 #   #   ###   #   #

"""

    return report