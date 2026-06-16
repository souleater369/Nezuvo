from src.lexer import Lexer


lexer = Lexer("age")

token = lexer.make_word_token()

print(token.token_type)
print(token.value)