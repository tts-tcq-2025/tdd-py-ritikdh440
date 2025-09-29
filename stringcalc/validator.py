def has_content(expression: str) -> bool:
    """Return False if string is empty, True otherwise."""
    return bool(expression)


def no_negatives(numbers: list[str]) -> None:
    """Raise error if negative numbers exist."""
    negatives = [n for n in numbers if n and int(n) < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(negatives)}")
