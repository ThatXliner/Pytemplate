from typing import Iterable, TypeVar

AnyNum = TypeVar("AnyNum", int, float, complex)

def factorial(number: int) -> int: ...
def multiply_all(some_iter: Iterable[AnyNum]) -> AnyNum: ...