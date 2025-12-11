from __future__ import annotations

from typing import Dict, Sequence


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int, color: str | None = None) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        return self.quantity * self.__price + other.quantity * other.__price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            # raise ValueError("Цена не должна быть нулевая или отрицательная")
            # делаю по заданию, но лучше в таких случаях кидать ошибку
            print("Цена не должна быть нулевая или отрицательная")
            return
        if self.__price > price:
            if input("Понизить цену? (1 для подтверждения)\t") == "1":
                self.__price = price
        else:
            self.__price = price

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
        __price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: float,
        color: str | None,
    ) -> None:
        super().__init__(name, description, __price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        __price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str | None,
    ) -> None:
        super().__init__(name, description, __price, quantity, color)
        self.country = country
        self.germination_period = germination_period
