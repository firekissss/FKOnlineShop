from src.product import Product


class Category:
    # class attributes
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        output_list = []
        # adding to list is more optimized than adding to a string
        for product in self.__products:
            output_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

        return "\n".join(output_list)

    @property
    def _products_list(self) -> list[Product]:
        return self.__products
