import pytest

from src.iterators import CategoryIterator


def test_category_iterator(product_1, product_2, category_1):
    category_1.add_product(product_1)
    category_1.add_product(product_2)
    iterator = CategoryIterator(category_1)
    result = list(iterator)
    assert result == [product_1, product_2]


def test_category_iterator_stop_iteration(product_1, category_1):
    category_1.add_product(product_1)
    iterator = CategoryIterator(category_1)
    next(iterator)
    with pytest.raises(StopIteration):
        next(iterator)
