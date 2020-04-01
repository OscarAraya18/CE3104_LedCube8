# ------------------------------------------------------------
# Codigo Fuente: AnalizadorLexico.py
# Desarrollado por: Saymon Astúa, Oscar Araya
# Proyecto: LedCube8
# Version: Beta
#
# Descripcion: Definir las reglas para el analizador lexico
#
# TEC 2020 | CE3104 - Lenguajes, Compiladores e Interpretes
# ------------------------------------------------------------


#Se importan las librerias a utilizar
import Compilador.ply.ply.lex as lex
import re
import codecs
import os
import sys




#Se declaran los tokens a utilizar dentro del programa, en forma de una lista de strings
tokens = ['ID0',
'ID1', 
'ID2',
'NUMERO',
'BOOL',
'SUMA', 
'RESTA',
'NEGATIVO',
'MULTIPLICACION', 
'DIVISION', 
'EXPONENCIAL',
'DIVISIONE', 
'ASIGNACION', 
'COMPARACION', 
'PARENTESISD', 
'PARENTESISI', 
'MODULO',
'PUNTOCOMA', 
'COMENTARIO', 
'PARENTESISCD', 
'PARENTESISCI', 
'PUNTO', 
'COMA', 
'DOSPUNTOS',
'LLAVED',
'LLAVEI',
'MAYORQUE',
'MAYORIGUALQUE',
'MENORQUE',
'MENORIGUALQUE',
'DISTINTOQUE']


#Se declaran las keywords o palabras reservadas a utilizar dentro del programa, en forma de un diccionario
keywords = {'type' : 'TYPE',
'Timer' : 'TIMER',
'Rango_Timer' : 'RANGOTIMER',
'Dim_Columnas': 'DIMCOLUMNAS',
'Dim_Filas': 'DIMFILAS',
'Cubo' : 'CUBO',
'range' : 'RANGE',
'list': 'LIST',
'True': 'TRUE',
'False': 'FALSE',
'insert': 'INSERT',
'del': 'DEL',
'len': 'LEN',
'Neg': 'NEG',
'T': 'T',
'F': 'F',
'Blink': 'BLINK',
'Delay': 'DELAY',
'for': 'FOR',
'in': 'IN',
'If': 'IF',
'Step': 'STEP',
'shapeF': 'SHAPEF',
'shapeC': 'SHAPEC',
'shapeA': 'SHAPEA',
'Procedure': 'PROCEDURE',
'Seg': 'SEG',
'Mil': 'MIL',
'Min': 'MIN',
'CALL': 'CALL',
'Main': 'MAIN'}


#Se añade a la lista de tokens los valores (los datos en mayuscula) del diccionario de palabras reservadas
tokens = tokens + list(keywords.values())

#Se establece que se ignoran los caracteres " " y salto de tabulador
t_ignore = ' \t'



#-------------------------------- EXPRESIONES REGULARES----------------------------------------


#Se declara la estructura a reconocer para cada token
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISIONE = r'//'
t_DIVISION = r'\/'
t_DISTINTOQUE = r'<>'
t_ASIGNACION = r'='
t_COMPARACION = r'=='
t_PARENTESISD = r'\)'
t_PARENTESISI = r'\('
t_MODULO = r'%'
t_PUNTOCOMA = r';'
t_PARENTESISCD = r'\]'
t_PARENTESISCI = r'\['
t_PUNTO = r'\.'
t_COMA = r','
t_DOSPUNTOS = r':'
t_LLAVED = r'}'
t_LLAVEI = r'{'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='


#Revisa ID's invalidos de más de 10 caracteres
def t_ID1(t):
    r'[a-zA-Z0-9_@&]{10,}'
    t.type = keywords.get(t.value, 'ID1')  #Revisa palabras reservadas
    return t


#Revisa que los Id's esten correctos segun la especificacion del proyecto
def t_ID0(t):
    #Primero, una letra de la "a" a la "z"
    #Concatenado con cualquier letra, numero o simbolo indicado
    #con un maximo de 10 caracteres
    r'[a-z]([a-zA-Z0-9_@&]{0,9})'
    t.type = keywords.get(t.value, 'ID0') #Revisa palabras reservadas
    return t


#Revisa id's que comiencen con mayuscula o minuscula, cualquier cantidad de caracteres
def t_ID2(t):
    r'[a-zA-Z][a-zA-Z0-9_@&]*'
    t.type = keywords.get(t.value, 'ID2') #Revisa palabras reservadas
    return t


#Revisa comentarios que empiezen con -- y siga cualquier caracter n cantidad de veces. Se coloca pass porque la funcion
#debe retornar nada, al ser un comentario
def t_COMENTARIO(t):
    r'\--.*'
    pass


#Revisa numeros de cualquier tipo, que sean de al menos un digito
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Revisa que hayan dos ** juntos y los cataloga como exponenciales
def t_EXPONENCIAL(t):
	r'[*][*]'
	return t


#En caso de no encontrar ningun caracter valido, se considera como error
def t_error(t):
    print("Caracter ilegal '%s' " % t.value[0])
    t.lexer.skip(1)


#Cuenta la cantidad de saltos de linea dentro del lexer
def t_NUEVALINEA(t):
	r'\n+'
	t.lexer.lineno += len(t.value)



#-------------------------------------------------------------------------------------------


# Main function to analyze a received data (source code string) and returns a list with tuples, containing
# the token value and the token type for each lexeme found.
def analyzeData(data):
    # Build the lexer
    lexer = lex.lex()
    # Receive input
    lexer.input(data)
    # Create tokens list
    token_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
        token_list.append((tok.value, tok.type))
    return lexer