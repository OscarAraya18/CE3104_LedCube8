# ------------------------------------------------------------
# Codigo Fuente: Ciclos.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Define la gramatica de los ciclos
#
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

from Compilador.EstructurasDeDatos.TreeNode import *
from Compilador.Sintactico.OperacionesMatematicas import *


def p_loop_for(p):
    '''loop : FOR ID0 IN iterable STEP NUMERO LLAVEI statements LLAVED PUNTOCOMA'''
    nodo = TreeNode("for")
    nodo.add_children([p[1], p[2], p[4], p[6]])

    for child in forList:
        nodo.add_child(child)
    forList.clear()

    for child in funcList:
        nodo.add_child(child)

    forList.insert(0, nodo)
    funcList.clear()

    #p[0] = nodo


def p_loop_for_2(p):
    '''loop : FOR ID0 IN iterable LLAVEI statements LLAVED PUNTOCOMA'''
    nodo = TreeNode("for")
    nodo.add_children([p[1], p[2], p[4], 1])

    for child in forList:
        nodo.add_child(child)

    forList.clear()
    for child in funcList:
        nodo.add_child(child)

    p[0] = nodo
    forList.insert(0, nodo)
    funcList.clear()


def p_iterable_1(p):
    '''iterable : NUMERO'''
    p[0] = [p[1]]


def p_iterable_2(p):
    '''iterable : ID0 conjunto'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        if p[2] is not None:
            p[0] = [ID, p[2]]
        else:
            p[0] = ID
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
