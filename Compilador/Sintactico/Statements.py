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



variables = {}
valores = []

def p_statements_1(p):
    '''statements : asignacion statements
                  | COMENTARIO statements'''
    p[0] = p[2]

def p_statements_2(p):
    '''statements : empty'''

def p_statements_3(p):
    '''statements : expression PUNTOCOMA statements'''
    p[0] = p[3]

def p_asignacion_0(p):
    'asignacion : ID0 ASIGNACION valor PUNTOCOMA'
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if not id_en_variables:
        variables[ID] = valores.pop()
    else:
        # Aqui cambia el valor de una variable ya establecida
        # tengo que revisar si es correcto hacer x, y ,z = 1, 2, 3;
        # y si anteriormente x, y o z estaba definida. Ej: x = 2 anteriormente y ahora x va a ser 1
        valor = variables[ID]
        if isinstance(valor, valores.pop()):
            variables[ID] = valores.pop()

    nodo = Node("asignacion",[ID, variables[ID], p[2]])
    p[0] = nodo


def p_asignacion_1(p):
    'asignacion : ID0 COMA asignacion'
    ID = p[1]
    id_en_variables = variables.get(ID, False)

    if not id_en_variables:
        variables[ID] = valores.pop()
    else:
        valor = variables[ID]
        asig = valores.pop()
        if isinstance(asig, type(valor)):
            variables[ID] = asig
    p[0] = variables


def p_asignacion_2(p):
    'asignacion : ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMA'
    variables[p[1]] = []


def p_asignacion_3(p):
    'asignacion : ID0 ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMA'
    variables[p[1]] = valores
    p[0] = variables

def p_statements_4(p):
    '''statements : loop statements'''
    p[0] = p[1]

def p_asignacion_range(p):
    'asignacion : ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA'
    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if not id_en_variables:
        list = []
        for x in range(p[5]):
            list.append(p[7])
        variables[ID] = list
        p[0] = variables
    print(variables)


def p_asignacion_index(p):
    'asignacion : ID0 PARENTESISCI NUMERO PARENTESISCD ASIGNACION valor PUNTOCOMA'

    ID = p[1]
    id_en_variables = variables.get(ID, False)
    print(id_en_variables)
    if id_en_variables != False:
        valor = variables[ID]
        if isinstance(valor, list):
            if len(valor) > p[3]:
                valor[p[3]] = p[6]
                variables[ID] = valor
                p[0] = variables
            else:
                print("Error. Indice fuera de rango")
        else:
            print("Error. La variable no es indexable")
    else:
        print("Error. La variable no ha sido declarada")


def p_asignacion_index_2(p):
    'asignacion : ID0 PARENTESISCI NUMERO DOSPUNTOS NUMERO PARENTESISCD ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMA'

    ID = p[1]
    id_en_variables = variables.get(ID, False)
    if id_en_variables != False:
        valor = variables[ID]
        if isinstance(valor, list):
            if len(valor) > p[5] and p[5] > p[3]:
                if (p[5] - p[3]) == len(valores):
                    valor[p[3]:p[5]] = valores
                    variables[ID] = valor
                    p[0] = variables
                else:
                    print("Error.Debe indicar la cantidad de elementos correctos")
            else:
                print("Error. Indice fuera de rango o declaracion incorrecta de rango")
        else:
            print("Error. La variable no es indexable")
    else:
        print("Error. La variable no ha sido declarada")


def p_valor_0(p):
    '''valor : NUMERO
               | bool '''
    p[0] = p[1]
    valores.append(p[1])


def p_valor_1(p):
    '''valor : valor valor2 '''
    p[0] = [p[1] ,p[2]]


def p_valor_2(p):
    '''valor2 : COMA valor'''
    p[0] = p[2]


def p_bool(p):
    '''bool : TRUE
            | FALSE'''
    p[0] = p[1]


def p_comentario_opcional(p):
    '''comentario_opcional : COMENTARIO
                          | empty'''

def p_lista_1(p):
    ''' lista : PARENTESISCI valor PARENTESISCD'''