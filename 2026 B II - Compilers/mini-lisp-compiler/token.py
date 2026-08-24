from enum import Enum, auto

class TokenType(Enum):
    TK_NUMBER = auto() # [0-9] ou números decimais com .
    TK_OPERATOR = auto()  #  -, *, /, %, >, <, ==, !=, <=, >=
    TK_KEYWORDS = auto()# if, while, begin, set, print
    TK_IDENTIFIER = auto()
    TK_OPENPAR = auto() # (
    TK_CLOSEPAR = auto() # )
    TK_END = auto() # ''
