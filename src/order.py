from src.container import ProductContainer
from src.exceptions import ZeroQuantityError
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
            raise ZeroQuantityError("Количество товара в заказе должно быть больше 0")

        if product.quantity < quantity:
            raise ValueError("Недостаточно товара на складе")

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, " f"{self.quantity} шт., " f"итого {self.total_price} руб."

    def add_product(self, product: Product) -> None:
        try:
            if not isinstance(product, Product):
                raise TypeError(
                    f"Ожидался объект класса Product или его подкласса, "
                    f"получен объект типа: {type(product).__name__}"
                )

            if product.quantity <= 0:
                raise ZeroQuantityError("Нельзя добавить товар с нулевым количеством")

            self.product = product
            print("Товар успешно добавлен")

        except ZeroQuantityError as e:
            print(e)

        finally:
            print("Обработка добавления товара завершена")
