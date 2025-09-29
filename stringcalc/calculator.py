from splitter import StringSplitter
from validator import has_content, no_negatives


def add(expression: str) -> int:
    """
    Add numbers from a string expression.
    Rules:
    - Empty string returns 0
    - Numbers separated by , or \n
    - Supports custom delimiters (//[delim]\n)
    - Ignores numbers > 1000
    - Raises error for negatives
    """
    if not has_content(expression):
        return 0

    splitter = StringSplitter(expression)
    delimiters, numbers_str = splitter.split()
    numbers = splitter.split_numbers(numbers_str, delimiters)

    no_negatives(numbers)
    return _sum_valid(numbers)


def _sum_valid(numbers: list[str]) -> int:
    return sum(int(n) for n in numbers if n and int(n) <= 1000)
