# FKOnlineShop

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

**FKOnlineShop** — это консольное приложение для импорта товаров по категориям из файла .json. Реализация включает в себя применение функционального и объектно-ориентированного программирования.

---

## Возможности

### Функционал
* Импорт и авто-конвертация в объекты содержимого .json-файла.


### Используются следующие классы:
* Класс Category
* Класс Product

Классы поддерживают инициализацию объектов, имеют собственное представление (representation, или __repr__). Класс Category имеет счётчики товаров и категорий, которые заполняются автоматически при инициализации.

---

## Установка

### Требования

* Python 3.10+
* pip / poetry
* Установленные зависимости из `pyproject.toml`

### Установка через Poetry

```bash
git clone https://github.com/firekissss/FKOnlineShop.git
cd firefinance
poetry install
```

### Запуск проекта

```bash
poetry run python fkonlineshop/main.py
```

---

## Настройка

### Переменные окружения

Проект пока не использует внешние API. Можете не создавать `.env` файл:

```
<smth from .env-example>
```

---

## Примеры использования

### 1. Импорт транзакций

```python
from src.utils import import_products_from_json_file

example_products = import_products_from_json_file("data/example_products.json")
print(example_products)
```

---

## Тесты

Для автоматизированного тестирования использован [pytest](https://docs.pytest.org/).  
Тесты содержатся в папке `tests/`. Использованы фикстуры для переиспользования тестовых данных, включая корректные и некорректные значения, а также граничные случаи.

### Запуск тестов

Для запуска тестов введите:

```bash
pytest
```

Также можно протестировать отдельно модуль или функцию:

```bash
pytest tests/test_module_name.py
pytest tests/test_module_name.py::test_function_name
```

---

## Документация и ссылки

* Репозиторий: [https://github.com/firekissss/FKOnlineShop](https://github.com/firekissss/FKOnlineShop)
* smth else

---

## Лицензия

Проект распространяется под лицензией **MIT License**.

Вы можете свободно использовать, изменять и распространять проект при указании авторства.
