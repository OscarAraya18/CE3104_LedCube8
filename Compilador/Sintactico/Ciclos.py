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
    'loop : FOR ID0 IN iterable STEP NUMERO LLAVEI statements LLAVED PUNTOCOMA'
    loopNode = TreeNode("loop")
    loopNode.add_children([p[1], p[2], p[4], p[6]])
    for child in funcList:
        loopNode.add_child(child)
    print("Reconoce el FOR")
    p[0] = loopNode
    funcList.clear()

def p_loop_for_2(p):
    'loop : FOR ID0 IN iterable LLAVEI statements LLAVED PUNTOCOMA'
    loopNode = TreeNode("loop")
    loopNode.add_children([p[1], p[2], p[4]])
    for child in funcList:
        loopNode.add_child(child)
    print("Reconoce el FOR")
    p[0] = loopNode
    funcList.clear()



def p_iterable_1(p):
    '''iterable : NUMERO
                | ID0'''
    p[0] = [p[1]]

def p_iterable_2(p):
    '''iterable : ID0 conjunto'''
    p[0] = [p[1], p[2]]