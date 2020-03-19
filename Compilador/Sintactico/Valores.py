# ------------------------------------------------------------
# Codigo Fuente: Valores.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Define la gramatica para acceder a los valores de alguna variable
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

from Compilador.Lexer.AnalizadorLexico import *
from Compilador.ply.ply import yacc

variables = {'x' : [1,2,3,4]}


def p_index_list(p):
    '''indexar : ID0 PARENTESISCI NUMERO PARENTESISCD'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        valor = variables[ID]
        if isinstance(valor, list):
            if len(valor) > p[3]:
                p[0] = valor[p[3]]
            else:
                print("Error. Indice fuera de rango")
        else:
            print("Error. La variable no es indexable")
    else:
        print("Error. La variable no ha sido declarada")


def p_index_list_2(p):
    '''indexar : ID0 PARENTESISCI NUMERO DOSPUNTOS NUMERO PARENTESISCD'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        valor = variables[ID]
        if isinstance(valor, list):
            if len(valor) > p[5] and p[3] < p[5]:
                p[0] = valor[p[3]:p[5]]
            else:
                print("Error. Indice fuera de rango")
        else:
            print("Error. La variable no es indexable")
    else:
        print("Error. La variable no ha sido declarada")

def p_index_list_3(p):
    '''indexar : ID0 PARENTESISCI DOSPUNTOS NUMERO PARENTESISCD'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        valor = variables[ID]
        if isinstance(valor, list):
            if len(valor) > p[4]:
                p[0] = valor[:p[4]]
            else:
                print("Error. Indice fuera de rango")
        else:
            print("Error. La variable no es indexable")
    else:
        print("Error. La variable no ha sido declarada")



yacc.yacc()