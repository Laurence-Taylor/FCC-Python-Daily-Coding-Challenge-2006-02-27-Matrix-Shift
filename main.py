def shift_matrix(matrix, shift):
    # Determine the amount of sub_arrays
    len_outer_matrix = len(matrix)
    # Determine the lenght of sub_array
    len_inner_matrix = len(matrix[0])
    # Determine the total of elements
    len_total_matrix = len_outer_matrix * len_inner_matrix
    # Create a new empty array
    lineal_array = []
    # convert the matrix in a lineal array
    for i in range(len_outer_matrix):
        lineal_array += matrix[i]
    # Declare a new array of the total of elements
    swap_array = [0]*len_total_matrix
    # iterate over all elements of the array
    for j in range(len_total_matrix):
        # assign the right element to the right position
        swap_array[(shift + j)%len_total_matrix] = lineal_array[j]
    # Return the swaped array in a valid matrix
    return [swap_array[k:k+len_inner_matrix] for k in range(0,len_total_matrix,len_inner_matrix)]

if __name__ == '__main__':
    print(shift_matrix([[1, 2, 3], [4, 5, 6]], 1))
    print('---------')
    print(shift_matrix([[1, 2, 3], [4, 5, 6]], -1))
    print('---------')
    print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))
    print('---------')
    print(shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6))
    print('---------')
    print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7))
    print('---------')
    print(shift_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54))