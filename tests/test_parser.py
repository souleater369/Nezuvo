from src.lexer import Lexer
from src.parser import Parser


lexer = Lexer("10 + 8 * 2")

parser = Parser(lexer)

node = parser.parse_expression()

print(node)