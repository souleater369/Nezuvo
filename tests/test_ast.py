from src.ast.nodes import BinaryExpression, NumberLiteral

node = BinaryExpression(
    NumberLiteral(10),
    "+",
    NumberLiteral(8)
)

print(node)