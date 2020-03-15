from Compilador.EstructurasDeDatos.Node import *
from Compilador.Sintactico.OperacionesMatematicas import *

def p_loop_for(p):
    'loop : FOR variable IN iterable STEP salto LLAVEI statement LLAVED PUNTOCOMA'
    p[0] = Node("loop")