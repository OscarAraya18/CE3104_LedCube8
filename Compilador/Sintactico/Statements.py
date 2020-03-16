# ------------------------------------------------------------
# Codigo Fuente: Statements.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Define la gramatica para los statements
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *

variables = {}
valores = []

def p_asignacion_0(p):
    'asignacion : ID0 ASIGNACION valor PUNTOCOMA'

    variables[p[1]] = p[3]

    p[0] = p[3]

def p_asignacion_1(p):
    'asignacion : ID0 COMA asignacion'

    variables[p[1]] = p[3]


# def p_identificador(p):
#     '''identificador: ID0 | ID0 COMA identificador'''
#     if len(p[0] == 2):
#         p[0] = p[1]


def p_asignacion_index(p):
    'asignacion : ID0 PARENTESISCI NUMERO PARENTESISCD ASIGNACION valor PUNTOCOMA'
    p[0] = [p[1], p[3], p[6]]


def p_valor_0(p):
    '''valor : NUMERO
               | bool '''
    p[0] = p[1]
    valores.append(p[1])

def p_valor_1(p):
    '''valor : NUMERO COMA valor
               | bool COMA valor '''

    valores.append(p[1])
    p[0]= p[1]

def p_bool(p):
    '''bool : TRUE
            | FALSE'''
    p[0] = p[1]

