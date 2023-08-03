from abc import ABC, abstractclassmethod
from typing import Literal


class Race(ABC):
    gender: Literal["female", "male"]
    data: dict

    @abstractclassmethod
    def __init__(self, gender: Literal["female", "male"]) -> None:
        ...

    @abstractclassmethod
    def __str__(self) -> str:
        ...
    
    @abstractclassmethod
    def to_json(self) -> dict:
        ...
