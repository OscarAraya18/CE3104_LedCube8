import Compilador.ply.ply.yacc as yacc
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Sintactico.Statements import *

start = 'estructura'


def p_estructura(p):
    '''estructura : main\
    MODULO'''


def p_main(p):
    '''main : PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    print("Entra al main")
    p[0] = p[6]

# Build the parser
def parse(lex):
    parser = yacc.yacc()
    astTree = parser.parse(lexer = lex)
    return astTree