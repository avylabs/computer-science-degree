from token import TokenType

def is_number(num):
    if num is None:
        return False
    try:
        float(num)
        return True
    except:
        return False

def check_delimiter(ch):
    if ch == '(':
        return (TokenType.TK_OPENPAR, "(")

    if ch == ')':
        return (TokenType.TK_CLOSEPAR, ")")


def lexical_analysis(source_code):
    state = 1
    tk_table = []
    temp_lexic = ''
    for ch in source_code:
        match state:
            case 1:
                if ch.isspace(): # Pular espaços.
                    state = 1

                # Verificar se é um digito alfabético
                elif ch.isalpha():
                    state = 2
                    temp_lexic += ch

                # Verificar se é um dígito numérico
                elif ch.isdigit() or ch == '.':
                    state = 3
                    temp_lexic += ch

                # Verificar se é um operador
                elif ch in {"-", "+", "*", "/", "%", "<", ">", "=", "!"}:
                    state = 4
                    temp_lexic += ch
                elif ch in {"(", ")"}:
                    tk_table.append(check_delimiter(ch))

                else:
                    print("\033[31mERRO: Caractere inválido\033[0m")
                    break
            
            case 2:
                if ch.isspace() or ch in {"(", ")"}:
                    if temp_lexic in {"if", "while", "begin", "set", "print"}:
                        tk_table.append((TokenType.TK_KEYWORDS, temp_lexic))

                    else:
                        tk_table.append((TokenType.TK_IDENTIFIER, temp_lexic))
                    temp_lexic = ''
                    state = 1
                    if ch in {"(", ")"}:
                        tk_table.append(check_delimiter(ch))

                elif ch.isalpha():
                    temp_lexic += ch
                    state = 2

                else:
                    print("\033[31mERRO: Identificador contém caracteres não alfabéticos\033[0m")
                    break

            case 3:
                if ch.isspace() or ch in {"(", ")"}:
                    if is_number(temp_lexic):
                        tk_table.append((TokenType.TK_NUMBER, temp_lexic))
                    else:
                        print("\033[31mERRO: Número escrito incorretamente.\033[0m")
                        break
                    temp_lexic = ''
                    state = 1
                    if ch in {"(", ")"}:
                        tk_table.append(check_delimiter(ch))

                elif ch.isdigit():
                    temp_lexic += ch
                    state = 3

                # Verificar se número já possui ponto antes de adicionar.
                elif ch == '.':
                    if '.' in temp_lexic:
                        print("\033[31mERRO: Número malformado.\033[0m")
                        break
                    else:
                        temp_lexic += ch
                    state = 3

                else:
                    print("\033[31mERRO: Número possui caracteres inválidos\033[0m")
                    break

            case 4:
                if ch.isspace() or ch in {"(", ")"}:
                    tk_table.append((TokenType.TK_OPERATOR, temp_lexic))
                    temp_lexic = ''
                    state = 1
                elif ch in {"="}:
                    temp_lexic += ch
                    state = 4
                else:
                    print("\033[31mERRO: OPERADOR INVÁLIDO\033[0m")
                    break
    return tk_table

