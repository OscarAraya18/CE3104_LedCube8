import Compilador.ply.ply.yacc as yacc
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Sintactico.Statements import *
from Compilador.EstructurasDeDatos.TreeNode import TreeNode



tablaSimbolos = {}
parametros = []

start = 'estructura'
astRoot = TreeNode("estructura")

def p_estructura(p):
    '''estructura : rutina\
    rutina\
    main
    '''


def p_main(p):
    '''main : PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    print("Entra al main")
    tablaSimbolos[p[2]] = variables.copy()
    variables.clear()
    p[0] = p[6]


def p_rutina(p):
    '''rutina : PROCEDURE ID0 PARENTESISI parametros PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    ID = p[2]
    nombreEnTabla = tablaSimbolos.get(ID, False)
    print(nombreEnTabla)
    if nombreEnTabla != False:
        lista = tablaSimbolos[ID].copy()
        for elem in lista:
            param = elem["parametros"]
            if len(parametros) != len(param):
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
    p[0] = p[7]
    print(tablaSimbolos)

def p_parametros_1(p):
    '''parametros : ID0'''
    p[0] = p[1]
    variables[p[1]] = []
    parametros.append(p[1])

def p_parametros_2(p):
    '''parametros : ID0 COMA parametros'''
    p[0] = p[2]
    variables[p[1]] = []
    parametros.append(p[1])

#Se crea el parser
def parse(lex):
    parser = yacc.yacc()
    astTree = parser.parse(lexer=lex)
    return astTree