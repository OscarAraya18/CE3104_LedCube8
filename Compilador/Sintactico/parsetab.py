
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'estructuraleftSUMARESTAleftMULTIPLICACIONDIVISIONDIVISIONErightNEGATIVOleftPARENTESISIPARENTESISDASIGNACION BLINK BOOL CALL COMA COMENTARIO COMPARACION CUBO DEL DELAY DIMCOLUMNAS DIMFILAS DISTINTOQUE DIVISION DIVISIONE DOSPUNTOS EXPONENCIAL F FALSE FOR ID0 ID1 ID2 IF IN INSERT LEN LIST LLAVED LLAVEI MAIN MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MIL MIN MODULO MULTIPLICACION NEG NEGATIVO NUMERO PARENTESISCD PARENTESISCI PARENTESISD PARENTESISI PROCEDURE PUNTO PUNTOCOMA RANGE RANGOTIMER RESTA SEG SHAPEA SHAPEC SHAPEF STEP SUMA T TIMER TRUE TYPEloop : FOR ID0 IN iterable STEP NUMERO LLAVEI statements LLAVED PUNTOCOMAfuncionReservada : ID0 PUNTO INSERT PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMAstatements : COMENTARIO statementsestructura : confiCons    globalVar    main    rutinas statements : emptystatements : expression PUNTOCOMA statementsloop : FOR ID0 IN iterable LLAVEI statements LLAVED PUNTOCOMAfuncionReservada : ID0 PUNTO INSERT PARENTESISI valor COMA tipo COMA NUMERO PARENTESISD PUNTOCOMAstatements : loop statements\n                  | asignacion statementsexpression : expression SUMA termexpression : expression RESTA termfuncionReservada : ID0 PUNTO INSERT PARENTESISI valor COMA NUMERO PARENTESISD PUNTOCOMA main : PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMAiterable : NUMEROterm : term MULTIPLICACION factorstatements : funcionReservada statementsiterable : ID0 conjuntoterm : term DIVISION factorstatements : bifurcacion statementsterm : term DIVISIONE factorrutinas : rutina rutinas statements : rutina statementsfuncionReservada : ID0 PUNTO DEL PARENTESISI NUMERO PARENTESISD PUNTOCOMAterm : term MODULO factorrutinas : emptyterm : term EXPONENCIAL factorasignacion : ID0 ASIGNACION valor PUNTOCOMAfuncionReservada : ID0 PUNTO DEL PARENTESISI NUMERO COMA tipo PARENTESISD PUNTOCOMAexpression : RESTA term %prec NEGATIVOrutina : PROCEDURE ID0 PARENTESISI parametros PARENTESISD LLAVEI statements LLAVED PUNTOCOMAexpression : termfuncionReservada :  LEN PARENTESISI ID0 PARENTESISD PUNTOCOMAterm : factorfuncionReservada : ID0 conjunto PUNTO NEG PUNTOCOMAfactor : NUMEROasignacion : ID0 COMA asignacionfactor : PARENTESISI expression PARENTESISDempty :funcionReservada : ID0 conjunto PUNTO T PUNTOCOMA\n                        | CUBO conjunto PUNTO T PUNTOCOMAparametros : ID0\n                  | empty asignacion : ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMAparametros : ID0 COMA parametrosas : ID0 ASIGNACION valor PUNTOCOMAasignacion : ID0 ASIGNACION funcionReservada PUNTOCOMAfuncionReservada : ID0 conjunto PUNTO F PUNTOCOMA\n                        | CUBO conjunto PUNTO F PUNTOCOMAglobalVar : as globalVar\n                 | emptyasignacion : ID0 ASIGNACION expression PUNTOCOMAconfiCons : timer    rangoTimer    dimFilas    dimCol    cubotimer : TIMER ASIGNACION NUMERO PUNTOCOMAasignacion : ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMArangoTimer : RANGOTIMER ASIGNACION rango PUNTOCOMAdimFilas : DIMFILAS ASIGNACION NUMERO PUNTOCOMAfuncionReservada : BLINK PARENTESISI ID0 conjunto COMA NUMERO COMA rango COMA bool PARENTESISD PUNTOCOMA dimCol : DIMCOLUMNAS ASIGNACION NUMERO PUNTOCOMAasignacion : ID0 conjunto ASIGNACION valor PUNTOCOMAcubo : CUBO ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMAfuncionReservada : BLINK PARENTESISI ID0 conjunto COMA bool PARENTESISD PUNTOCOMAasignacion : ID0 conjunto ASIGNACION valor_b PUNTOCOMAfuncionReservada : DELAY PARENTESISI PARENTESISD PUNTOCOMAasignacion : ID0 ASIGNACION valor_b PUNTOCOMAfuncionReservada : DELAY PARENTESISI NUMERO COMA rango PARENTESISD PUNTOCOMAbifurcacion : IF ID0 conjunto operador valor_b LLAVEI statements LLAVED PUNTOCOMAfuncionReservada : ID0 PUNTO SHAPEFfuncionReservada : ID0 PUNTO SHAPECoperador : COMPARACION\n                | DISTINTOQUE\n                | MENORQUE\n                | MAYORQUE\n                | MAYORIGUALQUE\n                | MENORIGUALQUE funcionReservada : ID0 PUNTO SHAPEAvalor : NUMERO\n             | bool valor : valor valor2 funcionReservada : CALL ID0 PARENTESISI parametrosFuncion PARENTESISD PUNTOCOMAvalor2 : COMA valorvalor : listarango : SEG\n             | MIN\n             | MILvalor_b : ID0 conjuntotipo : NUMERO valor_b : NUMERO\n               | bool\n               | expressionconjunto : PARENTESISCI indice DOSPUNTOS indice PARENTESISCDbool : TRUE\n            | FALSEconjunto : PARENTESISCI DOSPUNTOS indice PARENTESISCDconjunto : PARENTESISCI indice PARENTESISCDcomentario_opcional : COMENTARIO\n                           | emptyconjunto : PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD lista : PARENTESISCI valor PARENTESISCDconjunto : emptyrango_matriz : PARENTESISCI indice PARENTESISCDconjunto : PARENTESISCI indice COMA indice PARENTESISCDconjunto : PARENTESISCI DOSPUNTOS COMA indice PARENTESISCDconjunto : PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCDparametrosFuncion : ID0\n                         | NUMERO\n                         | emptyparametrosFuncion : ID0 COMA parametrosFuncionparametrosFuncion : NUMERO COMA parametrosFuncionindice : NUMERO\n              | ID0'
    
_lr_action_items = {'TIMER':([0,],[4,]),'$end':([1,12,20,21,22,40,125,208,],[0,-39,-4,-39,-26,-22,-14,-31,]),'ID0':([2,6,23,43,47,52,62,65,69,72,73,74,75,76,79,86,87,91,95,110,111,112,116,118,134,145,147,150,154,155,156,162,164,170,172,173,175,177,179,181,195,201,202,203,204,205,206,207,208,211,212,215,220,221,222,223,224,228,229,230,233,235,254,256,257,264,269,272,274,280,283,285,287,288,290,291,295,297,],[8,8,41,-46,-53,59,80,59,80,80,80,80,80,80,109,120,121,80,80,135,144,149,157,159,166,-37,149,182,-68,-69,-76,197,-61,-28,-47,-52,-65,149,149,149,-64,182,-70,-71,-72,-73,-74,-75,-31,80,-44,149,-60,-63,-35,-40,-48,-33,-41,-49,197,197,-80,80,80,-24,-66,-7,149,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'PROCEDURE':([2,5,6,7,12,14,21,43,47,62,69,72,73,74,75,76,91,95,125,145,154,155,156,164,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[-39,13,-39,-51,23,-50,23,-46,-53,23,23,23,23,23,23,23,23,23,-14,-37,-68,-69,-76,-61,-28,-47,-52,-65,-64,-31,23,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,23,23,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'RANGOTIMER':([3,39,],[10,-54,]),'ASIGNACION':([4,8,10,17,33,48,80,113,115,144,176,178,217,242,244,245,260,292,],[11,15,18,34,49,56,110,150,-100,110,150,-95,-94,-91,-102,-103,-98,-104,]),'DIMFILAS':([9,51,],[17,-56,]),'NUMERO':([11,15,31,34,45,49,62,63,67,69,72,73,74,75,76,78,91,95,96,97,103,104,105,106,107,110,112,119,134,137,145,147,150,154,155,156,162,170,172,173,174,175,177,179,181,189,190,195,201,202,203,204,205,206,207,208,210,211,212,215,220,221,222,223,224,228,229,230,231,233,235,247,249,254,256,257,264,269,272,274,276,280,283,285,287,288,290,291,295,297,],[19,26,26,50,26,57,81,26,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,141,148,161,168,26,-37,148,141,-68,-69,-76,199,-28,-47,-52,213,-65,148,148,148,225,227,-64,237,-70,-71,-72,-73,-74,-75,-31,239,81,-44,148,-60,-63,-35,-40,-48,-33,-41,-49,250,199,199,263,265,-80,81,81,-24,-66,-7,148,286,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'MAIN':([13,],[24,]),'TRUE':([15,31,45,63,110,137,150,189,201,202,203,204,205,206,207,231,241,246,247,289,],[29,29,29,29,29,29,29,29,29,-70,-71,-72,-73,-74,-75,29,29,29,29,29,]),'FALSE':([15,31,45,63,110,137,150,189,201,202,203,204,205,206,207,231,241,246,247,289,],[30,30,30,30,30,30,30,30,30,-70,-71,-72,-73,-74,-75,30,30,30,30,30,]),'PARENTESISCI':([15,31,45,56,63,80,83,110,121,135,137,144,150,159,166,178,182,189,247,260,],[31,31,31,63,31,112,112,137,112,112,31,112,31,112,112,215,112,31,31,274,]),'DIMCOLUMNAS':([16,58,],[33,-57,]),'SEG':([18,196,267,],[36,36,36,]),'MIN':([18,196,267,],[37,37,37,]),'MIL':([18,196,267,],[38,38,38,]),'PUNTOCOMA':([19,25,26,27,28,29,30,35,36,37,38,44,50,54,55,57,71,77,81,88,93,108,115,122,124,127,128,129,130,131,132,133,135,136,138,139,141,142,143,154,155,156,160,165,169,171,178,182,183,184,185,186,187,188,191,192,193,195,217,219,222,223,224,228,229,230,234,242,244,245,248,252,254,258,260,264,268,269,273,275,277,278,280,281,282,285,287,288,292,293,295,296,297,],[39,43,-77,-78,-82,-92,-93,51,-83,-84,-85,-79,58,-81,-99,64,95,-32,-36,-34,125,-30,-100,164,-38,-11,-12,-16,-19,-21,-25,-27,-39,170,172,173,-36,-78,175,-68,-69,-76,195,208,-86,212,-95,-39,220,221,-90,222,223,224,228,229,230,-64,-94,-86,-35,-40,-48,-33,-41,-49,254,-91,-102,-103,264,269,-80,272,-98,-24,280,-66,283,285,287,288,-62,290,291,-2,-13,-29,-104,295,-8,297,-58,]),'PARENTESISI':([24,41,62,67,69,72,73,74,75,76,78,82,84,85,91,95,96,97,103,104,105,106,107,110,120,140,145,150,152,153,154,155,156,170,172,173,175,195,201,202,203,204,205,206,207,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[42,52,67,67,67,67,67,67,67,67,67,116,118,119,67,67,67,67,67,67,67,67,67,67,162,174,-37,67,189,190,-68,-69,-76,-28,-47,-52,-65,-64,67,-70,-71,-72,-73,-74,-75,-31,67,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,67,67,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'COMA':([25,26,27,28,29,30,36,37,38,44,46,54,55,59,80,89,115,136,141,142,144,146,147,148,149,159,161,178,183,194,197,199,213,217,225,226,227,242,244,245,250,260,262,263,279,292,],[45,-77,-78,-82,-92,-93,-83,-84,-85,-79,45,45,-99,65,111,45,-100,45,-77,-78,111,179,181,-110,-111,-39,196,-95,45,231,233,235,241,-94,246,247,249,-91,-102,-103,267,-98,276,-77,289,-104,]),'PARENTESISCD':([26,27,28,29,30,44,46,54,55,89,137,146,148,149,180,214,216,218,243,284,],[-77,-78,-82,-92,-93,-79,55,-81,-99,122,171,178,-110,-111,217,242,244,245,260,292,]),'LLAVEI':([29,30,53,66,77,81,88,108,115,124,127,128,129,130,131,132,133,166,167,168,178,182,185,209,217,219,236,237,238,239,242,244,245,260,292,],[-92,-93,62,91,-32,-36,-34,-30,-100,-38,-11,-12,-16,-19,-21,-25,-27,-39,211,-15,-95,-39,-90,-18,-94,-86,256,-36,-89,257,-91,-102,-103,-98,-104,]),'PARENTESISD':([29,30,36,37,38,42,52,59,60,61,65,77,81,88,90,92,108,119,124,127,128,129,130,131,132,133,157,162,197,198,199,200,227,232,233,235,251,253,255,259,261,263,265,266,286,294,],[-92,-93,-83,-84,-85,53,-39,-42,66,-43,-39,-32,-36,-34,-45,124,-30,160,-38,-11,-12,-16,-19,-21,-25,-27,191,-39,-105,234,-106,-107,248,252,-39,-39,268,-108,-109,273,275,277,-87,278,293,296,]),'CUBO':([32,62,64,69,72,73,74,75,76,91,95,110,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[48,83,-59,83,83,83,83,83,83,83,83,83,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,83,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,83,83,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'COMENTARIO':([62,69,72,73,74,75,76,91,95,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[69,69,69,69,69,69,69,69,69,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,69,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,69,69,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'LLAVED':([62,68,69,70,72,73,74,75,76,91,94,95,98,99,100,101,102,123,126,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,240,254,256,257,264,269,270,271,272,280,283,285,287,288,290,291,295,297,],[-39,93,-39,-5,-39,-39,-39,-39,-39,-39,-3,-39,-9,-10,-17,-20,-23,165,-6,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,-39,-44,-60,-63,-35,-40,-48,-33,-41,-49,258,-80,-39,-39,-24,-66,281,282,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'RESTA':([62,67,69,71,72,73,74,75,76,77,81,88,91,92,95,108,110,124,127,128,129,130,131,132,133,139,141,145,150,154,155,156,170,172,173,175,185,195,201,202,203,204,205,206,207,208,211,212,220,221,222,223,224,228,229,230,237,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[78,78,78,97,78,78,78,78,78,-32,-36,-34,78,97,78,-30,78,-38,-11,-12,-16,-19,-21,-25,-27,97,-36,-37,78,-68,-69,-76,-28,-47,-52,-65,97,-64,78,-70,-71,-72,-73,-74,-75,-31,78,-44,-60,-63,-35,-40,-48,-33,-41,-49,-36,-80,78,78,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'FOR':([62,69,72,73,74,75,76,91,95,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[79,79,79,79,79,79,79,79,79,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,79,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,79,79,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'LEN':([62,69,72,73,74,75,76,91,95,110,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[82,82,82,82,82,82,82,82,82,82,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,82,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,82,82,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'BLINK':([62,69,72,73,74,75,76,91,95,110,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[84,84,84,84,84,84,84,84,84,84,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,84,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,84,84,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'DELAY':([62,69,72,73,74,75,76,91,95,110,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[85,85,85,85,85,85,85,85,85,85,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,85,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,85,85,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'CALL':([62,69,72,73,74,75,76,91,95,110,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[86,86,86,86,86,86,86,86,86,86,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,86,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,86,86,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'IF':([62,69,72,73,74,75,76,91,95,145,154,155,156,170,172,173,175,195,208,211,212,220,221,222,223,224,228,229,230,254,256,257,264,269,272,280,283,285,287,288,290,291,295,297,],[87,87,87,87,87,87,87,87,87,-37,-68,-69,-76,-28,-47,-52,-65,-64,-31,87,-44,-60,-63,-35,-40,-48,-33,-41,-49,-80,87,87,-24,-66,-7,-62,-55,-2,-13,-29,-67,-1,-8,-58,]),'SUMA':([71,77,81,88,92,108,124,127,128,129,130,131,132,133,139,141,185,237,],[96,-32,-36,-34,96,-30,-38,-11,-12,-16,-19,-21,-25,-27,96,-36,96,-36,]),'MULTIPLICACION':([77,81,88,108,124,127,128,129,130,131,132,133,141,237,],[103,-36,-34,103,-38,103,103,-16,-19,-21,-25,-27,-36,-36,]),'DIVISION':([77,81,88,108,124,127,128,129,130,131,132,133,141,237,],[104,-36,-34,104,-38,104,104,-16,-19,-21,-25,-27,-36,-36,]),'DIVISIONE':([77,81,88,108,124,127,128,129,130,131,132,133,141,237,],[105,-36,-34,105,-38,105,105,-16,-19,-21,-25,-27,-36,-36,]),'MODULO':([77,81,88,108,124,127,128,129,130,131,132,133,141,237,],[106,-36,-34,106,-38,106,106,-16,-19,-21,-25,-27,-36,-36,]),'EXPONENCIAL':([77,81,88,108,124,127,128,129,130,131,132,133,141,237,],[107,-36,-34,107,-38,107,107,-16,-19,-21,-25,-27,-36,-36,]),'PUNTO':([80,83,113,115,117,135,169,178,217,242,244,245,260,292,],[114,-39,151,-100,158,114,151,-95,-94,-91,-102,-103,-98,-104,]),'IN':([109,],[134,]),'RANGE':([110,],[140,]),'DOSPUNTOS':([112,146,148,149,],[147,177,-110,-111,]),'INSERT':([114,],[152,]),'DEL':([114,],[153,]),'SHAPEF':([114,],[154,]),'SHAPEC':([114,],[155,]),'SHAPEA':([114,],[156,]),'COMPARACION':([115,121,163,178,217,242,244,245,260,292,],[-100,-39,202,-95,-94,-91,-102,-103,-98,-104,]),'DISTINTOQUE':([115,121,163,178,217,242,244,245,260,292,],[-100,-39,203,-95,-94,-91,-102,-103,-98,-104,]),'MENORQUE':([115,121,163,178,217,242,244,245,260,292,],[-100,-39,204,-95,-94,-91,-102,-103,-98,-104,]),'MAYORQUE':([115,121,163,178,217,242,244,245,260,292,],[-100,-39,205,-95,-94,-91,-102,-103,-98,-104,]),'MAYORIGUALQUE':([115,121,163,178,217,242,244,245,260,292,],[-100,-39,206,-95,-94,-91,-102,-103,-98,-104,]),'MENORIGUALQUE':([115,121,163,178,217,242,244,245,260,292,],[-100,-39,207,-95,-94,-91,-102,-103,-98,-104,]),'STEP':([115,166,167,168,178,209,217,242,244,245,260,292,],[-100,-39,210,-15,-95,-18,-94,-91,-102,-103,-98,-104,]),'NEG':([151,],[186,]),'T':([151,158,],[187,192,]),'F':([151,158,],[188,193,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'estructura':([0,],[1,]),'confiCons':([0,],[2,]),'timer':([0,],[3,]),'globalVar':([2,6,],[5,14,]),'as':([2,6,],[6,6,]),'empty':([2,6,12,21,52,62,65,69,72,73,74,75,76,80,83,91,95,121,135,144,159,162,166,182,211,233,235,256,257,],[7,7,22,22,61,70,61,70,70,70,70,70,70,115,115,70,70,115,115,115,115,200,115,115,70,200,200,70,70,]),'rangoTimer':([3,],[9,]),'main':([5,],[12,]),'dimFilas':([9,],[16,]),'rutinas':([12,21,],[20,40,]),'rutina':([12,21,62,69,72,73,74,75,76,91,95,211,256,257,],[21,21,76,76,76,76,76,76,76,76,76,76,76,76,]),'valor':([15,31,45,63,110,137,150,189,247,],[25,46,54,89,136,46,183,226,54,]),'bool':([15,31,45,63,110,137,150,189,201,231,241,246,247,289,],[27,27,27,27,142,27,142,27,238,251,259,261,27,294,]),'lista':([15,31,45,63,110,137,150,189,247,],[28,28,28,28,28,28,28,28,28,]),'dimCol':([16,],[32,]),'rango':([18,196,267,],[35,232,279,]),'valor2':([25,46,54,89,136,183,226,],[44,44,44,44,44,44,44,]),'cubo':([32,],[47,]),'parametros':([52,65,],[60,90,]),'statements':([62,69,72,73,74,75,76,91,95,211,256,257,],[68,94,98,99,100,101,102,123,126,240,270,271,]),'expression':([62,67,69,72,73,74,75,76,91,95,110,150,201,211,256,257,],[71,92,71,71,71,71,71,71,71,71,139,185,185,71,71,71,]),'loop':([62,69,72,73,74,75,76,91,95,211,256,257,],[72,72,72,72,72,72,72,72,72,72,72,72,]),'asignacion':([62,69,72,73,74,75,76,91,95,111,211,256,257,],[73,73,73,73,73,73,73,73,73,145,73,73,73,]),'funcionReservada':([62,69,72,73,74,75,76,91,95,110,211,256,257,],[74,74,74,74,74,74,74,74,74,138,74,74,74,]),'bifurcacion':([62,69,72,73,74,75,76,91,95,211,256,257,],[75,75,75,75,75,75,75,75,75,75,75,75,]),'term':([62,67,69,72,73,74,75,76,78,91,95,96,97,110,150,201,211,256,257,],[77,77,77,77,77,77,77,77,108,77,77,127,128,77,77,77,77,77,77,]),'factor':([62,67,69,72,73,74,75,76,78,91,95,96,97,103,104,105,106,107,110,150,201,211,256,257,],[88,88,88,88,88,88,88,88,88,88,88,88,88,129,130,131,132,133,88,88,88,88,88,88,]),'conjunto':([80,83,121,135,144,159,166,182,],[113,117,163,169,176,194,209,219,]),'valor_b':([110,150,201,],[143,184,236,]),'indice':([112,147,177,179,181,215,274,],[146,180,214,216,218,243,284,]),'iterable':([134,],[167,]),'parametrosFuncion':([162,233,235,],[198,253,255,]),'operador':([163,],[201,]),'tipo':([247,249,],[262,266,]),}

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
  ('loop -> FOR ID0 IN iterable LLAVEI statements LLAVED PUNTOCOMA','loop',8,'p_loop_for_2','Ciclos.py',35),
  ('funcionReservada -> ID0 PUNTO INSERT PARENTESISI valor COMA tipo COMA NUMERO PARENTESISD PUNTOCOMA','funcionReservada',11,'p_insert_2','FuncionesReservadas.py',35),
  ('statements -> loop statements','statements',2,'p_statements_4','Statements.py',38),
  ('statements -> asignacion statements','statements',2,'p_statements_4','Statements.py',39),
  ('expression -> expression SUMA term','expression',3,'p_expression_suma','OperacionesMatematicas.py',42),
  ('expression -> expression RESTA term','expression',3,'p_expression_resta','OperacionesMatematicas.py',47),
  ('funcionReservada -> ID0 PUNTO INSERT PARENTESISI valor COMA NUMERO PARENTESISD PUNTOCOMA','funcionReservada',9,'p_insert_3','FuncionesReservadas.py',50),
  ('main -> PROCEDURE MAIN PARENTESISI PARENTESISD LLAVEI statements LLAVED PUNTOCOMA','main',8,'p_main','Parser.py',51),
  ('iterable -> NUMERO','iterable',1,'p_iterable_1','Ciclos.py',52),
  ('term -> term MULTIPLICACION factor','term',3,'p_term_multiplicacion','OperacionesMatematicas.py',52),
  ('statements -> funcionReservada statements','statements',2,'p_statements_5','Statements.py',53),
  ('iterable -> ID0 conjunto','iterable',2,'p_iterable_2','Ciclos.py',57),
  ('term -> term DIVISION factor','term',3,'p_term_division','OperacionesMatematicas.py',57),
  ('statements -> bifurcacion statements','statements',2,'p_statements_6','Statements.py',59),
  ('term -> term DIVISIONE factor','term',3,'p_term_divisione','OperacionesMatematicas.py',61),
  ('rutinas -> rutina rutinas','rutinas',2,'p_rutinas_1','Parser.py',61),
  ('statements -> rutina statements','statements',2,'p_statements_7','Statements.py',64),
  ('funcionReservada -> ID0 PUNTO DEL PARENTESISI NUMERO PARENTESISD PUNTOCOMA','funcionReservada',7,'p_del','FuncionesReservadas.py',65),
  ('term -> term MODULO factor','term',3,'p_term_modulo','OperacionesMatematicas.py',65),
  ('rutinas -> empty','rutinas',1,'p_rutinas_2','Parser.py',68),
  ('term -> term EXPONENCIAL factor','term',3,'p_term_exponencial','OperacionesMatematicas.py',69),
  ('asignacion -> ID0 ASIGNACION valor PUNTOCOMA','asignacion',4,'p_asignacion_0','Statements.py',69),
  ('funcionReservada -> ID0 PUNTO DEL PARENTESISI NUMERO COMA tipo PARENTESISD PUNTOCOMA','funcionReservada',9,'p_del_2','FuncionesReservadas.py',73),
  ('expression -> RESTA term','expression',2,'p_expression_negativo','OperacionesMatematicas.py',73),
  ('rutina -> PROCEDURE ID0 PARENTESISI parametros PARENTESISD LLAVEI statements LLAVED PUNTOCOMA','rutina',9,'p_rutina','Parser.py',73),
  ('expression -> term','expression',1,'p_expression_term','OperacionesMatematicas.py',80),
  ('funcionReservada -> LEN PARENTESISI ID0 PARENTESISD PUNTOCOMA','funcionReservada',5,'p_len','FuncionesReservadas.py',81),
  ('term -> factor','term',1,'p_term_factor','OperacionesMatematicas.py',85),
  ('funcionReservada -> ID0 conjunto PUNTO NEG PUNTOCOMA','funcionReservada',5,'p_neg','FuncionesReservadas.py',89),
  ('factor -> NUMERO','factor',1,'p_factor_num','OperacionesMatematicas.py',90),
  ('asignacion -> ID0 COMA asignacion','asignacion',3,'p_asignacion_1','Statements.py',94),
  ('factor -> PARENTESISI expression PARENTESISD','factor',3,'p_factor_expr','OperacionesMatematicas.py',95),
  ('empty -> <empty>','empty',0,'p_empty','OperacionesMatematicas.py',100),
  ('funcionReservada -> ID0 conjunto PUNTO T PUNTOCOMA','funcionReservada',5,'p_t','FuncionesReservadas.py',107),
  ('funcionReservada -> CUBO conjunto PUNTO T PUNTOCOMA','funcionReservada',5,'p_t','FuncionesReservadas.py',108),
  ('parametros -> ID0','parametros',1,'p_parametros_1','Parser.py',108),
  ('parametros -> empty','parametros',1,'p_parametros_1','Parser.py',109),
  ('asignacion -> ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMA','asignacion',5,'p_asignacion_2','Statements.py',116),
  ('parametros -> ID0 COMA parametros','parametros',3,'p_parametros_2','Parser.py',117),
  ('as -> ID0 ASIGNACION valor PUNTOCOMA','as',4,'p_globalVar','Parser.py',124),
  ('asignacion -> ID0 ASIGNACION funcionReservada PUNTOCOMA','asignacion',4,'p_asignacion_3','Statements.py',128),
  ('funcionReservada -> ID0 conjunto PUNTO F PUNTOCOMA','funcionReservada',5,'p_f','FuncionesReservadas.py',135),
  ('funcionReservada -> CUBO conjunto PUNTO F PUNTOCOMA','funcionReservada',5,'p_f','FuncionesReservadas.py',136),
  ('globalVar -> as globalVar','globalVar',2,'p_globalVar_2','Parser.py',135),
  ('globalVar -> empty','globalVar',1,'p_globalVar_2','Parser.py',136),
  ('asignacion -> ID0 ASIGNACION expression PUNTOCOMA','asignacion',4,'p_asignacion_4','Statements.py',136),
  ('confiCons -> timer rangoTimer dimFilas dimCol cubo','confiCons',5,'p_confiCons','Parser.py',140),
  ('timer -> TIMER ASIGNACION NUMERO PUNTOCOMA','timer',4,'p_timer','Parser.py',148),
  ('asignacion -> ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA','asignacion',9,'p_asignacion_range','Statements.py',148),
  ('rangoTimer -> RANGOTIMER ASIGNACION rango PUNTOCOMA','rangoTimer',4,'p_rango_timer','Parser.py',153),
  ('dimFilas -> DIMFILAS ASIGNACION NUMERO PUNTOCOMA','dimFilas',4,'p_dimFilas','Parser.py',158),
  ('funcionReservada -> BLINK PARENTESISI ID0 conjunto COMA NUMERO COMA rango COMA bool PARENTESISD PUNTOCOMA','funcionReservada',12,'p_blink_1','FuncionesReservadas.py',163),
  ('dimCol -> DIMCOLUMNAS ASIGNACION NUMERO PUNTOCOMA','dimCol',4,'p_dimCol','Parser.py',163),
  ('asignacion -> ID0 conjunto ASIGNACION valor PUNTOCOMA','asignacion',5,'p_asignacion_index','Statements.py',164),
  ('cubo -> CUBO ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMA','cubo',6,'p_cubo','Parser.py',168),
  ('funcionReservada -> BLINK PARENTESISI ID0 conjunto COMA bool PARENTESISD PUNTOCOMA','funcionReservada',8,'p_blink_2','FuncionesReservadas.py',180),
  ('asignacion -> ID0 conjunto ASIGNACION valor_b PUNTOCOMA','asignacion',5,'p_asignacion_index_3','Statements.py',183),
  ('funcionReservada -> DELAY PARENTESISI PARENTESISD PUNTOCOMA','funcionReservada',4,'p_delay_1','FuncionesReservadas.py',197),
  ('asignacion -> ID0 ASIGNACION valor_b PUNTOCOMA','asignacion',4,'p_asignacion_index_4','Statements.py',201),
  ('funcionReservada -> DELAY PARENTESISI NUMERO COMA rango PARENTESISD PUNTOCOMA','funcionReservada',7,'p_delay_2','FuncionesReservadas.py',204),
  ('bifurcacion -> IF ID0 conjunto operador valor_b LLAVEI statements LLAVED PUNTOCOMA','bifurcacion',9,'p_if','Statements.py',210),
  ('funcionReservada -> ID0 PUNTO SHAPEF','funcionReservada',3,'p_shapeF','FuncionesReservadas.py',211),
  ('funcionReservada -> ID0 PUNTO SHAPEC','funcionReservada',3,'p_shapeC','FuncionesReservadas.py',225),
  ('operador -> COMPARACION','operador',1,'p_operador','Statements.py',231),
  ('operador -> DISTINTOQUE','operador',1,'p_operador','Statements.py',232),
  ('operador -> MENORQUE','operador',1,'p_operador','Statements.py',233),
  ('operador -> MAYORQUE','operador',1,'p_operador','Statements.py',234),
  ('operador -> MAYORIGUALQUE','operador',1,'p_operador','Statements.py',235),
  ('operador -> MENORIGUALQUE','operador',1,'p_operador','Statements.py',236),
  ('funcionReservada -> ID0 PUNTO SHAPEA','funcionReservada',3,'p_shapeA','FuncionesReservadas.py',239),
  ('valor -> NUMERO','valor',1,'p_valor_0','Statements.py',241),
  ('valor -> bool','valor',1,'p_valor_0','Statements.py',242),
  ('valor -> valor valor2','valor',2,'p_valor_1','Statements.py',248),
  ('funcionReservada -> CALL ID0 PARENTESISI parametrosFuncion PARENTESISD PUNTOCOMA','funcionReservada',6,'p_call','FuncionesReservadas.py',253),
  ('valor2 -> COMA valor','valor2',2,'p_valor_2','Statements.py',253),
  ('valor -> lista','valor',1,'p_valor_3','Statements.py',258),
  ('rango -> SEG','rango',1,'p_rango','FuncionesReservadas.py',261),
  ('rango -> MIN','rango',1,'p_rango','FuncionesReservadas.py',262),
  ('rango -> MIL','rango',1,'p_rango','FuncionesReservadas.py',263),
  ('valor_b -> ID0 conjunto','valor_b',2,'p_valor_b','Statements.py',263),
  ('tipo -> NUMERO','tipo',1,'p_tipo','FuncionesReservadas.py',268),
  ('valor_b -> NUMERO','valor_b',1,'p_valor_b2','Statements.py',275),
  ('valor_b -> bool','valor_b',1,'p_valor_b2','Statements.py',276),
  ('valor_b -> expression','valor_b',1,'p_valor_b2','Statements.py',277),
  ('conjunto -> PARENTESISCI indice DOSPUNTOS indice PARENTESISCD','conjunto',5,'p_conjunto_1','FuncionesReservadas.py',278),
  ('bool -> TRUE','bool',1,'p_bool','Statements.py',282),
  ('bool -> FALSE','bool',1,'p_bool','Statements.py',283),
  ('conjunto -> PARENTESISCI DOSPUNTOS indice PARENTESISCD','conjunto',4,'p_conjunto_2','FuncionesReservadas.py',283),
  ('conjunto -> PARENTESISCI indice PARENTESISCD','conjunto',3,'p_conjunto_3','FuncionesReservadas.py',288),
  ('comentario_opcional -> COMENTARIO','comentario_opcional',1,'p_comentario_opcional','Statements.py',288),
  ('comentario_opcional -> empty','comentario_opcional',1,'p_comentario_opcional','Statements.py',289),
  ('conjunto -> PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD','conjunto',6,'p_conjunto_4','FuncionesReservadas.py',293),
  ('lista -> PARENTESISCI valor PARENTESISCD','lista',3,'p_lista_1','Statements.py',293),
  ('conjunto -> empty','conjunto',1,'p_conjunto_5','FuncionesReservadas.py',298),
  ('rango_matriz -> PARENTESISCI indice PARENTESISCD','rango_matriz',3,'p_rango_matriz_1','FuncionesReservadas.py',302),
  ('conjunto -> PARENTESISCI indice COMA indice PARENTESISCD','conjunto',5,'p_rango_matriz_2','FuncionesReservadas.py',307),
  ('conjunto -> PARENTESISCI DOSPUNTOS COMA indice PARENTESISCD','conjunto',5,'p_rango_matriz_3','FuncionesReservadas.py',312),
  ('conjunto -> PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD PARENTESISCI indice PARENTESISCD','conjunto',9,'p_rango_matriz_4','FuncionesReservadas.py',317),
  ('parametrosFuncion -> ID0','parametrosFuncion',1,'p_parametros_funcion_1','FuncionesReservadas.py',322),
  ('parametrosFuncion -> NUMERO','parametrosFuncion',1,'p_parametros_funcion_1','FuncionesReservadas.py',323),
  ('parametrosFuncion -> empty','parametrosFuncion',1,'p_parametros_funcion_1','FuncionesReservadas.py',324),
  ('parametrosFuncion -> ID0 COMA parametrosFuncion','parametrosFuncion',3,'p_parametros_funcion_2','FuncionesReservadas.py',330),
  ('parametrosFuncion -> NUMERO COMA parametrosFuncion','parametrosFuncion',3,'p_parametros_funcion_3','FuncionesReservadas.py',335),
  ('indice -> NUMERO','indice',1,'p_indices','FuncionesReservadas.py',340),
  ('indice -> ID0','indice',1,'p_indices','FuncionesReservadas.py',341),
]
