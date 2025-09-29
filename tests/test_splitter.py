import re
from splitter import StringSplitter


def test_default_delimiters_split():
    splitter = StringSplitter("1,2\n3")
    delimiters, nums_str = splitter.split()
    numbers = splitter.split_numbers(nums_str, delimiters)
    assert delimiters == [",", "\n"]
    assert numbers == ["1", "2", "3"]


def test_single_char_custom_delimiter():
    splitter = StringSplitter("//;\n1;2;3")
    delimiters, nums_str = splitter.split()
    numbers = splitter.split_numbers(nums_str, delimiters)
    assert delimiters == [";", "\n"]
    assert numbers == ["1", "2", "3"]


def test_multi_char_custom_delimiter():
    splitter = StringSplitter("//[***]\n1***2***3")
    delimiters, nums_str = splitter.split()
    numbers = splitter.split_numbers(nums_str, delimiters)
    assert delimiters == ["***", "\n"]
    assert numbers == ["1", "2", "3"]


def test_split_numbers_with_multiple_occurrences():
    splitter = StringSplitter("1***2***3")
    numbers = splitter.split_numbers("1***2***3", ["***", "\n"])
    assert numbers == ["1", "2", "3"]
