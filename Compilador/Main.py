from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Parser import *

def Main():
    data = ''' 
        Timer = 15;
Rango_Timer = "Mil";
Dim_Filas = 8;
Dim_Columnas = 8; 
Cubo = [
                    [   
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ], 
                    [   [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ], 
                    [   [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ], 
                    [   [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ], 
                    [   [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ], 
                    [   [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ], 
                    [   [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ], 
                    [   [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False],  
                        [False, False, False, False, False, False, False, False], 
                        [False, False, False, False, False, False, False, False] 
                    ]
            ];

Procedure Main(){
    
    ----- 1 -------

    for i in 7{
        Cubo[i].T;

    };

    Delay(500, "Mil");

    for i in 7{
        Cubo[i].F;

    };

    ------ 2 --------

    for i in 7{
        Cubo[i].T;

    };

    Delay(500, "Mil");

    for i in 7{
        Cubo[i].F;

    };

    ------ 3 --------

    for i in 7{
        Cubo[i].T;

    };

    Delay(500, "Mil");

    for i in 7{
        Cubo[i].F;

    };

    ------ 4 -------

    for i in 7{
        Cubo[i].T;

    };

    Delay(500, "Mil");

    for i in 7{
        Cubo[i].F;

    };

};
    '''

    # analyzeData(data)

    # Build the lexer
    lexer = lex.lex()
    # Receive input
    lexer.input(data)

    try:

        #analisis sintáctico
        result = parse(lexer)

        print("Exito: " + str(result))
        return
    except Exception:
        print("Error")
        return


Main()
