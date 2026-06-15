class Lexer:

    def __init__(self, text):
        self.text = text
        self.position = 0

    def current_character(self):
        return self.text[self.position]

    def advance(self):
        self.position += 1

    def skip_whitespace(self):
        while self.position < len(self.text) and self.text[self.position] == " ":
            self.advance()