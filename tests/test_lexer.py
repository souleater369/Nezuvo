from src.lexer import Lexer


lexer = Lexer("nez age = 18")


while True:
    token = lexer.get_next_token()

    print(token)

    if token.token_type == "EOF":
        break