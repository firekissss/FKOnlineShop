from src.container import ProductContainer
from src.product import Product


class Order(ProductContainer):
    def __init__(
        self,
        name: str,
        description: str,
        product: Product,
        quantity: int,
    ) -> None:
        super().__init__(name, description)

        if quantity <= 0:
            raise ValueError("Количество товара в заказе должно быть больше 0")

        if product.quantity < quantity:
            raise ValueError("Недостаточно товара на складе")

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, " f"{self.quantity} шт., " f"итого {self.total_price} руб."
