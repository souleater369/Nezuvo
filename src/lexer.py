from src.token import Token, IDENTIFIER, NUMBER, EQUALS, EOF


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
    
    def skip_whitespace(self):
        while self.has_more_characters() and self.current_character().isspace():
            self.advance()


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
    
    def read_number(self):
        number = ""

        while self.has_more_characters() and self.current_character().isdigit():
            number += self.current_character()
            self.advance()

        return number
    
    def get_next_token(self):
    

        while self.has_more_characters():

            current = self.current_character()

            if current.isspace():
                self.skip_whitespace()
                continue

            if current.isalpha():
                return self.make_word_token()

            if current.isdigit():
                number = self.read_number()
                return Token(NUMBER, number)

            if current == "=":
                self.advance()
                return Token(EQUALS, "=")
        return Token(EOF,None)