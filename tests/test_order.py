import pytest

from src.exceptions import ZeroQuantityError
from src.order import Order
from src.product import Product


def test_order_creation():
    product = Product("продукт", "айфон 100 ультра про макс", 1000000.0, 5)
    order = Order("заказ", "доставка бесплатно", product, 3)

    assert order.product is product
    assert order.quantity == 3
    assert order.total_price == 3000000.0


def test_order_incorrect_amount():
    product = Product("продукт", "айфон 100 ультра про макс", 1000000.0, 5)
    with pytest.raises(ValueError):
        Order("something", "description", product, 6)
    with pytest.raises(ZeroQuantityError):
        Order("something", "description", product, 0)
    with pytest.raises(ZeroQuantityError):
        Order("something", "description", product, -3)


def test_order_str():
    product = Product("продукт", "айфон 100 ультра про макс", 1000000.0, 5)
    order = Order("заказ", "доставка бесплатно", product, 3)
    result = str(order)
    assert "продукт" in result
    assert "3" in result
    assert "3000000" in result


def test_order_add_product_success(capsys):
    product1 = Product("p1", "desc", 100.0, 5)
    product2 = Product("p2", "desc", 200.0, 10)
    order = Order("order", "desc", product1, 2)

    order.add_product(product2)

    assert order.product is product2

    captured = capsys.readouterr()
    assert "Товар успешно добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_order_add_product_zero_quantity(capsys):
    product1 = Product("p1", "desc", 100.0, 5)
    bad_product = Product("bad", "desc", 50.0, 1)
    bad_product.quantity = 0
    order = Order("order", "desc", product1, 1)

    order.add_product(bad_product)

    captured = capsys.readouterr()
    assert "Нельзя добавить товар с нулевым количеством" in captured.out
    assert order.product is product1  # не заменился


def test_order_add_product_not_a_product():
    product = Product("p1", "desc", 100.0, 5)
    order = Order("order", "desc", product, 1)

    with pytest.raises(TypeError):
        order.add_product("not a product")
