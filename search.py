def binary_search(list_in: List[int], item: int) -> int:
    """
    If item exists in list_in, this function returns its position in the list.
    """
    my_list = sorted(list_in)

    start = 0
    end = len(list_in) - 1
    while start <= end:
        mid = start + (end - start)//2
        if my_list[mid] == item:
            return list_in.index(item)
        elif my_list[mid] > item:
            end = mid - 1
        elif my_list[mid] < item:
            start = mid + 1
        else:
            return None