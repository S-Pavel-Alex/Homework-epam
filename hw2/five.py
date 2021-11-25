def custom_range(f, *some):
    """function that accept any iterable of unique values and then
it behaves as range function"""
    my_some_list = [*some]
    ascii_list = list(f)
    lenth = len(my_some_list)
    if lenth == 1:
        fin = ascii_list.index(my_some_list[0])
        return ascii_list[:fin]
    elif lenth == 2:
        start = ascii_list.index(my_some_list[0])
        fin = ascii_list.index(my_some_list[1])
        return ascii_list[start:fin]
    elif lenth == 3:
        start = ascii_list.index(my_some_list[0])
        fin = ascii_list.index(my_some_list[1])
        step = my_some_list[2]
        return ascii_list[start:fin:step]
