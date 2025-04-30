# 1. Create a tuple with different data types
mixed_tuple = (10, "Hello", 3.14, True)
print("Tuple with different datatypes: ", mixed_tuple)
# 2. Create another tuple of integers
int_tuple = (1, 2, 3, 4, 5)
print("Integer tuple: ", int_tuple)
# 3. Create a new tuple by adding 9 to each element in the integer tuple
# Using a generator expression with tuple comprenhension
updated_tuple = tuple(x + 9 for x in int_tuple)
print("Tuple after adding 9 to each element:", updated_tuple)
# 4. Count the occurences of an element int the tuple
# For example, count how many times '12 appears in the updated tuple
elements_to_count = 12
count = updated_tuple.count(elements_to_count)
print(f"Occurences of {elements_to_count}:", count)
# 5. Perform slicing on the tuple
# For example, take elements from index 1 to 3
sliced_tuple = updated_tuple[1:4]
print("Sliced tuple (index 1 to 3):", sliced_tuple)