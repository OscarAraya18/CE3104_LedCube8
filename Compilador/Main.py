from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Parser import *

def Main():
    data = ''' 
    Procedure prueba (perro, gato){
            a.insert(2,True);
            m = [ [1,2,3], [4, 5, 6], [7, 8, 9]];
            m = True;
            ca = [];
            f = [];
            ca[2]  = True; 
            f = ca[1:3];
            };

    '''

    # analyzeData(data)

    # Build the lexer
    lexer = lex.lex()
    # Receive input
    lexer.input(data)

    try:
        result = parse(lexer)
        print("Exito: " + str(result))
        return
    except Exception:
        print("Error")
        return


Main()
