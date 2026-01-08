from abc import ABC, abstractmethod


class ProductContainer(ABC):
    def __init__(self, name: str, description: str) -> None:
        if not name:
            raise ValueError("Название не может быть пустым")
        if not description:
            raise ValueError("Описание не может быть пустым")

        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass
