from src.lexer import Lexer


lexer = Lexer("     nez age")


lexer.skip_whitespace()

print(lexer.current_character())