from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Parser import *

def Main():
    data = ''' Procedure Main(){
        x = range(5, True);
    };
    '''

    # analyzeData(data)

    # Build the lexer
    lexer = lex.lex()
    # Receive input
    lexer.input(data)

    try:
        result = parse(lexer)
        print("Exito: " + str(result))

        return
    except Exception:
        print("Error")
        return


Main()
