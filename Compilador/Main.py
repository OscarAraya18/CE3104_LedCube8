from Compilador.Lexer import AnalizadorLexico
from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
#from Compilador.Sintactico.Statements import *
from Compilador.Sintactico.Valores import *
#from Compilador.Sintactico.OperacionesMatematicas import *


def Main():
    data = '''x[0]'''

    # analyzeData(data)

    # Build the lexer
    lexer = lex.lex()
    # Receive input
    lexer.input(data)

    try:
        parser = yacc.yacc()
        result = parser.parse(lexer = lexer)
        print("Me interesa: " + str(result))

        return
    except Exception:
        print("Error")
        return


Main()
