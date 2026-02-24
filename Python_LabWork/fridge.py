from lab1 import monotonicity_check

def check_temperature(temp_array):
    if monotonicity_check(temp_array) and temp_array[0] < temp_array[-1]:
        return "Error: temperature rises"
    else:
        return "The temperature is normal"

