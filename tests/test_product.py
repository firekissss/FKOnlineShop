from unittest.mock import patch

from src.product import Product


# test initialization


def test_product(product_1):
    assert isinstance(product_1, Product)
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


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
