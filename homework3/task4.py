def is_armstrong(number: int) -> bool:
    """function that detects if a number is Armstrong number"""
    if number <= 0:
        return False
    num_in_str = str(number)
    length = len(num_in_str)
    int_list = list(map(lambda x: int(x)**length, num_in_str))
    sum_all = sum(int_list)
    return True if (sum_all == number) else False
