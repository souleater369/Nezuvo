from src.token import Token, IDENTIFIER


token = Token(IDENTIFIER, "age")

print(token.token_type)
print(token.value)