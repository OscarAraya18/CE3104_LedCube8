from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Sintactico.Statements import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex


def Main():

    data = '''x , y , z = 1 ,  2 ,3;'''

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