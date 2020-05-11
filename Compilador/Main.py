from Compilador.Lexer.AnalizadorLexico import *
import Compilador.ply.ply.yacc as yacc
import Compilador.ply.ply.lex as lex
from Compilador.Sintactico.Parser import *

def Main():
    data = ''' 
    Procedure Main(){
    
    };
    
    Procedure img1 (perro, gato){
            m = [ [1,2,3], [4, 5, 6], [7, 8, 9]];
            m = True;
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
        
        Procedure img3 (){
            m = [ [1,2,3], [4, 5, 6], [7, 8, 9]];
            m = True;
            ca = [];
            for var5 in ca[1:3] {
                for var6 in ca[4:6] Step 2{
                    m[var1, var2].Neg;
                };
            };
        };
        
    Procedure img4 (){
            m = [ [1,2,3], [4, 5, 6]];
            m = True;
            ca = [];
            for var7 in ca[1:3] {
                for var8 in ca[4:6] Step 2{
                    m[var1, var2].Neg;
                };
            };
    };
        
    Procedure img5 (){
            m = [[4, 5, 6], [7, 8, 9]];
            m = True;
            ca = [];
            for var9 in ca[1:3] {
                for var10 in ca[4:6] Step 2{
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
