# Show use of list comprehensions
# Normal way. 
# Igore items in mixed_list that are marked as no_data
def num_list1(mixed_list):
    temp_list = []
    for item in mixed_list:
        if item != 'no data':
            temp_list.append(item)
    return temp_list

# Shorthand way using list comprehensions.
# Igore items in mixed_list that are marked as no_data
def num_list2(mixed_list):
    temp_list = [item for item in mixed_list if item != 'no data']
    return temp_list

# Using list comprehensions and if else.
# For items in mixed_list that are strings replace with 0
def num_list3(mixed_list):
    temp_list = [item if item != 'no data' else 0 for item in mixed_list]
    return temp_list

# Run the example
my_list = [23,98,'no data',765,'no data',834,67, 'no data']
print(num_list3(my_list))