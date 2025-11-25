from pathlib import Path

import pytest

from src.category import Category
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
    assert isinstance(cat.products, str)
    assert cat.products == "Samsung, 10.0 руб. Остаток: 11 шт.\nIphone, 30.0 руб. Остаток: 24 шт."


def test_import_products_from_json_file_empty_list(tmp_path: Path):
    file_path = tmp_path / "empty_list.json"
    file_path.write_text("[]")

    categories = import_products_from_json_file(file_path)
    assert isinstance(categories, list)
    assert len(categories) == 0
