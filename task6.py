def get_element_at_index(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None

my_list = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input(f"Enter an index (0 to {len(my_list) - 1}): "))
        element = get_element_at_index(my_list, index)
        if element is not None:
            print(f"Element at index {index} is: {element}")
            break
        else:
            print("Index out of range. Try again.")
    except ValueError:
        print("Please enter a valid integer.")