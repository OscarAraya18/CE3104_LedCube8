
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONDIVISIONDIVISIONErightNEGATIVOleftPARENTESISIPARENTESISDASIGNACION BLINK BOOL CALL COMA COMENTARIO COMPARACION CUBO DEL DELAY DIMCOLUMNAS DIMFILAS DISTINTOQUE DIVISION DIVISIONE DOSPUNTOS EXPONENCIAL F FALSE FOR ID0 ID1 ID2 IN INSERT LEN LIST LLAVED LLAVEI MAIN MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MIL MIN MODULO MULTIPLICACION NEG NEGATIVO NUMERO PARENTESISCD PARENTESISCI PARENTESISD PARENTESISI PROCEDURE PUNTO PUNTOCOMA RANGE RANGOTIMER RESTA SEG SHAPEA SHAPEC SHAPEF STEP SUMA T TIMER TRUE TYPEindexar : ID0 PARENTESISCI NUMERO PARENTESISCDasignacion : ID0 ASIGNACION valor PUNTOCOMAexpression : expression SUMA termexpression : expression RESTA termasignacion : ID0 COMA asignacionindexar : ID0 PARENTESISCI NUMERO DOSPUNTOS NUMERO PARENTESISCDterm : term MULTIPLICACION factorterm : term DIVISION factorterm : term DIVISIONE factorasignacion : ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMAterm : term MODULO factorasignacion : ID0 ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMAindexar : ID0 PARENTESISCI DOSPUNTOS NUMERO PARENTESISCDterm : term EXPONENCIAL factorasignacion : ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMAexpression : RESTA term %prec NEGATIVOexpression : termasignacion : ID0 PARENTESISCI NUMERO PARENTESISCD ASIGNACION valor PUNTOCOMAterm : factorfactor : NUMEROvalor : NUMERO\n               | bool valor : valor valor2 valor2 : COMA valorbool : TRUE\n            | FALSEfactor : PARENTESISI expression PARENTESISDcomentario_opcional : COMENTARIO\n                          | emptyempty :'
    
_lr_action_items = {'ID0':([0,],[2,]),'$end':([1,6,10,11,],[0,-1,-13,-6,]),'PARENTESISCI':([2,],[3,]),'NUMERO':([3,5,7,],[4,8,9,]),'DOSPUNTOS':([3,4,],[5,7,]),'PARENTESISCD':([4,8,9,],[6,10,11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'indexar':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> indexar","S'",1,None,None,None),
  ('indexar -> ID0 PARENTESISCI NUMERO PARENTESISCD','indexar',4,'p_index_list','Valores.py',19),
  ('asignacion -> ID0 ASIGNACION valor PUNTOCOMA','asignacion',4,'p_asignacion_0','Statements.py',22),
  ('expression -> expression SUMA term','expression',3,'p_expression_suma','OperacionesMatematicas.py',28),
  ('expression -> expression RESTA term','expression',3,'p_expression_resta','OperacionesMatematicas.py',33),
  ('asignacion -> ID0 COMA asignacion','asignacion',3,'p_asignacion_1','Statements.py',36),
  ('indexar -> ID0 PARENTESISCI NUMERO DOSPUNTOS NUMERO PARENTESISCD','indexar',6,'p_index_list_2','Valores.py',37),
  ('term -> term MULTIPLICACION factor','term',3,'p_term_multiplicacion','OperacionesMatematicas.py',38),
  ('term -> term DIVISION factor','term',3,'p_term_division','OperacionesMatematicas.py',43),
  ('term -> term DIVISIONE factor','term',3,'p_term_divisione','OperacionesMatematicas.py',47),
  ('asignacion -> ID0 ASIGNACION PARENTESISCI PARENTESISCD PUNTOCOMA','asignacion',5,'p_asignacion_2','Statements.py',49),
  ('term -> term MODULO factor','term',3,'p_term_modulo','OperacionesMatematicas.py',51),
  ('asignacion -> ID0 ASIGNACION PARENTESISCI valor PARENTESISCD PUNTOCOMA','asignacion',6,'p_asignacion_3','Statements.py',54),
  ('indexar -> ID0 PARENTESISCI DOSPUNTOS NUMERO PARENTESISCD','indexar',5,'p_index_list_3','Valores.py',54),
  ('term -> term EXPONENCIAL factor','term',3,'p_term_exponencial','OperacionesMatematicas.py',55),
  ('asignacion -> ID0 ASIGNACION RANGE PARENTESISI NUMERO COMA bool PARENTESISD PUNTOCOMA','asignacion',9,'p_asignacion_range','Statements.py',58),
  ('expression -> RESTA term','expression',2,'p_expression_negativo','OperacionesMatematicas.py',59),
  ('expression -> term','expression',1,'p_expression_term','OperacionesMatematicas.py',66),
  ('asignacion -> ID0 PARENTESISCI NUMERO PARENTESISCD ASIGNACION valor PUNTOCOMA','asignacion',7,'p_asignacion_index','Statements.py',69),
  ('term -> factor','term',1,'p_term_factor','OperacionesMatematicas.py',71),
  ('factor -> NUMERO','factor',1,'p_factor_num','OperacionesMatematicas.py',76),
  ('valor -> NUMERO','valor',1,'p_valor_0','Statements.py',88),
  ('valor -> bool','valor',1,'p_valor_0','Statements.py',89),
  ('valor -> valor valor2','valor',2,'p_valor_1','Statements.py',94),
  ('valor2 -> COMA valor','valor2',2,'p_valor_2','Statements.py',98),
  ('bool -> TRUE','bool',1,'p_bool','Statements.py',103),
  ('bool -> FALSE','bool',1,'p_bool','Statements.py',104),
  ('factor -> PARENTESISI expression PARENTESISD','factor',3,'p_factor_expr','OperacionesMatematicas.py',107),
  ('comentario_opcional -> COMENTARIO','comentario_opcional',1,'p_comentario_opcional','Statements.py',108),
  ('comentario_opcional -> empty','comentario_opcional',1,'p_comentario_opcional','Statements.py',109),
  ('empty -> <empty>','empty',0,'p_empty','OperacionesMatematicas.py',112),
]
