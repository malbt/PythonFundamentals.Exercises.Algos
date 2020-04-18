def binary_search(list_in, item):
    """
    If item exists in list_in, this function returns its position in the list.
    list_in : list of non duplicate integers
    item : an integer to look for in the list_in
    result : position of an integer(item) in the list_in
    """
    my_list = sorted(list_in)
    # my_list = list_in

    start = 0
    end = len(list_in) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if my_list[mid] == item:
            return my_list.index(item)
        elif my_list[mid] > item:
            end = mid - 1
        elif my_list[mid] < item:
            start = mid + 1

    else:
        return None


# returns nothing not even an error
# list_in = [4, 10, 2, 20, 100, 800, 1, 35, 17]
# item = 200
if __name__ == '__main__':
    list_in = [20, 10, 31, 4, 800, 799, 600]
    my_list = sorted(list_in)
    item = 600
    print(binary_search(list_in, item))
