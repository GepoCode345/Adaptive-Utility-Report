import pandas as pd

def obtain_data_from_csv(file_path):
    """
    The CSV file must be organised in the following logical structure:
    
    Seed, Adaptive_DA, Fixed_DA
    """

    if type(file_path) != str:
        raise TypeError("file_path must be a string value")

    else:    
        file = pd.read_csv(file_path, skipinitialspace=True)
        data_array = file[['Seed', 'Adaptive_DA', 'Fixed_DA']].to_numpy()

        return data_array