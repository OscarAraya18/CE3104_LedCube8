
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'estructuraleftSUMARESTAleftMULTIPLICACIONDIVISIONDIVISIONErightNEGATIVOleftPARENTESISIPARENTESISDASIGNACION BLINK BOOL CALL COMA COMENTARIO COMPARACION CUBO DEL DELAY DIMCOLUMNAS DIMFILAS DISTINTOQUE DIVISION DIVISIONE DOSPUNTOS EXPONENCIAL F FALSE FOR ID0 ID1 ID2 IF IN INSERT LEN LIST LLAVED LLAVEI MAIN MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MIL MIN MODULO MULTIPLICACION NEG NEGATIVO NUMERO PARENTESISCD PARENTESISCI PARENTESISD PARENTESISI PROCEDURE PUNTO PUNTOCOMA RANGE RANGOTIMER RESTA SEG SHAPEA SHAPEC SHAPEF STEP SUMA T TIMER TRUE TYPEloop : FOR ID0 IN iterable STEP NUMERO LLAVEI statements LLAVED PUNTOCOMAfuncionReservada : ID0 PUNTO INSERT PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMAstatements : COMENTARIO statementsestructura : confiCons    globalVar    main    rutinas statements : emptystatements : expression PUNTOCOMA statementsloop : FOR ID0 IN iterable LLAVEI statements LLAVED PUNTOCOMAfuncionReservada : ID0 PUNTO INSERT PARENTESISI valor COMA tipo COMA NUMERO PARENTESISD PUNTOCOMAstatements : loop statements\n                  | asignacion statementsexpression : expression SUMA termexpression : expression RESTA termstatements : funcionReservada statementsfuncionReservada : ID0 PUNTO INSERT PARENTESISI valor COMA NUMERO PARENTESISD PUNTOCOMA iterable : NUMEROmain : PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMAterm : term MULTIPLICACION factorstatements : bifurcacion statementsiterable : ID0 conjuntoterm : term DIVISION factorstatements : rutina statementsterm : term DIVISIONE factorrutinas : rutina rutinas asignacion : ID0 ASIGNACION valor PUNTOCOMAfuncionReservada : ID0 PUNTO DEL PARENTESISI NUMERO PARENTESISD PUNTOCOMAterm : term MODULO factorrutinas : emptyterm : term EXPONENCIAL factorfuncionReservada : ID0 PUNTO DEL PARENTESISI NUMERO COMA tipo PARENTESISD PUNTOCOMAexpression : RESTA term %prec NEGATIVOrutina : PROCEDURE ID0 PARENTESISI parametros PARENTESISD LLAVEI statements LLAVED PUNTOCOMAexpression : termfuncionReservada :  LEN PARENTESISI ID0 PARENTESISD PUNTOCOMAasignacion : ID0 COMA asignacionterm : factorfuncionReservada : ID0 conjunto PUNTO NEG PUNTOCOMAfactor : NUMEROfactor : PARENTESISI expression PARENTESISDasignacion : ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMAempty :funcionReservada : ID0 conjunto PUNTO T PUNTOCOMAparametros : ID0\n                  | empty asignacion : ID0 ASIGNACION funcionReservada PUNTOCOMAparametros : ID0 COMA parametrosasignacion : ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMAas : ID0 ASIGNACION valor PUNTOCOMAfuncionReservada : ID0 conjunto PUNTO F PUNTOCOMAasignacion : ID0 conjunto ASIGNACION valor PUNTOCOMAglobalVar : as globalVar\n                 | emptyconfiCons : timer    rangoTimer    dimFilas    dimCol    cubofuncionReservada : BLINK PARENTESISI ID0 conjunto COMA NUMERO COMA rango COMA bool PARENTESISD PUNTOCOMA timer : TIMER ASIGNACION NUMERO PUNTOCOMAasignacion : ID0 conjunto ASIGNACION valor_b PUNTOCOMArangoTimer : RANGOTIMER ASIGNACION rango PUNTOCOMAdimFilas : DIMFILAS ASIGNACION NUMERO PUNTOCOMAfuncionReservada : BLINK PARENTESISI ID0 conjunto COMA bool PARENTESISD PUNTOCOMAdimCol : DIMCOLUMNAS ASIGNACION NUMERO PUNTOCOMAcubo : CUBO ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMAasignacion : ID0 ASIGNACION valor_b PUNTOCOMAfuncionReservada : DELAY PARENTESISI PARENTESISD PUNTOCOMAfuncionReservada : DELAY PARENTESISI NUMERO COMA rango PARENTESISD PUNTOCOMAbifurcacion : IF ID0 conjunto operador valor_b LLAVEI statements LLAVED PUNTOCOMAfuncionReservada : ID0 PUNTO SHAPEFfuncionReservada : ID0 PUNTO SHAPECoperador : COMPARACION\n                | DISTINTOQUE\n                | MENORQUE\n                | MAYORQUE\n                | MAYORIGUALQUE\n                | MENORIGUALQUE valor : NUMERO\n             | bool funcionReservada : ID0 PUNTO SHAPEAvalor : valor valor2 valor2 : COMA valorvalor : listafuncionReservada : CALL ID0 PARENTESISI parametrosFuncion PARENTESISD PUNTOCOMAvalor_b : ID0 conjuntorango : SEG\n             | MIN\n             | MILtipo : NUMERO valor_b : NUMERO\n               | bool\n               | expressionbool : TRUE\n            | FALSEconjunto : PARENTESISCI indice DOSPUNTOS indice PARENTESISCDcomentario_opcional : COMENTARIO\n                           | emptyconjunto : PARENTESISCI DOSPUNTOS indice PARENTESISCDlista : PARENTESISCI valor PARENTESISCDconjunto : PARENTESISCI indice PARENTESISCDconjunto : PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD conjunto : emptyrango_matriz : PARENTESISCI indice PARENTESISCDconjunto : PARENTESISCI indice COMA indice PARENTESISCDconjunto : PARENTESISCI DOSPUNTOS COMA indice PARENTESISCDconjunto : PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCDparametrosFuncion : ID0\n                         | NUMERO\n                         | emptyparametrosFuncion : ID0 COMA parametrosFuncionparametrosFuncion : NUMERO COMA parametrosFuncionindice : NUMERO\n              | ID0'
    
_lr_action_items = {'TIMER':([0,],[4,]),'$end':([1,12,20,21,22,40,123,201,],[0,-40,-4,-40,-27,-23,-16,-31,]),'ID0':([2,6,23,43,47,52,62,65,69,72,73,74,75,76,79,85,86,90,94,109,110,111,115,116,132,143,145,148,152,153,154,159,161,167,169,171,173,175,177,188,194,195,196,197,198,199,200,201,204,205,208,213,214,215,216,217,221,224,226,245,247,248,255,260,263,265,271,274,276,278,279,281,282,286,288,],[8,8,41,-47,-52,59,80,59,80,80,80,80,80,80,108,118,119,80,80,133,142,147,155,156,163,-34,147,178,-65,-66,-75,190,-60,-24,-44,-61,147,147,147,-62,178,-67,-68,-69,-70,-71,-72,-31,80,-39,147,-49,-55,-36,-41,-48,-33,190,190,-79,80,80,-25,-63,-7,147,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'PROCEDURE':([2,5,6,7,12,14,21,43,47,62,69,72,73,74,75,76,90,94,123,143,152,153,154,161,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[-40,13,-40,-51,23,-50,23,-47,-52,23,23,23,23,23,23,23,23,23,-16,-34,-65,-66,-75,-60,-24,-44,-61,-62,-31,23,-39,-49,-55,-36,-41,-48,-33,-79,23,23,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'RANGOTIMER':([3,39,],[10,-54,]),'ASIGNACION':([4,8,10,17,33,48,80,112,114,142,172,174,210,233,235,236,251,283,],[11,15,18,34,49,56,109,148,-97,109,148,-95,-93,-90,-99,-100,-96,-101,]),'DIMFILAS':([9,51,],[17,-56,]),'NUMERO':([11,15,31,34,45,49,62,63,67,69,72,73,74,75,76,78,90,94,95,96,102,103,104,105,106,109,111,117,132,135,143,145,148,152,153,154,159,167,169,170,171,173,175,177,184,185,188,194,195,196,197,198,199,200,201,203,204,205,208,213,214,215,216,217,221,222,224,226,238,240,245,247,248,255,260,263,265,267,271,274,276,278,279,281,282,286,288,],[19,26,26,50,26,57,81,26,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,138,146,158,165,26,-34,146,138,-65,-66,-75,192,-24,-44,206,-61,146,146,146,218,220,-62,228,-67,-68,-69,-70,-71,-72,-31,230,81,-39,146,-49,-55,-36,-41,-48,-33,241,192,192,254,256,-79,81,81,-25,-63,-7,146,277,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'MAIN':([13,],[24,]),'TRUE':([15,31,45,63,109,135,148,184,194,195,196,197,198,199,200,222,232,237,238,280,],[29,29,29,29,29,29,29,29,29,-67,-68,-69,-70,-71,-72,29,29,29,29,29,]),'FALSE':([15,31,45,63,109,135,148,184,194,195,196,197,198,199,200,222,232,237,238,280,],[30,30,30,30,30,30,30,30,30,-67,-68,-69,-70,-71,-72,30,30,30,30,30,]),'PARENTESISCI':([15,31,45,56,63,80,109,119,133,135,142,148,156,163,174,178,184,238,251,],[31,31,31,63,31,111,135,111,111,31,111,31,111,111,208,111,31,31,265,]),'DIMCOLUMNAS':([16,58,],[33,-57,]),'SEG':([18,189,258,],[36,36,36,]),'MIN':([18,189,258,],[37,37,37,]),'MIL':([18,189,258,],[38,38,38,]),'PUNTOCOMA':([19,25,26,27,28,29,30,35,36,37,38,44,50,54,55,57,71,77,81,87,92,107,114,120,122,125,126,127,128,129,130,131,133,134,136,138,139,140,141,152,153,154,157,162,166,168,174,178,179,180,181,182,183,186,188,210,212,215,216,217,221,225,233,235,236,239,243,245,249,251,255,259,260,264,266,268,269,271,272,273,276,278,279,283,284,286,287,288,],[39,43,-73,-74,-78,-88,-89,51,-81,-82,-83,-76,58,-77,-94,64,94,-32,-37,-35,123,-30,-97,161,-38,-11,-12,-17,-20,-22,-26,-28,-40,167,169,-37,-74,171,-87,-65,-66,-75,188,201,-80,205,-95,-40,213,214,215,216,217,221,-62,-93,-80,-36,-41,-48,-33,245,-90,-99,-100,255,260,-79,263,-96,-25,271,-63,274,276,278,279,-58,281,282,-2,-14,-29,-101,286,-8,288,-53,]),'PARENTESISI':([24,41,62,67,69,72,73,74,75,76,78,82,83,84,90,94,95,96,102,103,104,105,106,109,118,137,143,148,150,151,152,153,154,167,169,171,188,194,195,196,197,198,199,200,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[42,52,67,67,67,67,67,67,67,67,67,115,116,117,67,67,67,67,67,67,67,67,67,67,159,170,-34,67,184,185,-65,-66,-75,-24,-44,-61,-62,67,-67,-68,-69,-70,-71,-72,-31,67,-39,-49,-55,-36,-41,-48,-33,-79,67,67,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'COMA':([25,26,27,28,29,30,36,37,38,44,46,54,55,59,80,88,114,134,138,139,142,144,145,146,147,156,158,174,179,187,190,192,206,210,218,219,220,233,235,236,241,251,253,254,270,283,],[45,-73,-74,-78,-88,-89,-81,-82,-83,-76,45,45,-94,65,110,45,-97,45,-73,-74,110,175,177,-107,-108,-40,189,-95,45,222,224,226,232,-93,237,238,240,-90,-99,-100,258,-96,267,-73,280,-101,]),'PARENTESISCD':([26,27,28,29,30,44,46,54,55,88,135,144,146,147,176,207,209,211,234,275,],[-73,-74,-78,-88,-89,-76,55,-77,-94,120,168,174,-107,-108,210,233,235,236,251,283,]),'LLAVEI':([29,30,53,66,77,81,87,107,114,122,125,126,127,128,129,130,131,141,163,164,165,174,178,202,210,212,227,228,229,230,233,235,236,251,283,],[-88,-89,62,90,-32,-37,-35,-30,-97,-38,-11,-12,-17,-20,-22,-26,-28,-87,-40,204,-15,-95,-40,-19,-93,-80,247,-37,-86,248,-90,-99,-100,-96,-101,]),'PARENTESISD':([29,30,36,37,38,42,52,59,60,61,65,77,81,87,89,91,107,117,122,125,126,127,128,129,130,131,155,159,190,191,192,193,220,223,224,226,242,244,246,250,252,254,256,257,277,285,],[-88,-89,-81,-82,-83,53,-40,-42,66,-43,-40,-32,-37,-35,-45,122,-30,157,-38,-11,-12,-17,-20,-22,-26,-28,186,-40,-102,225,-103,-104,239,243,-40,-40,259,-105,-106,264,266,268,-84,269,284,287,]),'CUBO':([32,64,],[48,-59,]),'COMENTARIO':([62,69,72,73,74,75,76,90,94,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[69,69,69,69,69,69,69,69,69,-34,-65,-66,-75,-24,-44,-61,-62,-31,69,-39,-49,-55,-36,-41,-48,-33,-79,69,69,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'LLAVED':([62,68,69,70,72,73,74,75,76,90,93,94,97,98,99,100,101,121,124,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,231,245,247,248,255,260,261,262,263,271,274,276,278,279,281,282,286,288,],[-40,92,-40,-5,-40,-40,-40,-40,-40,-40,-3,-40,-9,-10,-13,-18,-21,162,-6,-34,-65,-66,-75,-24,-44,-61,-62,-31,-40,-39,-49,-55,-36,-41,-48,-33,249,-79,-40,-40,-25,-63,272,273,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'RESTA':([62,67,69,71,72,73,74,75,76,77,81,87,90,91,94,107,109,122,125,126,127,128,129,130,131,138,141,143,148,152,153,154,167,169,171,188,194,195,196,197,198,199,200,201,204,205,213,214,215,216,217,221,228,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[78,78,78,96,78,78,78,78,78,-32,-37,-35,78,96,78,-30,78,-38,-11,-12,-17,-20,-22,-26,-28,-37,96,-34,78,-65,-66,-75,-24,-44,-61,-62,78,-67,-68,-69,-70,-71,-72,-31,78,-39,-49,-55,-36,-41,-48,-33,-37,-79,78,78,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'FOR':([62,69,72,73,74,75,76,90,94,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[79,79,79,79,79,79,79,79,79,-34,-65,-66,-75,-24,-44,-61,-62,-31,79,-39,-49,-55,-36,-41,-48,-33,-79,79,79,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'LEN':([62,69,72,73,74,75,76,90,94,109,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[82,82,82,82,82,82,82,82,82,82,-34,-65,-66,-75,-24,-44,-61,-62,-31,82,-39,-49,-55,-36,-41,-48,-33,-79,82,82,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'BLINK':([62,69,72,73,74,75,76,90,94,109,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[83,83,83,83,83,83,83,83,83,83,-34,-65,-66,-75,-24,-44,-61,-62,-31,83,-39,-49,-55,-36,-41,-48,-33,-79,83,83,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'DELAY':([62,69,72,73,74,75,76,90,94,109,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[84,84,84,84,84,84,84,84,84,84,-34,-65,-66,-75,-24,-44,-61,-62,-31,84,-39,-49,-55,-36,-41,-48,-33,-79,84,84,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'CALL':([62,69,72,73,74,75,76,90,94,109,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[85,85,85,85,85,85,85,85,85,85,-34,-65,-66,-75,-24,-44,-61,-62,-31,85,-39,-49,-55,-36,-41,-48,-33,-79,85,85,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'IF':([62,69,72,73,74,75,76,90,94,143,152,153,154,167,169,171,188,201,204,205,213,214,215,216,217,221,245,247,248,255,260,263,271,274,276,278,279,281,282,286,288,],[86,86,86,86,86,86,86,86,86,-34,-65,-66,-75,-24,-44,-61,-62,-31,86,-39,-49,-55,-36,-41,-48,-33,-79,86,86,-25,-63,-7,-58,-46,-2,-14,-29,-64,-1,-8,-53,]),'SUMA':([71,77,81,87,91,107,122,125,126,127,128,129,130,131,138,141,228,],[95,-32,-37,-35,95,-30,-38,-11,-12,-17,-20,-22,-26,-28,-37,95,-37,]),'MULTIPLICACION':([77,81,87,107,122,125,126,127,128,129,130,131,138,228,],[102,-37,-35,102,-38,102,102,-17,-20,-22,-26,-28,-37,-37,]),'DIVISION':([77,81,87,107,122,125,126,127,128,129,130,131,138,228,],[103,-37,-35,103,-38,103,103,-17,-20,-22,-26,-28,-37,-37,]),'DIVISIONE':([77,81,87,107,122,125,126,127,128,129,130,131,138,228,],[104,-37,-35,104,-38,104,104,-17,-20,-22,-26,-28,-37,-37,]),'MODULO':([77,81,87,107,122,125,126,127,128,129,130,131,138,228,],[105,-37,-35,105,-38,105,105,-17,-20,-22,-26,-28,-37,-37,]),'EXPONENCIAL':([77,81,87,107,122,125,126,127,128,129,130,131,138,228,],[106,-37,-35,106,-38,106,106,-17,-20,-22,-26,-28,-37,-37,]),'PUNTO':([80,112,114,133,166,174,210,233,235,236,251,283,],[113,149,-97,113,149,-95,-93,-90,-99,-100,-96,-101,]),'IN':([108,],[132,]),'RANGE':([109,],[137,]),'DOSPUNTOS':([111,144,146,147,],[145,173,-107,-108,]),'INSERT':([113,],[150,]),'DEL':([113,],[151,]),'SHAPEF':([113,],[152,]),'SHAPEC':([113,],[153,]),'SHAPEA':([113,],[154,]),'COMPARACION':([114,119,160,174,210,233,235,236,251,283,],[-97,-40,195,-95,-93,-90,-99,-100,-96,-101,]),'DISTINTOQUE':([114,119,160,174,210,233,235,236,251,283,],[-97,-40,196,-95,-93,-90,-99,-100,-96,-101,]),'MENORQUE':([114,119,160,174,210,233,235,236,251,283,],[-97,-40,197,-95,-93,-90,-99,-100,-96,-101,]),'MAYORQUE':([114,119,160,174,210,233,235,236,251,283,],[-97,-40,198,-95,-93,-90,-99,-100,-96,-101,]),'MAYORIGUALQUE':([114,119,160,174,210,233,235,236,251,283,],[-97,-40,199,-95,-93,-90,-99,-100,-96,-101,]),'MENORIGUALQUE':([114,119,160,174,210,233,235,236,251,283,],[-97,-40,200,-95,-93,-90,-99,-100,-96,-101,]),'STEP':([114,163,164,165,174,202,210,233,235,236,251,283,],[-97,-40,203,-15,-95,-19,-93,-90,-99,-100,-96,-101,]),'NEG':([149,],[181,]),'T':([149,],[182,]),'F':([149,],[183,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'estructura':([0,],[1,]),'confiCons':([0,],[2,]),'timer':([0,],[3,]),'globalVar':([2,6,],[5,14,]),'as':([2,6,],[6,6,]),'empty':([2,6,12,21,52,62,65,69,72,73,74,75,76,80,90,94,119,133,142,156,159,163,178,204,224,226,247,248,],[7,7,22,22,61,70,61,70,70,70,70,70,70,114,70,70,114,114,114,114,193,114,114,70,193,193,70,70,]),'rangoTimer':([3,],[9,]),'main':([5,],[12,]),'dimFilas':([9,],[16,]),'rutinas':([12,21,],[20,40,]),'rutina':([12,21,62,69,72,73,74,75,76,90,94,204,247,248,],[21,21,76,76,76,76,76,76,76,76,76,76,76,76,]),'valor':([15,31,45,63,109,135,148,184,238,],[25,46,54,88,134,46,179,219,54,]),'bool':([15,31,45,63,109,135,148,184,194,222,232,237,238,280,],[27,27,27,27,139,27,139,27,229,242,250,252,27,285,]),'lista':([15,31,45,63,109,135,148,184,238,],[28,28,28,28,28,28,28,28,28,]),'dimCol':([16,],[32,]),'rango':([18,189,258,],[35,223,270,]),'valor2':([25,46,54,88,134,179,219,],[44,44,44,44,44,44,44,]),'cubo':([32,],[47,]),'parametros':([52,65,],[60,89,]),'statements':([62,69,72,73,74,75,76,90,94,204,247,248,],[68,93,97,98,99,100,101,121,124,231,261,262,]),'expression':([62,67,69,72,73,74,75,76,90,94,109,148,194,204,247,248,],[71,91,71,71,71,71,71,71,71,71,141,141,141,71,71,71,]),'loop':([62,69,72,73,74,75,76,90,94,204,247,248,],[72,72,72,72,72,72,72,72,72,72,72,72,]),'asignacion':([62,69,72,73,74,75,76,90,94,110,204,247,248,],[73,73,73,73,73,73,73,73,73,143,73,73,73,]),'funcionReservada':([62,69,72,73,74,75,76,90,94,109,204,247,248,],[74,74,74,74,74,74,74,74,74,136,74,74,74,]),'bifurcacion':([62,69,72,73,74,75,76,90,94,204,247,248,],[75,75,75,75,75,75,75,75,75,75,75,75,]),'term':([62,67,69,72,73,74,75,76,78,90,94,95,96,109,148,194,204,247,248,],[77,77,77,77,77,77,77,77,107,77,77,125,126,77,77,77,77,77,77,]),'factor':([62,67,69,72,73,74,75,76,78,90,94,95,96,102,103,104,105,106,109,148,194,204,247,248,],[87,87,87,87,87,87,87,87,87,87,87,87,87,127,128,129,130,131,87,87,87,87,87,87,]),'conjunto':([80,119,133,142,156,163,178,],[112,160,166,172,187,202,212,]),'valor_b':([109,148,194,],[140,180,227,]),'indice':([111,145,173,175,177,208,265,],[144,176,207,209,211,234,275,]),'iterable':([132,],[164,]),'parametrosFuncion':([159,224,226,],[191,244,246,]),'operador':([160,],[194,]),'tipo':([238,240,],[253,257,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> estructura","S'",1,None,None,None),
  ('loop -> FOR ID0 IN iterable STEP NUMERO LLAVEI statements LLAVED PUNTOCOMA','loop',10,'p_loop_for','Ciclos.py',17),
  ('funcionReservada -> ID0 PUNTO INSERT PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA','funcionReservada',9,'p_insert','FuncionesReservadas.py',19),
  ('statements -> COMENTARIO statements','statements',2,'p_statements_1','Statements.py',23),
  ('estructura -> confiCons globalVar main rutinas','estructura',4,'p_estructura','Parser.py',25),
  ('statements -> empty','statements',1,'p_statements_2','Statements.py',28),
  ('statements -> expression PUNTOCOMA statements','statements',3,'p_statements_3','Statements.py',32),
  ('loop -> FOR ID0 IN iterable LLAVEI statements LLAVED PUNTOCOMA','loop',8,'p_loop_for_2','Ciclos.py',34),
  ('funcionReservada -> ID0 PUNTO INSERT PARENTESISI valor COMA tipo COMA NUMERO PARENTESISD PUNTOCOMA','funcionReservada',11,'p_insert_2','FuncionesReservadas.py',35),
  ('statements -> loop statements','statements',2,'p_statements_4','Statements.py',38),
  ('statements -> asignacion statements','statements',2,'p_statements_4','Statements.py',39),
  ('expression -> expression SUMA term','expression',3,'p_expression_suma','OperacionesMatematicas.py',42),
  ('expression -> expression RESTA term','expression',3,'p_expression_resta','OperacionesMatematicas.py',47),
  ('statements -> funcionReservada statements','statements',2,'p_statements_5','Statements.py',47),
  ('funcionReservada -> ID0 PUNTO INSERT PARENTESISI valor COMA NUMERO PARENTESISD PUNTOCOMA','funcionReservada',9,'p_insert_3','FuncionesReservadas.py',50),
  ('iterable -> NUMERO','iterable',1,'p_iterable_1','Ciclos.py',51),
  ('main -> PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMA','main',8,'p_main','Parser.py',51),
  ('term -> term MULTIPLICACION factor','term',3,'p_term_multiplicacion','OperacionesMatematicas.py',52),
  ('statements -> bifurcacion statements','statements',2,'p_statements_6','Statements.py',53),
  ('iterable -> ID0 conjunto','iterable',2,'p_iterable_2','Ciclos.py',56),
  ('term -> term DIVISION factor','term',3,'p_term_division','OperacionesMatematicas.py',57),
  ('statements -> rutina statements','statements',2,'p_statements_7','Statements.py',58),
  ('term -> term DIVISIONE factor','term',3,'p_term_divisione','OperacionesMatematicas.py',61),
  ('rutinas -> rutina rutinas','rutinas',2,'p_rutinas_1','Parser.py',61),
  ('asignacion -> ID0 ASIGNACION valor PUNTOCOMA','asignacion',4,'p_asignacion_0','Statements.py',63),
  ('funcionReservada -> ID0 PUNTO DEL PARENTESISI NUMERO PARENTESISD PUNTOCOMA','funcionReservada',7,'p_del','FuncionesReservadas.py',65),
  ('term -> term MODULO factor','term',3,'p_term_modulo','OperacionesMatematicas.py',65),
  ('rutinas -> empty','rutinas',1,'p_rutinas_2','Parser.py',68),
  ('term -> term EXPONENCIAL factor','term',3,'p_term_exponencial','OperacionesMatematicas.py',69),
  ('funcionReservada -> ID0 PUNTO DEL PARENTESISI NUMERO COMA tipo PARENTESISD PUNTOCOMA','funcionReservada',9,'p_del_2','FuncionesReservadas.py',73),
  ('expression -> RESTA term','expression',2,'p_expression_negativo','OperacionesMatematicas.py',73),
  ('rutina -> PROCEDURE ID0 PARENTESISI parametros PARENTESISD LLAVEI statements LLAVED PUNTOCOMA','rutina',9,'p_rutina','Parser.py',73),
  ('expression -> term','expression',1,'p_expression_term','OperacionesMatematicas.py',80),
  ('funcionReservada -> LEN PARENTESISI ID0 PARENTESISD PUNTOCOMA','funcionReservada',5,'p_len','FuncionesReservadas.py',81),
  ('asignacion -> ID0 COMA asignacion','asignacion',3,'p_asignacion_1','Statements.py',82),
  ('term -> factor','term',1,'p_term_factor','OperacionesMatematicas.py',85),
  ('funcionReservada -> ID0 conjunto PUNTO NEG PUNTOCOMA','funcionReservada',5,'p_neg','FuncionesReservadas.py',89),
  ('factor -> NUMERO','factor',1,'p_factor_num','OperacionesMatematicas.py',90),
  ('factor -> PARENTESISI expression PARENTESISD','factor',3,'p_factor_expr','OperacionesMatematicas.py',95),
  ('asignacion -> ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMA','asignacion',5,'p_asignacion_2','Statements.py',98),
  ('empty -> <empty>','empty',0,'p_empty','OperacionesMatematicas.py',100),
  ('funcionReservada -> ID0 conjunto PUNTO T PUNTOCOMA','funcionReservada',5,'p_t','FuncionesReservadas.py',107),
  ('parametros -> ID0','parametros',1,'p_parametros_1','Parser.py',108),
  ('parametros -> empty','parametros',1,'p_parametros_1','Parser.py',109),
  ('asignacion -> ID0 ASIGNACION funcionReservada PUNTOCOMA','asignacion',4,'p_asignacion_3','Statements.py',109),
  ('parametros -> ID0 COMA parametros','parametros',3,'p_parametros_2','Parser.py',117),
  ('asignacion -> ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA','asignacion',9,'p_asignacion_range','Statements.py',118),
  ('as -> ID0 ASIGNACION valor PUNTOCOMA','as',4,'p_globalVar','Parser.py',124),
  ('funcionReservada -> ID0 conjunto PUNTO F PUNTOCOMA','funcionReservada',5,'p_f','FuncionesReservadas.py',125),
  ('asignacion -> ID0 conjunto ASIGNACION valor PUNTOCOMA','asignacion',5,'p_asignacion_index','Statements.py',133),
  ('globalVar -> as globalVar','globalVar',2,'p_globalVar_2','Parser.py',135),
  ('globalVar -> empty','globalVar',1,'p_globalVar_2','Parser.py',136),
  ('confiCons -> timer rangoTimer dimFilas dimCol cubo','confiCons',5,'p_confiCons','Parser.py',140),
  ('funcionReservada -> BLINK PARENTESISI ID0 conjunto COMA NUMERO COMA rango COMA bool PARENTESISD PUNTOCOMA','funcionReservada',12,'p_blink_1','FuncionesReservadas.py',143),
  ('timer -> TIMER ASIGNACION NUMERO PUNTOCOMA','timer',4,'p_timer','Parser.py',148),
  ('asignacion -> ID0 conjunto ASIGNACION valor_b PUNTOCOMA','asignacion',5,'p_asignacion_index_3','Statements.py',152),
  ('rangoTimer -> RANGOTIMER ASIGNACION rango PUNTOCOMA','rangoTimer',4,'p_rango_timer','Parser.py',153),
  ('dimFilas -> DIMFILAS ASIGNACION NUMERO PUNTOCOMA','dimFilas',4,'p_dimFilas','Parser.py',158),
  ('funcionReservada -> BLINK PARENTESISI ID0 conjunto COMA bool PARENTESISD PUNTOCOMA','funcionReservada',8,'p_blink_2','FuncionesReservadas.py',160),
  ('dimCol -> DIMCOLUMNAS ASIGNACION NUMERO PUNTOCOMA','dimCol',4,'p_dimCol','Parser.py',163),
  ('cubo -> CUBO ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMA','cubo',6,'p_cubo','Parser.py',168),
  ('asignacion -> ID0 ASIGNACION valor_b PUNTOCOMA','asignacion',4,'p_asignacion_index_4','Statements.py',170),
  ('funcionReservada -> DELAY PARENTESISI PARENTESISD PUNTOCOMA','funcionReservada',4,'p_delay_1','FuncionesReservadas.py',177),
  ('funcionReservada -> DELAY PARENTESISI NUMERO COMA rango PARENTESISD PUNTOCOMA','funcionReservada',7,'p_delay_2','FuncionesReservadas.py',184),
  ('bifurcacion -> IF ID0 conjunto operador valor_b LLAVEI statements LLAVED PUNTOCOMA','bifurcacion',9,'p_if','Statements.py',184),
  ('funcionReservada -> ID0 PUNTO SHAPEF','funcionReservada',3,'p_shapeF','FuncionesReservadas.py',191),
  ('funcionReservada -> ID0 PUNTO SHAPEC','funcionReservada',3,'p_shapeC','FuncionesReservadas.py',205),
  ('operador -> COMPARACION','operador',1,'p_operador','Statements.py',205),
  ('operador -> DISTINTOQUE','operador',1,'p_operador','Statements.py',206),
  ('operador -> MENORQUE','operador',1,'p_operador','Statements.py',207),
  ('operador -> MAYORQUE','operador',1,'p_operador','Statements.py',208),
  ('operador -> MAYORIGUALQUE','operador',1,'p_operador','Statements.py',209),
  ('operador -> MENORIGUALQUE','operador',1,'p_operador','Statements.py',210),
  ('valor -> NUMERO','valor',1,'p_valor_0','Statements.py',215),
  ('valor -> bool','valor',1,'p_valor_0','Statements.py',216),
  ('funcionReservada -> ID0 PUNTO SHAPEA','funcionReservada',3,'p_shapeA','FuncionesReservadas.py',219),
  ('valor -> valor valor2','valor',2,'p_valor_1','Statements.py',222),
  ('valor2 -> COMA valor','valor2',2,'p_valor_2','Statements.py',227),
  ('valor -> lista','valor',1,'p_valor_3','Statements.py',232),
  ('funcionReservada -> CALL ID0 PARENTESISI parametrosFuncion PARENTESISD PUNTOCOMA','funcionReservada',6,'p_call','FuncionesReservadas.py',233),
  ('valor_b -> ID0 conjunto','valor_b',2,'p_valor_b','Statements.py',237),
  ('rango -> SEG','rango',1,'p_rango','FuncionesReservadas.py',241),
  ('rango -> MIN','rango',1,'p_rango','FuncionesReservadas.py',242),
  ('rango -> MIL','rango',1,'p_rango','FuncionesReservadas.py',243),
  ('tipo -> NUMERO','tipo',1,'p_tipo','FuncionesReservadas.py',248),
  ('valor_b -> NUMERO','valor_b',1,'p_valor_b2','Statements.py',249),
  ('valor_b -> bool','valor_b',1,'p_valor_b2','Statements.py',250),
  ('valor_b -> expression','valor_b',1,'p_valor_b2','Statements.py',251),
  ('bool -> TRUE','bool',1,'p_bool','Statements.py',256),
  ('bool -> FALSE','bool',1,'p_bool','Statements.py',257),
  ('conjunto -> PARENTESISCI indice DOSPUNTOS indice PARENTESISCD','conjunto',5,'p_conjunto_1','FuncionesReservadas.py',258),
  ('comentario_opcional -> COMENTARIO','comentario_opcional',1,'p_comentario_opcional','Statements.py',262),
  ('comentario_opcional -> empty','comentario_opcional',1,'p_comentario_opcional','Statements.py',263),
  ('conjunto -> PARENTESISCI DOSPUNTOS indice PARENTESISCD','conjunto',4,'p_conjunto_2','FuncionesReservadas.py',263),
  ('lista -> PARENTESISCI valor PARENTESISCD','lista',3,'p_lista_1','Statements.py',267),
  ('conjunto -> PARENTESISCI indice PARENTESISCD','conjunto',3,'p_conjunto_3','FuncionesReservadas.py',268),
  ('conjunto -> PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD','conjunto',6,'p_conjunto_4','FuncionesReservadas.py',273),
  ('conjunto -> empty','conjunto',1,'p_conjunto_5','FuncionesReservadas.py',278),
  ('rango_matriz -> PARENTESISCI indice PARENTESISCD','rango_matriz',3,'p_rango_matriz_1','FuncionesReservadas.py',282),
  ('conjunto -> PARENTESISCI indice COMA indice PARENTESISCD','conjunto',5,'p_rango_matriz_2','FuncionesReservadas.py',287),
  ('conjunto -> PARENTESISCI DOSPUNTOS COMA indice PARENTESISCD','conjunto',5,'p_rango_matriz_3','FuncionesReservadas.py',292),
  ('conjunto -> PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD','conjunto',9,'p_rango_matriz_4','FuncionesReservadas.py',297),
  ('parametrosFuncion -> ID0','parametrosFuncion',1,'p_parametros_funcion_1','FuncionesReservadas.py',302),
  ('parametrosFuncion -> NUMERO','parametrosFuncion',1,'p_parametros_funcion_1','FuncionesReservadas.py',303),
  ('parametrosFuncion -> empty','parametrosFuncion',1,'p_parametros_funcion_1','FuncionesReservadas.py',304),
  ('parametrosFuncion -> ID0 COMA parametrosFuncion','parametrosFuncion',3,'p_parametros_funcion_2','FuncionesReservadas.py',310),
  ('parametrosFuncion -> NUMERO COMA parametrosFuncion','parametrosFuncion',3,'p_parametros_funcion_3','FuncionesReservadas.py',315),
  ('indice -> NUMERO','indice',1,'p_indices','FuncionesReservadas.py',320),
  ('indice -> ID0','indice',1,'p_indices','FuncionesReservadas.py',321),
]
