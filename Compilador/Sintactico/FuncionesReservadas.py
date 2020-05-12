# ------------------------------------------------------------
# Codigo Fuente: FuncionesReservadas.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Gramatica de las funciones reservadas
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------


from Compilador.EstructurasDeDatos.TreeNode import TreeNode
from Compilador.Sintactico.OperacionesMatematicas import *


param = []

def p_insert(p):
    '''funcionReservada : ID0 PUNTO INSERT PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[3], p[1], p[5], p[7]])
        p[0] = nodo

    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra al insert")

def p_insert_2(p):
    '''funcionReservada : ID0 PUNTO INSERT PARENTESISI valor COMA tipo COMA NUMERO PARENTESISD PUNTOCOMA'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[3], p[1], p[5], p[7], p[9]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra al insert")

def p_insert_3(p):
    '''funcionReservada : ID0 PUNTO INSERT PARENTESISI valor COMA NUMERO PARENTESISD PUNTOCOMA '''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[3], p[1], p[5], p[7]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra al insert")


def p_del(p):
    '''funcionReservada : ID0 PUNTO DEL PARENTESISI NUMERO PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[3], p[1], p[5]])
    p[0] = nodo
    print("Entra al del")

def p_del_2(p):
    '''funcionReservada : ID0 PUNTO DEL PARENTESISI NUMERO COMA tipo PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[3], p[1], p[5], p[7]])
    p[0] = nodo
    print("Entra al del")


def p_len(p):
    '''funcionReservada :  LEN PARENTESISI ID0 PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[1], p[3]])
    p[0] = nodo
    print("Entra al len")


def p_neg(p):
    '''funcionReservada : ID0 conjunto PUNTO NEG PUNTOCOMA'''
    ID  = p[1]
    id_en_variables = variables.get(ID, False)
    if  id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[4], [p[1], p[2]]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra al neg ")


def p_t(p):
    '''funcionReservada : ID0 conjunto PUNTO T PUNTOCOMA'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[4], [p[1], p[2]]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra al T")


def p_f(p):
    '''funcionReservada : ID0 conjunto PUNTO F PUNTOCOMA'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[4], [p[1], p[2]]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra al F")


def p_blink_1(p):
    '''funcionReservada : BLINK PARENTESISI ID0 conjunto COMA NUMERO COMA rango COMA bool PARENTESISD PUNTOCOMA '''
    ID = p[3]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        if p[4] is None:
            nodo.add_children([p[1], p[3], p[6], p[8], p[10]])
        else:
            nodo.add_children([p[1], [p[3], p[4]], p[6], p[8], p[10]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra a blink")


def p_blink_2(p):
    '''funcionReservada : BLINK PARENTESISI ID0 conjunto COMA bool PARENTESISD PUNTOCOMA'''
    ID = p[3]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        if p[4] is None:
            nodo.add_children([p[1], p[3], p[6]])
        else:
            nodo.add_children([p[1], [p[3], p[4]], p[6]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception
    print("Entra a blink")


def p_delay_1(p):
    '''funcionReservada : DELAY PARENTESISI PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_child(p[1])
    p[0] = nodo
    print("Entra al delay")

def p_delay_2(p):
    '''funcionReservada : DELAY PARENTESISI NUMERO COMA rango PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[1], p[3], p[5]])
    p[0] = nodo
    print("Entra al delay")

def p_shapeF(p):
    '''funcionReservada : ID0 PUNTO SHAPEF'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[3], ID])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception

def p_shapeC(p):
    '''funcionReservada : ID0 PUNTO SHAPEC'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[3], ID])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception

def p_shapeA(p):
    '''funcionReservada : ID0 PUNTO SHAPEA'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("funcion")
        nodo.add_children([p[3], ID])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception


def p_call(p):
    '''funcionReservada : CALL ID0 PARENTESISI parametrosFuncion PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[1], p[2], param.copy()])
    param.clear()
    print("Entra al call")
    print(variables)
    p[0] = nodo

def p_rango(p):
    '''rango : SEG
             | MIN
             | MIL'''

    p[0] = p[1]

def p_tipo(p):
    '''tipo : NUMERO '''
    if p[1] == 0 or p[1] == 1:
        p[0] = p[1]
    else:
        print("Error en la linea: " + str(p.lineno(1)))
        raise Exception


def p_conjunto_1(p):
    '''conjunto : PARENTESISCI indice DOSPUNTOS indice PARENTESISCD'''
    p[0] = [p[2], p[3], p[4]]

def p_conjunto_2(p):
    '''conjunto : PARENTESISCI DOSPUNTOS indice PARENTESISCD'''
    p[0] = [p[2], p[3]]

def p_conjunto_3(p):
    '''conjunto : PARENTESISCI indice PARENTESISCD'''
    p[0] = [p[2]]

def p_conjunto_4(p):
    '''conjunto : PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD '''
    p[0] = [p[2], p[5]]

def p_conjunto_5(p):
    '''conjunto : empty'''

def p_rango_matriz_1(p):
    '''rango_matriz : PARENTESISCI indice PARENTESISCD'''
    p[0] = [p[2]]

def p_rango_matriz_2(p):
    '''conjunto : PARENTESISCI indice COMA indice PARENTESISCD'''
    p[0] = [p[2], p[3], p[4]]

def p_rango_matriz_3(p):
    '''conjunto : PARENTESISCI DOSPUNTOS COMA indice PARENTESISCD'''
    p[0] = [p[2], p[3], p[4]]

def p_rango_matriz_4(p):
    '''conjunto : PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD'''
    p[0] = [p[2], p[5], p[8]]


def p_parametros_funcion_1(p):
    '''parametrosFuncion : ID0
                         | NUMERO
                         | empty'''

    if p[1]:
        param.insert(0, p[1])


def p_parametros_funcion_2(p):
    '''parametrosFuncion : ID0 COMA parametrosFuncion'''
    param.insert(0, p[1])

def p_parametros_funcion_3(p):
    '''parametrosFuncion : NUMERO COMA parametrosFuncion'''
    param.insert(0, p[1])

def p_indices(p):
    '''indice : NUMERO
              | ID0'''
    p[0] = p[1]