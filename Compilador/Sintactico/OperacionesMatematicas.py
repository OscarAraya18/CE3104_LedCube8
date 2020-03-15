from Compilador.ply.ply import yacc
from Compilador.Lexer.AnalizadorLexico import *

funcList = []
variables = {}
precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'DIVISIONE'),
    ('right', 'NEGATIVO'),
    ('left', 'PARENTESISI', 'PARENTESISD'),
)


# Basic operations
def p_expression_suma(p):
    'expression : expression SUMA term'
    p[0] = p[1] + p[3]


def p_expression_resta(p):
    'expression : expression RESTA term'
    p[0] = p[1] - p[3]


def p_term_multiplicacion(p):
    'term : term MULTIPLICACION factor'
    p[0] = p[1] * p[3]


def p_term_division(p):
    'term : term DIVISION factor'
    p[0] = p[1] / p[3]

def p_term_divisione(p):
    'term : term DIVISIONE factor'
    p[0] = p[1] // p[3]

def p_term_modulo(p):
    'term : term MODULO factor'
    p[0] = p[1] % p[3]

def p_term_exponencial(p):
    'term : term EXPONENCIAL factor'
    p[0] = p[1] ** p[3]

def p_expression_negativo(p):
    'expression : RESTA term %prec NEGATIVO'
    p[0] = -p[2]


# Basic atomic expressions

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]

'''
def p_factor_ID(p):
    'factor : ID0'
    try:
        if isinstance(variables[p[1]][-1], int):
            p[0] = variables[p[1]][-1]
        else:
            print("'" + p[1] + "'", "must be integer")
    except KeyError:
        print("Syntactic Error: Variable %s has not been declared." % p[1])
        p[0] = 0


def p_factor_array(p):
    'factor : ID0 PARENTESISCI NUMERO PARENTESISCD'
    if variables[p[1]]:
        arrayList = variables[p[1]][1]
        if p[3] < len(arrayList):
            value = arrayList[p[3]]
            p[0] = value
        else:
            print("Index out of range")
    else:
        print("Syntactic Error: Variable %s has not been declared." % p[1])
        
    '''

def p_factor_expr(p):
    'factor : PARENTESISI expression PARENTESISD'
    p[0] = p[2]


def p_empty(p):
    "empty :"
    pass


# Error rule for syntax errors
def p_error(p):
    if p:
        error_message = "Syntax error in line: " + str(p.lineno)
        #file = open(globals.projectFolderPath + "/src/tmp/error_log.txt", "w")
        #file.write(error_message)
        #file.close()
        print(error_message)
        raise SyntaxError

    # Build the parser


parser = yacc.yacc()

data = "3 + 5"

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)