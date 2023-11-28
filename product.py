class Product():
    def __init__(self, name, space, value):
        self.name = name
        self.space = space
        self.value = value

    def __repr__(self):
        return f"{self.name} - R$ {self.value} - {self.space} m³"
