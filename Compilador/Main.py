from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Parser import *

def Main():
    data = ''' Procedure Main(){
            miLista.del(2);
            m = [ [[True,True], [False,False]], [[True,True], [False,False]] ];
            miLista.insert([True, False, True], 1, 1);
            len(miLista);
            x[1:4].Neg;
            miLista[1].T;
            miLista[:3].T;
            miLista[1].F;
            miLista[1:3].F;
            miLista.shapeC
            miLista.shapeF
            miLista.shapeA
            Blink(x[1], 5, Min, True);
            Blink(x[1], True);
            Delay();
            CALL miProc();
            CALL miProc(1,2);
            Delay(3, Seg);
            If miVar == 5 {
                jaja = 2;
            };
            Procedure jAAA (){
            };
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
