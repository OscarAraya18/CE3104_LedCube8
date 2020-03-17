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

variables = {'x' : []}
valores = []

def p_asignacion_0(p):
    'asignacion : ID0 ASIGNACION valor PUNTOCOMA'
    ID = p[1]
    id_en_variables = variables.get(ID,False)
    if not id_en_variables:
        variables[ID] = valores.pop()
    else:
        valor = variables[ID]
        if isinstance(valor, p[3]):
            variables[ID] = p[3]

def p_asignacion_1(p):
    'asignacion : ID0 COMA asignacion'
    ID = p[1]
    id_en_variables = variables.get(ID, False)

    if not id_en_variables:
        variables[ID] = valores.pop()
    else:
        valor = variables[ID]
        if isinstance(valor, p[3]):
            variables[ID] = p[3]


def p_asignacion_2(p):
    'asignacion : ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMA'
    variables[p[1]] = []


def p_asignacion_3(p):
    'asignacion : ID0 ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMA'
    variables[p[1]] = [p[4]]


def p_asignacion_index(p):
    'asignacion : ID0 PARENTESISCI NUMERO PARENTESISCD ASIGNACION valor PUNTOCOMA'

    ID = p[1]
    id_en_variables = variables.get(ID,False)
    print(id_en_variables)
    if id_en_variables != False:
        valor = variables[ID]
        if isinstance(valor, list):
            if len(valor) > p[3]:
                valor[p[3]] = p[6]
                variables[ID] = valor
            else:
                print("Indice fuera de rango")
        else:
            print("La variable no es indexable")
    else:
        print("La variable no ha sido declarada")

def p_valor_0(p):
    '''valor : NUMERO
               | bool '''
    p[0] = p[1]
    valores.append(p[1])

def p_valor_1(p):
    '''valor : valor valor2 '''
    p[0] = p[2]

def p_valor_2(p):
    '''valor2 : COMA valor'''
    p[0] = p[2]


def p_bool(p):
    '''bool : TRUE
            | FALSE'''
    p[0] = p[1]

def comentario_opcional(p):
    '''comentario_opcional: COMENTARIO | empty'''