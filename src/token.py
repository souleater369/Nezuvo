NUMBER = "NUMBER"
IDENTIFIER = "IDENTIFIER"
STRING = "STRING"

NEZ = "NEZ"

PLUS = "PLUS"
MINUS = "MINUS"
EQUALS = "EQUALS"

EOF = "EOF"


class Token:

    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value