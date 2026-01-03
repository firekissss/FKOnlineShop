from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Sequence


class BaseProduct(ABC):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Product) -> float:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass


class Product(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str | None = None) -> None:
        super().__init__(name, description, price, quantity)
        self.color = color

    def __str__(self) -> str:
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        if not isinstance(self, Product) or not isinstance(other, Product):
            raise TypeError(
                f"Оба объекта должны быть экземплярами класса Product. Получены объекты типа {type(self).__name__} и {type(other).__name__}"
            )

        self_type = type(self)
        other_type = type(other)

        if self_type != other_type:
            raise TypeError(
                f"Можно сложить только 2 одинаковых товара. "
                f"Получены объекты {self_type.__name__} и {other_type.__name__}"
            )

        return self.quantity * self._price + other.quantity * other._price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            # raise ValueError("Цена не должна быть нулевая или отрицательная")
            # делаю по заданию, но лучше в таких случаях кидать ошибку
            print("Цена не должна быть нулевая или отрицательная")
            return
        if self._price > price:
            if input("Понизить цену? (1 для подтверждения)\t") == "1":
                self._price = price
        else:
            self._price = price

    @classmethod
    def new_product(
        cls, product_dict: Dict[str, str | int | float], existing_products: Sequence[Product]
    ) -> tuple[Product, bool]:
        name: str = str(product_dict["name"])
        description: str = str(product_dict["description"])
        price: float = float(product_dict["price"])
        quantity: int = int(product_dict["quantity"])
        for product in existing_products:
            if product.name == name:
                product.quantity += quantity
                product.description = description
                if price > product.price:
                    product.price = price
                return product, False

        return cls(name, description, price, quantity), True


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        _price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str | None = None,
    ) -> None:
        super().__init__(name, description, _price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        _price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str | None = None,
    ) -> None:
        super().__init__(name, description, _price, quantity, color)
        self.country = country
        self.germination_period = germination_period
