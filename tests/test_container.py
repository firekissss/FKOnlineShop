import pytest

from src.category import Category
from src.container import ProductContainer


def test_container_no_init():
    with pytest.raises(TypeError):
        ProductContainer("name", "description")


def test_container_is_parent():
    category = Category("Категория", "Описание", [])
    assert isinstance(category, ProductContainer)
