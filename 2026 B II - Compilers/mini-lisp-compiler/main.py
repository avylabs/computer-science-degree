from lexical import lexical_analysis
from syntax import Parser



f_path = input("Insira caminho do arquivo a ser compilado: ")
source_code = open(f_path).read()

lexic_table = lexical_analysis(source_code)

print("NUM       TOKEN                     LEXEMA")
print("===       ==================        ======")
index = 1
for i in lexic_table:
    print(f"{index}         {i[0]}      {i[1]}")
    index += 1

print("---------------------------------------------------")
print("ANÁLISE SINTÁTICA")
print("=================")

print(Parser(lexic_table).parse())
