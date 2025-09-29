import re
from typing import List, Tuple


class StringSplitter:
    """
    Responsible for extracting numbers and delimiters from an expression.
    Default delimiters: comma ',' and newline '\n'.
    Custom delimiters: //[delimiter]\n or multi-char //[***]\n
    """

    def __init__(self, expression: str):
        self.expression = expression

    def split(self) -> Tuple[List[str], str]:
        """
        Returns a tuple of (list of delimiters, raw number string)
        """
        if not self.expression.startswith("//"):
            return [",", "\n"], self.expression

        match = re.match(r"^//(\[.*\]|.)\n(.*)", self.expression, re.DOTALL)
        if not match:
            return [",", "\n"], self.expression

        return self._parse_match(match)

    def _parse_match(self, match: re.Match) -> Tuple[List[str], str]:
        raw_delim, numbers = match.groups()
        if raw_delim.startswith("[") and raw_delim.endswith("]"):
            # multi-character delimiter
            delim = [raw_delim[1:-1]]
        else:
            delim = [raw_delim]

        # always include newline as delimiter
        delim.append("\n")
        return delim, numbers

    @staticmethod
    def split_numbers(number_str: str, delimiters: list[str]) -> list[str]:
        """
        Split number_str using all delimiters provided.
        """
        pattern = "|".join(re.escape(d) for d in delimiters)
        return re.split(pattern, number_str)
