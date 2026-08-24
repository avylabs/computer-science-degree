#<program> ::= <expr>
#<expr> ::= <atom> | <list>
#<atom> ::= <number> | <symbol>
#<number> ::= <integer> | <float>
#<symbol> ::= <operator> | <keyword> | <identifier>
#<list> ::= "(" <expr_list> ")"
#<expr_list> ::= <expr> <expr_list> | ε

from token import TokenType

class Parser:

    def __init__(self, token_table):
        self.token_table = token_table
        self.tk_index = 0

    def current_token(self):
        return self.token_table[self.tk_index] if self.tk_index < len(self.token_table) else None

    def advance(self):
        token = self.current_token()
        self.tk_index += 1
        return token

    def parse(self):
        program = self.expr()
        if self.current_token() is not None:
            print(f"\033[31mERRO: Token inesperado: {self.current_token()}\033[0m")
        return program

    def expr(self):
        token = self.current_token()
        if token[0] is TokenType.TK_OPENPAR:
            return self.list()
        if token[0] is TokenType.TK_CLOSEPAR:
            print("\033[31mERRO: ) inesperado\033[0m")
        return self.atom()

    def list(self):
        self.advance()
        content = self.expr_list()

        if self.current_token() is None or self.current_token()[0] is not TokenType.TK_CLOSEPAR:
            print("\033[31mERRO: ) não encontrado\033[0m")
        self.advance()
        return content

    def expr_list(self):
        i = []
        while self.current_token() is not None and self.current_token()[0] is not TokenType.TK_CLOSEPAR:
            i.append(self.expr())
        return i

    def atom(self):
        token = self.advance()
        return token
