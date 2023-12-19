import numpy as np

def outliers_z_score(data_array, label, measure, z_threshold=2, is_sample=False):

    # Input validation checks
    if not isinstance(data_array, list) or len(data_array) == 0 or not isinstance(data_array[0], dict):
        raise ValueError('The first parameter requires a list of dictionaries.')
    
    if not isinstance(label, str): 
        raise ValueError('The second parameter requires a string.')
    
    if not isinstance(measure, str):
        raise ValueError('The third parameter requires a string.')
    
    if not isinstance(z_threshold, (int, float)) or not z_threshold:
        raise ValueError('The fourth parameter requires a number.')
    
    if not isinstance(is_sample, bool):
        raise ValueError('The fifth parameter requires a boolean.')

    # Create array of measure values
    measure_array = [data[measure] for data in data_array]
    
    # Calculate mean and standard deviation
    mean = np.mean(measure_array)
    if is_sample:
        std_dev = np.std(measure_array, ddof=1)  # Use ddof=1 for sample standard deviation
    else:
        std_dev = np.std(measure_array, ddof=0)  # Use ddof=0 for population standard deviation
    
    # Filter outliers
    outliers = []
    for data in data_array:
        value = data[measure]
        z_score = abs((value - mean) / std_dev)
        if z_score > z_threshold:
            outliers.append(data)

    # Structure results 
    results = []
    for data in outliers:
        value = data[measure]
        z_score = abs(round((value - mean) / std_dev, 2))
        outlier_type = 'high' if value > mean else 'low'
        
        result = {
            'label': data[label],
            'value': value,
            'type': outlier_type,
            'z_score': z_score,
            'z_threshold': z_threshold,
            'std_dev': round(std_dev, 2), 
            'mean': round(mean, 2)
        }
        results.append(result)

    return results

# test output
data = [
    {'month': 'Jan', 'orders': 275, 'sales': 28500},
    {'month': 'Feb', 'orders': 30, 'sales': 31200},
    {'month': 'Mar', 'orders': 310, 'sales': 33100 },
    {'month': 'Apr', 'orders': 290, 'sales': 27700 },
    {'month': 'May', 'orders': 285, 'sales': 28300 },
    {'month': 'Jun', 'orders': 305, 'sales': 27700 },
    {'month': 'Jul', 'orders': 292, 'sales': 31300 },
    {'month': 'Aug', 'orders': 307, 'sales': 30400 },
    {'month': 'Sep', 'orders': 290, 'sales': 27800 },
    {'month': 'Oct', 'orders': 612, 'sales': 62700 },
    {'month': 'Nov', 'orders': 310, 'sales': 29600 },
    {'month': 'Dec', 'orders': 314, 'sales': 30200 }
]

result1 = outliers_z_score(data, 'month', 'orders', 2, True) 
result2 = outliers_z_score(data, 'month', 'orders', 2, False)

print(result1)
print(result2)
