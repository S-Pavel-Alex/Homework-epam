def is_armstrong(number: int) -> bool:
    """function that detects if a number is Armstrong number"""
    num_in_list = convert_in_list(number)
    length = len(convert_in_list(number))
    int_list = list(map(lambda x: int(x)**length, num_in_list))
    sum_all = sum(int_list)
    return True if (sum_all == number) else False


def convert_in_list(n):
    return list(str(n))
