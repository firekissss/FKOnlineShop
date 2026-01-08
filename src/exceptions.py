class ZeroQuantityError(Exception):
    def __init__(self, message: str = "Объект с нулевым количеством не может быть добавлен"):
        super().__init__(message)
