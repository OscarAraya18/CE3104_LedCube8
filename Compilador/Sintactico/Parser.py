# ------------------------------------------------------------
# Codigo Fuente: Parser.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Gramatica de la estructura principal del programa
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------


import Compilador.ply.ply.yacc as yacc
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Sintactico.Statements import *
from Compilador.EstructurasDeDatos.TreeNode import TreeNode



start = 'estructura'
astRoot = TreeNode("estructura")

rutinas = []

def p_estructura(p):
    '''estructura : confiCons\
    globalVar\
    main\
    rutinas '''


    llaves = list(tablaSimbolos.keys())

    if p[3]:
        rutinas.insert(0, p[3])

    index = 0
    for i in range(0, len(llaves)):
        node = TreeNode(str(llaves[i]))
        node.add_children(rutinas[i])
        astRoot.add_child(node)
        index += 1
    p[0] = astRoot
    print("#############################################   A     S     T   ##########################################################")
    astRoot.print()
    print(tablaSimbolos)
    print("Variables globales: " + str(variablesGlobales))
    print("Constantes de configuración: " + str(consConfi))



def p_main(p):
    '''main : PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    print("Entra al main")
    tablaSimbolos[p[2]] = variables.copy()
    variables.clear()
    p[0] = inst.copy() + funcList.copy()
    funcList.clear()
    inst.clear()


def p_rutinas_1(p):
    '''rutinas : rutina rutinas '''
    if p[1]:
        rutinas.insert(0, p[1])
    p[0] = p[2]

def p_rutinas_2(p):
    '''rutinas : empty'''
    p[0] = p[1]

def p_rutina(p):
    '''rutina : PROCEDURE ID0 PARENTESISI parametros PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    forList.clear()
    funcList.clear()
    ID = p[2]
    nombreEnTabla = tablaSimbolos.get(ID, False)
    if nombreEnTabla != False:
        lista = tablaSimbolos[ID].copy()
        for elem in lista:
            param = elem["parametros"]
            if len(parametros) != len(param):
                variables["parametros"] = parametros.copy()
                tablaSimbolos[p[2]] += [variables.copy()]
            else:
                if param[0] == None and parametros[0] != None:
                    variables["parametros"] = parametros.copy()
                    tablaSimbolos[p[2]] += [variables.copy()]
                else:
                    print("Error. Proceso definido anteriormente")
                    print("Linea: " + str(p.lineno(1)))
                    raise Exception
    else:
        variables["parametros"] = parametros.copy()
        tablaSimbolos[p[2]] = [variables.copy()]
    variables.clear()
    parametros.clear()
    p[0] = inst.copy() + funcList.copy()
    funcList.clear()
    inst.clear()


def p_parametros_1(p):
    '''parametros : ID0
                  | empty '''
    if p[1]:
        variables[p[1]] = []
    p[0] = p[1]
    parametros.append(p[1])

def p_parametros_2(p):
    '''parametros : ID0 COMA parametros'''
    p[0] = p[2]
    variables[p[1]] = []
    parametros.append(p[1])

def p_globalVar(p):
    'as : ID0 ASIGNACION valor PUNTOCOMA'
    ID = p[1]
    id_en_variables = variablesGlobales.get(ID, False)
    if not id_en_variables:
        if len(valores) > 0:
            variablesGlobales[ID] = [valores.pop()]
        else:
            variablesGlobales[ID] = [valores2.pop()]

def p_globalVar_2(p):
    '''globalVar : as globalVar
                 | empty'''

def p_confiCons(p):
    '''confiCons : timer\
    rangoTimer\
    dimFilas\
    dimCol\
    cubo'''

def p_timer(p):
    '''timer : TIMER ASIGNACION NUMERO PUNTOCOMA'''
    consConfi[p[1]] = p[3]

def p_rango_timer(p):
    '''rangoTimer : RANGOTIMER ASIGNACION rango PUNTOCOMA'''
    consConfi[p[1]] = p[3]

def p_dimFilas(p):
    '''dimFilas : DIMFILAS ASIGNACION NUMERO PUNTOCOMA'''
    consConfi[p[1]] = p[3]

def p_dimCol(p):
    '''dimCol : DIMCOLUMNAS ASIGNACION NUMERO PUNTOCOMA'''
    consConfi[p[1]] = p[3]

def p_cubo(p):
    '''cubo : empty'''


#Se crea el parser
def parse(lex):
    parser = yacc.yacc()
    astTree = parser.parse(lexer=lex)
    return astTree