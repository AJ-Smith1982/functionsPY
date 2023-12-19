from scipy.stats import t
import numpy as np

def outliers_grubbs_test(data_array, label, measure, alpha = 0.05, test_type = 'two-sided'):
    
    # Input validation checks
    if not isinstance(data_array, list) or len(data_array) < 7:
        raise ValueError('data_array must be a list containing seven or more values.')
    
    if not isinstance(label, str):
        raise ValueError('label must be a string.')
    
    if not isinstance(measure, str):
        raise ValueError('measure must be a string.')
    
    if not isinstance(alpha, (int, float)) or alpha < 0 or alpha > 1:
        raise ValueError('alpha must be a number between 0 and 1.')
    
    valid_test_types = ['two-sided', 'left-sided', 'right-sided']
    if test_type not in valid_test_types:
        raise ValueError('Invalid test_type. Valid inputs are: "two-sided", "left-sided", "right-sided."')

    # Get sample mean and standard deviation
    mean = np.mean([data_point[measure] for data_point in data_array])
    std_d = np.std([data_point[measure] for data_point in data_array], ddof=1)

    # Get most extreme value and its corresponding label
    
    # Calculate Grubbs' statistic (G-score) for extreme value
  
    # Calculate degrees of freedom (df) for data_array

    # Calculate critical value from the t-distribution
    
    # Compare G-score with critical value

    # Construct the result object
    result = {}

    return result

# Test output 
test_data = []

result1 = outliers_grubbs_test(test_data, 'month', 'orders', 0.05, 'two-sided')
result2 = outliers_grubbs_test(test_data, 'month', 'orders', 0.05, 'left-sided')
result3 = outliers_grubbs_test(test_data, 'month', 'orders', 0.05, 'right-sided')

print(result1)
print(result2)
print(result3)
