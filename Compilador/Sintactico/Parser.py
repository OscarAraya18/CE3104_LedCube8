import Compilador.ply.ply.yacc as yacc
from Compilador.Lexer.AnalizadorLexico import *
from Compilador.Sintactico.OperacionesMatematicas import *
from Compilador.Sintactico.Statements import *
from Compilador.EstructurasDeDatos.TreeNode import TreeNode



tablaSimbolos = {}

start = 'estructura'
astRoot = TreeNode("estructura")

def p_estructura(p):
    '''estructura : main\
    rutina\
    rutina\
    rutina\
    rutina\
    rutina '''

    ListaLlaves = ["main", "img1", "img2", "img3", "img4", "img5"]
    index = 0
    for i in range(1, 6):
        node = TreeNode(ListaLlaves[index])
        if p[i]:
            node.add_children(p[i])
        astRoot.add_child(node)
        index += 1
    p[0] = astRoot
    print("#############################################   A     S     T   ##########################################################")
    astRoot.print()



def p_main(p):
    '''main : PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMA'''
    print("Entra al main")
    tablaSimbolos[p[2]] = variables.copy()
    variables.clear()
    p[0] = p[6]


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
                print("Error. Proceso definido anteriormente")
                print("Linea: " + str(p.lineno(1)))
                raise Exception
    else:
        variables["parametros"] = parametros.copy()
        tablaSimbolos[p[2]] = [variables.copy()]
    variables.clear()
    parametros.clear()

    p[0] = inst.copy()
    inst.clear()


def p_parametros_1(p):
    '''parametros : ID0
                  | empty '''
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