# ------------------------------------------------------------
# Codigo Fuente: OperacionesMatematicas.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Gramatica de las operaciones matematicas
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------

from Compilador.Lexer.AnalizadorLexico import *


variables = {}

funcList = []

parametros = []

ifList = []

forList = []

inst = []

tablaSimbolos = {}

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
        print(error_message)
        raise SyntaxError


