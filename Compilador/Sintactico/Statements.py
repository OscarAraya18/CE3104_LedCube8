# ------------------------------------------------------------
# Codigo Fuente: Statements.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Define la gramatica para los statements
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

from Compilador.EstructurasDeDatos.Node import Node
from Compilador.EstructurasDeDatos.TreeNode import TreeNode
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.Ciclos import *
from Compilador.Sintactico.FuncionesReservadas import *

valores = []
valores2 = []
ids = []


def p_statements_1(p):
    '''statements : COMENTARIO statements'''
    p[0] = p[2]


def p_statements_2(p):
    '''statements : empty'''


def p_statements_3(p):
    '''statements : expression PUNTOCOMA statements'''
    p[0] = p[3]


def p_statements_4(p):
    '''statements : loop statements
                  | asignacion statements'''
    if p[2]:
        inst.insert(0, p[2])
    p[0] = p[1]



def p_statements_5(p):
    '''statements : funcionReservada statements'''
    funcList.insert(0, p[1])
    p[0] = p[2]


def p_statements_6(p):
    '''statements : bifurcacion statements'''
    funcList.insert(0, p[1])
    p[0] = p[1]

def p_statements_7(p):
    '''statements : rutina statements'''
    p[0] = p[2]


def p_asignacion_0(p):
    'asignacion : ID0 ASIGNACION valor PUNTOCOMA'
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if not id_en_variables:
        if len(valores) > 0:
            variables[ID] = [valores.pop()]
            # if isinstance(variables[ID][-1], list):
            #     print("WTF")
            #     variables[ID][-1] += valores2
        else:
            variables[ID] = [valores2.pop()]
    else:
        nodo = TreeNode("asignacion")
        nodo.add_child(ID)
        if len(valores) > 0:
            nodo.add_child(valores.copy())
            valores.clear()
            # if isinstance(variables[ID][-1], list):
            #     variables[ID][-1] += valores2
        else:
            nodo.add_child(valores2.pop())
        p[0] = nodo

def p_asignacion_1(p):
    'asignacion : ID0 COMA asignacion'
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if not id_en_variables:
        lenValores = len(valores)
        lenVariables = len(variables) - len(parametros)
        if (lenValores - lenVariables) >= 2:
            print("Error. La asignacion no es correcta")
            print("Linea: " + str(p.lineno(1)))
            raise Exception
        else:
            print("Valores: " + str(valores))
            variables[ID] = [valores.pop()]


def p_asignacion_2(p):
    'asignacion : ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMA'
    variables[p[1]] = [[]]


def p_asignacion_range(p):
    'asignacion : ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA'
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    list = []
    for x in range(p[5]):
        list.append(p[7])
    if not id_en_variables:
        variables[ID] = [list]
    else:
        nodo = TreeNode("asignacion")
        nodo.add_children([ID, list])
        p[0] = nodo


def p_asignacion_index(p):
    'asignacion : ID0 conjunto ASIGNACION valor PUNTOCOMA'
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("asignacion")
        nodo.add_children([ID, p[2]])
        if len(valores) > 0:
            nodo.add_child(valores.copy())
            valores.clear()
        else:
            nodo.add_child(valores2.pop())
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception


# def p_asignacion_index_2(p):
#     'asignacion : ID0 conjunto ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMA'
#     ID = p[1]
#     id_en_variables = variables.get(ID, False)
#     if id_en_variables != False:
#         nodo = TreeNode("asignacion")
#         nodo.add_children([ID, p[2], p[5]])
#         nodo.print()
#         p[0] = nodo
#     else:
#         print("Error. La variable no ha sido declarada")
#         print("Linea: " + str(p.lineno(1)))
#         raise Exception

def p_asignacion_index_3(p):
    'asignacion : ID0 conjunto ASIGNACION valor_b PUNTOCOMA'
    ID = p[1]
    id1_en_variables = variables.get(ID, False)
    if id1_en_variables != False:
        nodo = TreeNode("asignacion")
        if p[3] is None:
            nodo.add_child(ID)
        else:
            nodo.add_child([ID, p[2]])
        nodo.add_child(p[4])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception


def p_asignacion_index_4(p):
    'asignacion : ID0 ASIGNACION valor_b PUNTOCOMA'
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("asignacion")
        nodo.add_children([ID, p[3]])
        p[0] = nodo
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception


def p_if(p):
    '''bifurcacion : IF ID0 conjunto operador valor_b LLAVEI statements LLAVED PUNTOCOMA'''
    ID = p[2]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        nodo = TreeNode("if")
        if p[3] is not None:
            nodo.add_children([p[1], [ID, p[3]], p[4], p[5]])
        else:
            nodo.add_children([p[1], ID, p[4], p[5]])

        # for child in ifList:
        #     nodo.add_child(child)
        # ifList.clear()
        for child in funcList:
            nodo.add_child(child)
        p[0] = nodo
        funcList.clear()
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception


# def p_if_2(p):
#     '''bifurcacion : IF ID0 conjunto operador valor LLAVEI statements LLAVED PUNTOCOMA'''
#     print("Entra al if")


def p_operador(p):
    '''operador : COMPARACION
                | DISTINTOQUE
                | MENORQUE
                | MAYORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE '''
    p[0] = p[1]


def p_valor_0(p):
    '''valor : NUMERO
             | bool '''
    p[0] = p[1]
    valores.append(p[1])


def p_valor_1(p):
    '''valor : valor valor2 '''
    p[0] = valores


def p_valor_2(p):
    '''valor2 : COMA valor'''
    p[0] = p[2]


def p_valor_3(p):
    '''valor : lista'''
    p[0] = p[1]


def p_valor_b(p):
    '''valor_b : ID0 conjunto'''
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        p[0] = [ID, p[2]]
    else:
        print("Error. La variable no ha sido declarada")
        print("Linea: " + str(p.lineno(1)))
        raise Exception


def p_valor_b2(p):
    '''valor_b : NUMERO
               | bool '''
    p[0] = p[1]


def p_bool(p):
    '''bool : TRUE
            | FALSE'''
    p[0] = p[1]


def p_comentario_opcional(p):
    '''comentario_opcional : COMENTARIO
                           | empty'''


def p_lista_1(p):
    ''' lista : PARENTESISCI valor PARENTESISCD'''
    valores_aux = valores.copy()
    if len(valores) == 1:
        valores2.append(valores.copy()[0])
        valores.clear()
    else:
        lista = []
        if len(valores) > 0 and isinstance(valores[0], list):
            valores_aux2 = valores_aux.pop(0)
            valores_aux3 = valores_aux.copy()
            if isinstance(valores_aux2[0], list):
                if isinstance(valores_aux2[0][0], list):
                    lista.append(valores_aux2)
                else:
                    lista += valores_aux2
            else:
                lista.append(valores_aux2)
            lista.append(valores_aux3)
            valores.clear()
            valores.append(lista)
        else:
            valores.clear()
            valores.append(valores_aux)

    p[0] = valores.copy()
