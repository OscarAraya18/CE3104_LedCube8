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
from Compilador.Sintactico.OperacionesMatematicas import *

def p_loop_for(p):
    'loop : FOR variable IN iterable STEP salto LLAVEI statement LLAVED PUNTOCOMA'
    p[0] = Node("loop")