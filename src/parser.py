from src.ast.nodes import VariableDeclaration, NumberLiteral, BinaryExpression

class Parser:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):

        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()

        else:
            raise Exception(
                f"Expected {token_type}, got {self.current_token.token_type}"
             )
        

    def parse_variable_declaration(self):

        self.eat("NEZ")

        name = self.current_token.value
        self.eat("IDENTIFIER")

        self.eat("EQUALS")

        value = self.parse_expression()

        return VariableDeclaration(name, value)
    
    def parse_number(self):

        value = self.current_token.value

        self.eat("NUMBER")

        return NumberLiteral(value)
    
    def parse_expression(self):

        node = self.parse_term()

        while self.current_token.token_type in ["PLUS", "MINUS"]:

            operator = self.current_token.value

            self.eat(self.current_token.token_type)

            right = self.parse_term()

            node = BinaryExpression(
                node,
                operator,
                right
            )

        return node
    
    def parse_factor(self):

        if self.current_token.token_type == "NUMBER":
            return self.parse_number()

        raise Exception("Invalid factor")
    
    def parse_term(self):

        node = self.parse_factor()

        while self.current_token.token_type in ["STAR", "SLASH"]:

            operator = self.current_token.value

            self.eat(self.current_token.token_type)

            right = self.parse_factor()

            node = BinaryExpression(
                node,
                operator,
                right
            )

        return node