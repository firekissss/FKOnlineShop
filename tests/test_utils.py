from pathlib import Path

import pytest

from src.category import Category
from src.product import Product
from src.utils import import_products_from_json_file, read_json_file


# test read_json


def test_read_json_correct(tmp_json_file: Path):
    data = read_json_file(tmp_json_file)
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Smartphones"
    assert isinstance(data[0]["products"], list)


def test_read_json_no_file():
    with pytest.raises(FileNotFoundError):
        read_json_file("something.json")


def test_read_json_decode_error(tmp_path):
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text("{ something")
    with pytest.raises(ValueError):
        read_json_file(invalid_file)


# test import_products_from_json_file


def test_import_products_from_json_file_correct(tmp_json_file: Path):
    categories = import_products_from_json_file(tmp_json_file)

    assert isinstance(categories, list)
    assert len(categories) == 1

    cat = categories[0]
    assert isinstance(cat, Category)
    assert cat.name == "Smartphones"
    assert isinstance(cat.products, list)
    assert len(cat.products) == 2

    prod1 = cat.products[0]
    assert isinstance(prod1, Product)
    assert prod1.name == "Samsung"
    assert isinstance(prod1.quantity, int)
    assert prod1.price == 10

    prod2 = cat.products[1]
    assert isinstance(prod2, Product)
    assert prod2.name == "Iphone"
    assert isinstance(prod2.price, float)
    assert prod2.quantity == 12


def test_import_products_from_json_file_empty_list(tmp_path: Path):
    file_path = tmp_path / "empty_list.json"
    file_path.write_text("[]")

    categories = import_products_from_json_file(file_path)
    assert isinstance(categories, list)
    assert len(categories) == 0
