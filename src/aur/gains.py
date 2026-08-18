import numpy as np

def adaptive_gain(read_data_array):
    
    adaptive_gains_array = []

    seeds = read_data_array[:, 0]
    adaptive = read_data_array[:, 1]
    fixed = read_data_array[:, 2]
    
    if len(adaptive) != len(fixed):
        raise ValueError("Length of adaptive array must be equal to Length of fixed array resultss")
    
    else:
        for i in range(len(adaptive)):
            
            fixed_value = fixed[i]
            adaptive_value = adaptive[i]
            
            if fixed_value == 0:
        
                raise ValueError("Division by zero is not possible. Change the fixed value to a non-zero value.")

            if not isinstance(fixed_value, (int, float, np.integer, np.floating)):
                raise TypeError("Use only float (decimal) values or integers")

            if not isinstance(adaptive_value, (int, float, np.integer, np.floating)):
                raise TypeError("Use only float (decimal) values or integers")
    
            else:
        
                difference = abs(adaptive_value-fixed_value)
                gains = (difference / abs(fixed_value)) * 100
                adaptive_gains_array.append([seeds[i], gains])
        
        return adaptive_gains_array