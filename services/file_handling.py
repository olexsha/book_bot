import os
import sys
from typing import Dict, Tuple

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: Dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> Tuple[str, int]:
    marks = set(',!.:;?')

    if len(text) < start + size:
        size = len(text) - start
        s = text[start:start + size]
    else:
        s = text[start:start + size]
        if s[-1] and text[start+size] in marks:
            while s[-1] in marks:
                s = s[:-1]

    for i in range(len(s) - 1, -1, -1):
        if s[i] in marks:
            return s[:i+1], i+1


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    global book

    text = open(path, encoding='utf-8').read().strip()
    i = 1
    start = 0
    while start < len(text):
        book[i], new_size = _get_part_text(text, start, PAGE_SIZE)
        book[i] = book[i].strip()
        start += new_size
        i += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
