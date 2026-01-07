from typing import Any
from unittest.mock import patch

import pytest

from src.exceptions import ZeroQuantityError
from src.product import BaseProduct, LawnGrass, Product, Smartphone


# test initialization


def test_product(product_1):
    assert isinstance(product_1, Product)
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_smartphone(smartphone_1):
    assert isinstance(smartphone_1, Smartphone)
    assert isinstance(smartphone_1, Product)

    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_lawngrass(lawngrass_1):
    assert isinstance(lawngrass_1, LawnGrass)
    assert isinstance(lawngrass_1, Product)

    assert lawngrass_1.name == "Газонная трава"
    assert lawngrass_1.description == "Элитная трава для газона"
    assert lawngrass_1.price == 500.0
    assert lawngrass_1.quantity == 20
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"


# test adding via new_product method


def test_add_product(data_list_of_categories, category_1):
    product1_dict, product2_dict, product3_dict = data_list_of_categories[0]["products"][:3]
    product_1_object: Product = Product(**product1_dict)
    assert isinstance(product_1_object, Product)
    assert product_1_object.name == product1_dict["name"]
    assert product_1_object.description == product1_dict["description"]
    assert product_1_object.price == product1_dict["price"]
    assert product_1_object.quantity == product1_dict["quantity"]
    category_1.add_product(product_1_object)
    assert category_1.product_count == 1

    product_2_object, is_new = Product.new_product(product2_dict, category_1._products_list)
    assert isinstance(product_2_object, Product)
    assert is_new is True
    assert product_2_object.name == product2_dict["name"]
    assert product_2_object.description == product2_dict["description"]
    assert product_2_object.price == product2_dict["price"]
    assert product_2_object.quantity == product2_dict["quantity"]
    category_1.add_product(product_2_object)
    assert category_1.product_count == 2

    product_3_object, is_new = Product.new_product(product3_dict, category_1._products_list)
    assert isinstance(product_3_object, Product)
    assert is_new is False
    assert product_3_object.name == product3_dict["name"]
    assert product_3_object.name == product_2_object.name
    assert product_3_object.description == product_2_object.description
    assert product_3_object.price == product3_dict["price"]
    assert product_3_object.quantity == product3_dict["quantity"] + product2_dict["quantity"]
    assert product_3_object.quantity == product_2_object.quantity
    category_1.add_product(product_3_object)
    assert category_1.product_count == 3
    # так и должно быть, мы добавляем объект в список категории, new_product не добавляет себя сам ни в случае
    # если такого раньше не было, ни если добавлен новый продукт, а при добавлении через add_product мы
    # не проверяем был ли уже такой товар, или нет


def test_price_setter_negative(product_1):
    with patch("builtins.print") as mock_print:
        product_1.price = 0
        mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
        assert product_1.price == 180000.0

    with patch("builtins.print") as mock_print:
        product_1.price = -1
        mock_print.assert_called_with("Цена не должна быть нулевая или отрицательная")
        assert product_1.price == 180000.0


def test_price_setter_lowering_confirmation_yes(product_1):
    with patch("builtins.input", return_value="1"):
        product_1.price = 20
        assert product_1.price == 20


def test_price_setter_lowering_confirmation_no(product_1):
    with patch("builtins.input", return_value="0"):
        product_1.price = 20
        assert product_1.price == 180000.0


def test_price_setter_increase(product_1):
    product_1.price = 200000.0
    assert product_1.price == 200000.0


def test_string_representation(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_products(product_1, product_2, lawngrass_1, lawngrass_2, smartphone_1, smartphone_2):
    assert product_1 + product_2 == 2580000.0
    assert lawngrass_1 + lawngrass_2 == 16750.0
    assert smartphone_1 + smartphone_2 == 2580000.0


@pytest.mark.parametrize(
    "first, second",
    [
        ("smartphone_1", "lawngrass_1"),
        ("lawngrass_1", "smartphone_1"),
        ("product_1", "smartphone_1"),
        ("smartphone_1", "product_1"),
        ("product_1", "lawngrass_1"),
        ("lawngrass_1", "product_1"),
    ],
    indirect=["first", "second"],
)
def test_add_different_products(first: Product, second: Product):
    with pytest.raises(TypeError) as exc_info:
        first + second

    assert str(exc_info.value).startswith("Можно сложить только 2 одинаковых товара")


@pytest.mark.parametrize(
    "first, second",
    [
        ("smartphone_1", 123),
        ("lawngrass_1", "строка"),
        ("product_1", []),
        ("smartphone_1", {"key": "value"}),
        ("smartphone_1", None),
    ],
    indirect=["first"],
)
def test_add_invalid_types(first: Product, second: Any):
    with pytest.raises(TypeError) as exc_info:
        first + second

    assert str(exc_info.value).startswith("Оба объекта должны быть экземплярами класса Product. Получены объекты типа")


def test_add_non_product(smartphone_1):
    class NotProduct:
        pass

    not_product = NotProduct()

    with pytest.raises(TypeError) as exc_info:
        smartphone_1 + not_product

    assert str(exc_info.value).startswith("Оба объекта должны быть экземплярами класса Product. Получены объекты типа")


def test_init_log_mixin_prints_creation_info(capsys):
    Product("продукт", "описание", 99999.9, 10)

    captured = capsys.readouterr()

    assert "Product создан с параметрами" in captured.out
    assert "продукт" in captured.out
    assert "99999.9" in captured.out


def test_base_product_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct("something", "something else", 1000000000000000.0, 10000000)


def test_product_is_instance_of_base_product():
    product = Product("something", "something else", 1000000000000000.0, 10000000)

    assert isinstance(product, BaseProduct)


def test_zero_quantity_product_error():
    with pytest.raises(ZeroQuantityError) as exc_info:
        Product("something", "something else", 1000000000000000.0, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
