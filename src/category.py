from typing import Iterator

from src.container import ProductContainer
from src.iterators import CategoryIterator
from src.product import Product


class Category(ProductContainer):
    # class attributes
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        super().__init__(name, description)
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                f"Ожидался объект класса Product или его подкласса, " f"получен объект типа: {type(product).__name__}"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        output_list = []
        # adding to list is more optimized than adding to a string
        for product in self.__products:
            output_list.append(str(product))

        return "\n".join(output_list)

    @property
    def _products_list(self) -> list[Product]:
        return self.__products

    def __iter__(self) -> Iterator[Product]:
        return CategoryIterator(self)

    def avg_price(self) -> float:
        try:
            return sum(current_product.price for current_product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0
