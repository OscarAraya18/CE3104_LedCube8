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

from Compilador.EstructurasDeDatos.Node import *

def p_loop_for(p):
    'loop : FOR ID0 IN iterable STEP salto LLAVEI statements LLAVED PUNTOCOMA'
    print("Reconoce el FOR")


def p_iterable(p):
    '''iterable : NUMERO
                | lista'''

def p_salto(p):
    '''salto : NUMERO
             | empty'''