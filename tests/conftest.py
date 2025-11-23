import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return product1


@pytest.fixture
def product_2():
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return product2


@pytest.fixture
def category_1(product_1, product_2):
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2],
    )
    return category1


@pytest.fixture
def category_2(product_1):
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_1],
    )
    return category2
