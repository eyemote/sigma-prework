input_list = input("Enter a list of integers separated by a space: ").split()
sorted_list = sorted(int(i) for i in input_list)
print([sorted_list[0], sorted_list[-1]])
