from typing import Callable, TypeVar, Iterable

E = TypeVar('E')


def find_first(predicate: Callable[[object], bool], iterable: Iterable[E]) -> E | None:
    for elem in iterable:
        if predicate(elem):
            return elem
