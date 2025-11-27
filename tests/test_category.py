from src.category import Category
from src.iterators import CategoryIterator


# test initializing


def test_category(category_1, category_2, product_1, product_2):
    assert isinstance(category_1, Category)
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert isinstance(category_2, Category)
    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


def test_category_adding_products(category_1, category_2, product_1, product_2):
    # test products getter (empty for now)
    assert isinstance(category_1.products, str)
    assert category_1.products == ""

    assert isinstance(category_2.products, str)
    assert category_2.products == ""

    # test add_products (almost products setter, but it's not)
    category_1.add_product(product_1)
    category_2.add_product(product_2)

    # now there will be some products, checking them with getter
    assert category_1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert category_2.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт."

    # test class attributes
    assert Category.category_count == 2
    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert Category.product_count == 2
    assert category_1.product_count == 2
    assert category_2.product_count == 2


def test_string_representation(category_1, product_1, product_2):
    category_1.add_product(product_1)
    category_1.add_product(product_2)
    assert str(category_1) == "Смартфоны, количество продуктов: 13 шт."


def test_category_iter_returns_iterator(product_1, product_2, category_1):
    category_1.add_product(product_1)
    category_1.add_product(product_2)
    it = iter(category_1)

    assert isinstance(it, CategoryIterator)

    result = list(category_1)
    assert result == [product_1, product_2]
