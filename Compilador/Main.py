from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
#from Compilador.Sintactico.Statements import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Valores import *

def Main():

    data = '''x[3]'''

    analyzeData(data)

    try:
        parser = yacc.yacc()
        result = parser.parse(data)
        print("Me interesa: " + str(variables))
        return
    except Exception:
        print("Error")
        return

Main()