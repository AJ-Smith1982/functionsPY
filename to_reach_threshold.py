def to_reach_threshold(data_array, target_threshold):
    # Input validation checks
    if not isinstance(data_array, list) or len(data_array) == 0:
        raise ValueError('data_array requires a list containing at least one number.')
    
    if not all(isinstance(value, (int, float)) for value in data_array):
        raise ValueError('Each element in data_array must be a number.')
    
    if not isinstance(target_threshold, (int, float)) or isinstance(target_threshold, bool):
        raise ValueError('target_threshold must be a number.')

    # Define reassignable variables for loop
    current_sum = 0
    i = 0

    # When target_threshold is positive
    if target_threshold >= 0:
        while i < len(data_array) and current_sum < target_threshold:
            current_sum += data_array[i]
            i += 1

        return i if current_sum >= target_threshold else -1

    # When target_threshold is negative
    else:
        while i < len(data_array) and current_sum > target_threshold:
            current_sum += data_array[i]
            i += 1

        return i if current_sum <= target_threshold else -1


# Test output
data_array1 = [1, 2, 3, 4, 5]
target_threshold1 = 0
result1 = to_reach_threshold(data_array1, target_threshold1)
print(result1)  # Expected output: 1

data_array2 = [1, 2, 3, 4, 5]
target_threshold2 = 5
result2 = to_reach_threshold(data_array2, target_threshold2)
print(result2)  # Expected output: 3

data_array3 = [1, -2, -3, 4, 5]
target_threshold3 = -3
result3 = to_reach_threshold(data_array3, target_threshold3)
print(result3)  # Expected output: 3

data_array4 = [1, -2, -3, 4, 5]
target_threshold4 = -5
result4 = to_reach_threshold(data_array4, target_threshold4)
print(result4)  # Expected output: -1
