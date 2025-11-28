from typing import TYPE_CHECKING, Iterator


if TYPE_CHECKING:
    from src.category import Category

from src.product import Product


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0
        self.length = len(category._products_list)

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Product:
        if self.index >= self.length:
            raise StopIteration

        item = self.category._products_list[self.index]
        self.index += 1
        return item
