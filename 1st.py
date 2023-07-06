num_elements = int(input("Enter the number of elements in the list: "))
elements = []
for i in range(num_elements):
    element = input("Enter element {}: ".format(i+1))
    elements.append(element)

tuple_data = tuple(elements)

reversed_tuple = tuple_data[::-1]

print("Reversed tuple:", reversed_tuple)
