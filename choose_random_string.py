import random

def choose_random_string(*options):
    # Validate that at least one option is provided
    if len(options) == 0:
        raise ValueError('Please provide at least one option.')

    # Initialize a list to hold selectable values
    selectable_values = []

    # Loop through each option and add values to the selectable list
    for option in options:
        if isinstance(option, str):
            # If it's a string, add it directly to the selectable list
            selectable_values.append(option)
        elif isinstance(option, list):
            # If it's a list, add its values to the selectable list
            for value in option:
                if isinstance(value, str):
                    selectable_values.append(value)
                else:
                    # If an invalid type is provided, raise an error
                    raise ValueError('Options must be strings or lists of strings.')
        else:
            # If an invalid type is provided, raise an error
            raise ValueError('Options must be strings or lists of strings.')

    # Randomly select an option
    random_index = random.randint(0, len(selectable_values) - 1)
    return selectable_values[random_index]

# Test output
array1 = ['Option 2', 'Option 3', 'Option 4']
array2 = ['Option 5', 'Option 6', 'Option 7']
try:
    result = choose_random_string('Option 1', array1, 'Option 4', array2)
    print(result)
except ValueError as error:
    print(str(error))
