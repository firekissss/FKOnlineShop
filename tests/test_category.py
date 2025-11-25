from src.category import Category
from src.product import Product


def test_category(category_1, category_2):
    assert isinstance(category_1, Category)
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.products) == 2

    assert isinstance(category_1.products[0], Product)
    assert isinstance(category_1.products[1], Product)

    assert category_1.products[0].name == "Samsung Galaxy S23 Ultra"
    assert category_1.products[1].description == "512GB, Gray space"

    assert category_1.category_count

    assert isinstance(category_2, Category)
    assert category_2.name == "Телевизоры"
    assert "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(category_2.products) == 1

    assert isinstance(category_2.products[0], Product)
    assert category_2.products[0].name == "Samsung Galaxy S23 Ultra"

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 3
    assert category_2.product_count == 3
