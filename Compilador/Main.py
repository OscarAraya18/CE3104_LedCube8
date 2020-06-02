from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Parser import *

def Main():
    data = ''' 
        Timer = 15;
        Rango_Timer = Seg;
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
        --Viva Saprissa
        --1ñfñgkfsgf
        4* ((2+7)/3) + 1;
        CALL img5();
        -(8);
    };
    
    Procedure img1 (perro, gato){
            m = [ [1,2,3], [4, 5, 6], [7, 8, 9]];
            m = True;
            x, y = 20, 15;
            ca = [];
            for var1 in ca[1:3] {
                m[2].T;
                for var2 in ca[4:6] Step 2{
                    m[var1, var2].Neg;
                };
            };
        };

    Procedure img2 (){
            m = [];
            m = True;
            ca = [];
            for var3 in ca[1:3] {
                for var4 in ca[4:6] Step 2{
                    m[var1, var2].Neg;
                };
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
