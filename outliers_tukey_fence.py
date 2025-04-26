import numpy as np

def outliers_tukey_fence(data_array, label, measure, multiplier=1.5):
    
    # Input validation checks
    if not isinstance(data_array, list) or len(data_array) == 0 or not isinstance(data_array[0], dict):
        raise ValueError('The first parameter requires a list of dictionaries.')
    
    if not isinstance(label, str):
        raise ValueError('The second parameter requires a string.')
    
    if not isinstance(measure, str):
        raise ValueError('The third parameter requires a string.')
    
    if not isinstance(multiplier, (int, float)):
        raise ValueError('The fourth parameter requires a number.')

    # Extract the array of values for the specified measure
    input_array = [data[measure] for data in data_array]

    # Calculate Q1, Q3 and IQR for array
    q1 = np.percentile(input_array, 25)
    q3 = np.percentile(input_array, 75)
    iqr = q3 - q1

    # Calculate upper and lower fences for threshold analysis
    lower_fence = q1 - (multiplier * iqr)
    upper_fence = q3 + (multiplier * iqr)

    # Filter the input data to leave the outlier objects only
    outliers_array = [data for data in data_array if data[measure] > upper_fence or data[measure] < lower_fence]

    # Map the filtered data to an array of results objects
    outliers = [{
        'label': data[label],
        'value': data[measure],
        'type': 'high' if data[measure] > upper_fence else 'low',
        'lower_fence': round(lower_fence, 2),
        'upper_fence': round(upper_fence, 2),
        'multiplier': multiplier
    } for data in outliers_array]

    return outliers

# Test output
my_data = [
    {'month': 'Jan', 'orders': 313, 'sales': 32500},
    {'month': 'Feb', 'orders': 30, 'sales': 31200 },
    {'month': 'Mar', 'orders': 315, 'sales': 33100 },
    {'month': 'Apr', 'orders': 290, 'sales': 27500 },
    {'month': 'May', 'orders': 293, 'sales': 28300 },
    {'month': 'Jun', 'orders': 305, 'sales': 27700 },
    {'month': 'Jul', 'orders': 354, 'sales': 38100 },
    {'month': 'Aug', 'orders': 307, 'sales': 30400 },
    {'month': 'Sep', 'orders': 290, 'sales': 27800 },
    {'month': 'Oct', 'orders': 544, 'sales': 59700 },
    {'month': 'Nov', 'orders': 288, 'sales': 29600 },
    {'month': 'Dec', 'orders': 314, 'sales': 30200 }
]

result1 = outliers_tukey_fence(my_data, 'month', 'orders')
result2 = outliers_tukey_fence(my_data, 'month', 'orders', 2)
result3 = outliers_tukey_fence(my_data, 'month', 'orders', 3)

print(result1)
print(result2)
print(result3)
