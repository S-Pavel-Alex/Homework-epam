from pathlib import Path
from typing import Callable, Optional


def count_lines(file_path: Path) -> int:
    with open(file_path) as file:
        count = 0
        for _ in file:
            count += 1
    return count


def count_with_tokenizer(file_path: Path, tokenizer: Callable) -> int:
    with open(file_path) as file:
        count = 0
        text = file.read()
        token = tokenizer(text)
        count += len(token)
    return count


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    files = [i for i in dir_path.glob(f'**/*.{file_extension}') if i.is_file()]
    if tokenizer:
        all_token = sum(count_with_tokenizer(file, tokenizer)
                        for file in files)
        return all_token
    return sum(count_lines(file) for file in files)
