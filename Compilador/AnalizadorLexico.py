import ply.ply.lex as lex
import re
import codecs
import os
import sys

#Se declaran los tokens a utilizar dentro del programa, en forma de una lista de strings
tokens = ['ID', 
'NUMERO',
'BOOL',
'SUMA', 
'RESTA', 
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

#Se declaran las keywords o palabras reservadas a utilizar dentro del programa, en forma de una lista de strings
keywords = ['type',
'Timer',
'Rango_Timer',
'Dim_Columnas',
'Dim_Filas',
'Cubo',
'range',
'list',
'True',
'False',
'insert',
'del',
'len',
'Neg',
'T',
'F',
'Blink',
'Delay',
'for',
'in',
'Step',
'shapeF',
'shapeC',
'shapeA',
'Procedure',
'Seg',
'Mil',
'Min',
'CALL',
'Main']

lexema = tokens + keywords


t_ignore = '\t'


#Se declara la estructura a reconocer para cada token
t_SUMA = r'\+'
t_MENOS = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_DISTINTOQUE = r'<>'
t_ASIGNACION = r'='
t_EXPONENCIAL = r'**'
t_DIVISIONE = r'//'
t_COMPARACION = r'=='
t_PARENTESISD = r'\)'
t_PARENTESISI = r'\('
t_MODULO = r'%'
t_PUNTOCOMA = r'/;'
#t_COMENTARIO = r'--'
t_PARENTESISCD = r'/]'
t_PARENTESISCI = r'/['
t_PUNTO = r'\.'
t_COMA = r','
t_DOSPUNTOS = r':'
t_LLAVED = r'}'
t_LLAVEI = r'{'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='



def t_ID(t):

    #Primero, una letra de la "a" a la "z"
    #Concatenado
    r'[a-z][a-zA-Z0-9_@&]*{0,10}$'

    if t.value in keywords:
        t.type = t.value

    return t

def t_COMENTARIO(t):
    r'\--.*'
    pass

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Caracter ilegal '%s' " % t.value[0])
    t.lexer.skip(1)

#----------------------------------------------------------

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print(str(cont)+". "+ "pr")
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print( "Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = '/home/saymon/Documentos/Python Proyects/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)