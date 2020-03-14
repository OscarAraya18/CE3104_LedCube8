from EstructurasDeDatos.TreeNode import *
from Sintactico.OperacionesMatematicas import *

def p_loop_for(p):
    'loop : FOR expression IN statements STEP SEMICOLON'
    loopNode = TreeNode("loop")
    loopNode.add_children([p[1], p[2], p[5]])
    for child in funcList:
        loopNode.add_child(child)
    p[0] = loopNode
    funcList.clear()