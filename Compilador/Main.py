from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Sintactico.Statements import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex


def Main():

    data = '''sGa, yt@, c_1, mew = False, 54, True, 5;'''

    analyzeData(data)

    try:
        parser = yacc.yacc()
        result = parser.parse(data)
        keys = list(variables.keys())
        for k in keys:
            variables[k] = valores.pop(0)
        print(variables)
        return
    except Exception:
        print("Error")
        return

Main()