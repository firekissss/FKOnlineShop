class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Name: {self.name}. Description: {self.description}. Price: {self.price}. Quantity: {self.quantity}"
