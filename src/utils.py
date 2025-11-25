import json
from pathlib import Path
from typing import Any, Sequence

from src.category import Category
from src.product import Product


def read_json_file(path: str | Path) -> Any:
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {path} не найден")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка декодирования JSON в файле {path}")


def import_products_from_json_file(path: str | Path) -> Sequence[Category]:
    products_dict = read_json_file(path)
    categories = []

    for category in products_dict:
        products: list[Product] = []

        for product_dict in category["products"]:
            new_product, is_new = Product.new_product(product_dict, products)

            if is_new:
                products.append(new_product)

        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    data = import_products_from_json_file("../data/example_products.json")
    for _ in data:
        print(f"{_}\n")
