from src.product import Product


class Category:
    # object attributes
    name: str
    description: str
    products: list[Product]

    # class attributes
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __repr__(self) -> str:
        return f"Name: {self.name}.\n" f"Description: {self.description}.\n" f"Products: {self.products}"
