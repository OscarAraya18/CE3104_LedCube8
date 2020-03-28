from Compilador.EstructurasDeDatos.TreeNode import TreeNode


def p_funcionReservada_1(p):
    '''funcionReservada : BLINK'''


def p_insert(p):
    '''funcionReservada : ID0 PUNTO INSERT PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[3], p[1], p[5], p[7]])
    p[0] = nodo
    print("Entra al insert")


def p_del(p):
    '''funcionReservada : ID0 PUNTO DEL PARENTESISI NUMERO PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[3], p[1], p[5]])
    p[0] = nodo
    print("Entra al del")


def p_len(p):
    '''funcionReservada :  LEN PARENTESISI ID0 PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[1], p[3]])
    p[0] = nodo
    print("Entra al len")


def p_neg(p):
    '''funcionReservada : ID0 PARENTESISCI NUMERO PARENTESISCD PUNTO NEG PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[6], p[1], p[3]])
    p[0] = nodo
    print("Entra al neg")


def p_neg_2(p):
    '''funcionReservada : ID0 PARENTESISCI NUMERO DOSPUNTOS NUMERO PARENTESISCD PUNTO NEG PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[8], p[1], p[3], p[4], p[5]])
    p[0] = nodo
    print("Entra al neg")


def p_neg_3(p):
    '''funcionReservada : ID0 PARENTESISCI  DOSPUNTOS NUMERO PARENTESISCD PUNTO NEG PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[7], p[1], p[3], p[4]])
    p[0] = nodo
    print("Entra al neg")


def p_t(p):
    '''funcionReservada : ID0 PARENTESISCI NUMERO PARENTESISCD PUNTO T PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[6], p[1], p[3]])
    p[0] = nodo
    print("Entra al T")


def p_t_2(p):
    '''funcionReservada : ID0 PARENTESISCI NUMERO DOSPUNTOS NUMERO PARENTESISCD PUNTO T PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[8], p[1], p[3], p[4], p[5]])
    p[0] = nodo
    print("Entra al T")


def p_t_3(p):
    '''funcionReservada : ID0 PARENTESISCI  DOSPUNTOS NUMERO PARENTESISCD PUNTO T PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[7], p[1], p[3], p[4]])
    p[0] = nodo
    print("Entra al T")


def p_f(p):
    '''funcionReservada : ID0 PARENTESISCI NUMERO PARENTESISCD PUNTO F PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[6], p[1], p[3]])
    p[0] = nodo
    print("Entra al F")


def p_f_2(p):
    '''funcionReservada : ID0 PARENTESISCI NUMERO DOSPUNTOS NUMERO PARENTESISCD PUNTO F PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[8], p[1], p[3], p[4], p[5]])
    p[0] = nodo
    print("Entra al F")


def p_f_3(p):
    '''funcionReservada : ID0 PARENTESISCI  DOSPUNTOS NUMERO PARENTESISCD PUNTO F PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[7], p[1], p[3], p[4]])
    p[0] = nodo
    print("Entra al F")


def p_blink_1(p):
    '''funcionReservada : BLINK PARENTESISI ID0 PARENTESISCI NUMERO PARENTESISCD COMA NUMERO COMA rango COMA bool PARENTESISD PUNTOCOMA '''
    nodo = TreeNode("funcion")
    nodo.add_children([p[1], p[3], p[5], p[8], p[10], p[12]])
    p[0] = nodo
    print("Entra a blink")


def p_blink_2(p):
    '''funcionReservada : BLINK PARENTESISI ID0 PARENTESISCI NUMERO PARENTESISCD COMA bool PARENTESISD PUNTOCOMA'''
    nodo = TreeNode("funcion")
    nodo.add_children([p[1], p[3], p[5], p[8]])
    p[0] = nodo
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


def p_rango(p):
    '''rango : SEG
             | MIN
             | MIL'''

    p[0] = p[1]
