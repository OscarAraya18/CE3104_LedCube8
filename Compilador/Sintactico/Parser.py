import Compilador.ply.ply.yacc as yacc
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Sintactico.Statements import *


tablaSimbolos = {}

start = 'estructura'


def p_estructura(p):
    '''estructura : main\
    '''


def p_main(p):
    '''main : PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    print("Entra al main")
    p[0] = p[6]


def p_rutina(p):
    '''rutina : PROCEDURE ID0 PARENTESISI parametros PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    print("Entra a proceso")

def p_parametros_1(p):
    '''parametros : ID0
                  | empty'''
    p[0] = p[1]

def p_parametros_2(p):
    '''parametros : ID0 COMA parametros'''
    p[0] = p[2]

#Se crea el parser
def parse(lex):
    parser = yacc.yacc()
    astTree = parser.parse(lexer=lex)
    return astTree