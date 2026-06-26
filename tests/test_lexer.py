from src.lexer import Lexer
from src.parser import Parser


lexer = Lexer("10 + 8 * 2")

while True:
    token = lexer.get_next_token()
    print(token)

    if token.token_type == "EOF":
        break