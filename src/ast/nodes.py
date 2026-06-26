class VariableDeclaration:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"VariableDeclaration({self.name}, {self.value})"

class NumberLiteral:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberLiteral({self.value})"

class BinaryExpression:

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BinaryExpression({self.left}, {self.operator}, {self.right})"