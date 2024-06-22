my_list = [1, 2, 3]  # Rename the variable

dict_example = {'a': 1, 'b': 2, 'c': 3}
#list_example = list(dict_example)  # This now correctly calls the built-in list function
#print(list_example)

dict1 = {1: 'one', 2: 'two', 3: 'three'}
dict2 = {4: 'four', 5: 'five'}

result = {key: val for key, val in zip(list(dict1) + list(dict2), list(dict1.values()) + list(dict2.values()))}

print(result)
print(dir(set))