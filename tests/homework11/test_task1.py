from homework11.task1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_simplifieldenum_color_correct():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
    assert ColorsEnum.BLACK == "BLACK"


def test_simplifieldenum_size_correct():
    assert SizesEnum.XL == "XL"
    assert SizesEnum.L == "L"
    assert SizesEnum.M == "M"
    assert SizesEnum.S == "S"
