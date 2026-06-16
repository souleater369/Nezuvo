from src.token import Token, IDENTIFIER


KEYWORDS = {
    "nez": "NEZ",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "funct": "FUNCT",
    "return": "RETURN",
    "printu": "PRINTU"
}


class Lexer:

    def __init__(self, text):
        self.text = text
        self.position = 0


    def current_character(self):
        return self.text[self.position]


    def advance(self):
        self.position += 1


    def has_more_characters(self):
        return self.position < len(self.text)


    def read_word(self):
        word = ""

        while self.has_more_characters() and self.current_character().isalpha():
            word += self.current_character()
            self.advance()

        return word


    def make_word_token(self):
        word = self.read_word()

        if word in KEYWORDS:
            return Token(KEYWORDS[word], word)

        return Token(IDENTIFIER, word)