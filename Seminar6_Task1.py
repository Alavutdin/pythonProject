import pytest


def find_avg(numbers: list) -> float:
    if not (isinstance(numbers, list)):
        raise TypeError('Переданный объект не является листом')
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def test_find_avg():
    assert find_avg([1, 2, 3]) == 2, 'Ожидаемое не сошлось'
    assert find_avg([]) == 0
    assert find_avg([5]) == 5


# Модифицируйте функцию find_average так,
# чтобы она вызывала исключение TypeError, если
# ей передается не список.
def test_find_avg_type():
    with pytest.raises(TypeError):
        find_avg('qwerty')
        