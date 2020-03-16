# ------------------------------------------------------------
# Codigo Fuente: Condicionales.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Define la gramatica de los condicionales
#
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------


from Compilador.ply.ply import yacc
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.EstructurasDeDatos.Node import *


def p_condicional_if(p):
    '''condicional: IF variable operador valor LLAVEI LLAVED'''
    p[0] = Node("condicional", [p[2], p[3], p[4]])

def p_valor(p):
    '''valor: NUMERO | TRUE | FALSE'''
    p[0] = p[1]

def p_variable(p):
    '''variable: valor | lista'''
    p[0] = p[1]

def p_operador(p):
    '''operador: COMPARACION | DISTINTOQUE |
    MENORQUE | MAYORQUE |  MAYORIGUALQUE | MENORIGUALQUE'''
    p[0] = p[1]

