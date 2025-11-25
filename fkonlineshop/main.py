from src.category import Category
from src.product import Product


def main() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)

    print("\n")

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    print("\n")

    # Пришлось немного изменить, чтобы работало доп. задание (проверка на уже существующий продукт)
    new_product, is_new = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        category1._products_list,
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)
    print("Продукт добавлен" if is_new else "Продукт уже был в списке, количество и(или) цена изменены")

    print("\n")

    new_product.price = 800
    print(new_product.price)

    print("\n")

    new_product.price = -100
    print(new_product.price)

    print("\n")

    new_product.price = 0
    print(new_product.price)


if __name__ == "__main__":
    main()
