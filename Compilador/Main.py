from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Parser import *

def Main():
    data = ''' 
    Procedure jAAA (name,age, color){
            name = 12454;
            CALL otro();
            };
    Procedure jAAA (name,age){
            hola = 3333;
            hola = True;
            hola = False;
            };
    Procedure Main(){
            
            CALL jAAA(kevin, 19);
                
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
