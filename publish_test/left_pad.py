def left_pad(word: str, length: int, fill_character: str = ' ') -> str:
    return str(word).rjust(length, str(fill_character))
