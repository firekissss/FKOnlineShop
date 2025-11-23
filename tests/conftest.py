import json
from pathlib import Path

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


@pytest.fixture
def tmp_json_file(tmp_path: Path) -> Path:
    data = [
        {
            "name": "Smartphones",
            "description": "Very expensive low-memory phones",
            "products": [
                {
                    "name": "Samsung",
                    "description": "10GB",
                    "price": 10.0,
                    "quantity": 11,
                },
                {
                    "name": "Iphone",
                    "description": "20GB",
                    "price": 20.0,
                    "quantity": 12,
                },
            ],
        }
    ]

    file_path = tmp_path / "products.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    return file_path
