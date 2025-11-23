import json
from typing import Any, Sequence

from src.category import Category
from src.product import Product


def read_json_file(path: str) -> Any:
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {path} не найден")
    except json.JSONDecodeError:
        raise ValueError(f"Ошибка декодирования JSON в файле {path}")


def import_products_from_json_file(path: str) -> Sequence[Category]:
    products_dict = read_json_file(path)
    categories = []
    for category in products_dict:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    data = import_products_from_json_file("../data/example_products.json")
    for _ in data:
        print(f"{_}\n")
