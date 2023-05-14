
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACHAV APAR APAR2 BINARY BOOL CCHAV COMMA COMMENT CPAR CPAR2 DATE DATETIME DOT EQUALS FLOAT HEXA INFINITY INTEGER KEY MULTILINE_STRING MULTILINE_STRING_LITERAL NAN NEWLINE NULL OCTAL STRING STRING_LITERAL TIMEconverter : file\n    file : file_lines last_line\n    file_lines : line\n             | file_lines line\n    line : NEWLINE\n    line : elem_newline\n    last_line : elem\n                 | empty\n    elem_newline : atrib NEWLINE \n                    | table NEWLINE \n                    | array_table NEWLINE \n    empty :elem : atrib\n            | table\n            | array_table\n    atrib : FLOAT EQUALS content\n    atrib : key EQUALS content\n            | key EQUALS content COMMENT\n            | key DOT atrib\n    content : value\n                | APAR arr_cont\n                | APAR NEWLINE arr_cont\n                | ACHAV table_cont\n    arr_cont : CPAR\n                | a_cont CPAR\n                | a_cont COMMA CPAR\n                | a_cont NEWLINE CPAR\n                | a_cont COMMA NEWLINE CPAR\n    a_cont : COMMENT NEWLINE a_cont\n             | COMMENT NEWLINE\n    a_cont : a_cont COMMA NEWLINE\n    a_cont : content\n                | a_cont COMMA a_cont\n                | a_cont COMMA NEWLINE a_cont \n    table_cont : CCHAV\n                    | t_cont CCHAV\n    t_cont : key EQUALS content\n              | t_cont COMMA key EQUALS content\n    key : KEY\n            | INTEGER\n            | STRING\n            | STRING_LITERAL\n    value : STRING\n                | BOOL\n                | NULL\n                | INTEGER\n                | FLOAT\n                | BINARY\n                | OCTAL\n                | HEXA\n                | NAN\n                | INFINITY\n                | DATE\n                | TIME\n                | DATETIME\n                | MULTILINE_STRING\n                | STRING_LITERAL\n                | MULTILINE_STRING_LITERAL\n    table : table NEWLINE COMMENT\n    table : table NEWLINE atrib\n    table : APAR tab_cont CPAR \n            | APAR tab_cont CPAR COMMENT\n    tab_cont : FLOAT\n    tab_cont : tab_cont DOT tab_cont\n                | key\n    array_table : array_table NEWLINE COMMENT\n    array_table : array_table NEWLINE atrib\n    array_table : APAR2 arr_table_cont CPAR2\n                    | APAR2 arr_table_cont CPAR2 COMMENT\n    arr_table_cont : arr_table_cont DOT arr_table_cont\n                    | key\n    '
    
_lr_action_items = {'NEWLINE':([0,3,4,5,6,7,8,9,19,22,23,24,25,26,27,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,69,70,71,72,73,76,77,79,81,82,83,85,86,89,90,91,92,93,96,97,98,100,],[5,5,-3,-5,-6,25,26,27,-4,25,26,27,-9,-10,-11,-59,-60,-66,-67,-47,-16,-20,67,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-17,-19,-61,-68,-21,-24,84,85,-32,-23,-35,-18,-62,-69,-22,-25,91,-30,-36,-33,-26,-31,-27,-29,100,-34,-28,-31,]),'FLOAT':([0,3,4,5,6,12,19,25,26,27,28,29,30,43,63,67,83,85,88,91,96,99,100,],[10,10,-3,-5,-6,32,-4,-9,10,10,40,40,10,40,32,40,40,40,40,40,40,40,40,]),'APAR':([0,3,4,5,6,19,25,26,27,28,29,43,67,83,85,88,91,96,99,100,],[12,12,-3,-5,-6,-4,-9,-10,-11,43,43,43,43,43,43,43,43,43,43,43,]),'APAR2':([0,3,4,5,6,19,25,26,27,],[13,13,-3,-5,-6,-4,-9,-10,-11,]),'KEY':([0,3,4,5,6,12,13,19,25,26,27,30,44,63,65,87,],[14,14,-3,-5,-6,14,14,-4,-9,14,14,14,14,14,14,14,]),'INTEGER':([0,3,4,5,6,12,13,19,25,26,27,28,29,30,43,44,63,65,67,83,85,87,88,91,96,99,100,],[15,15,-3,-5,-6,15,15,-4,-9,15,15,48,48,15,48,15,15,15,48,48,48,15,48,48,48,48,48,]),'STRING':([0,3,4,5,6,12,13,19,25,26,27,28,29,30,43,44,63,65,67,83,85,87,88,91,96,99,100,],[16,16,-3,-5,-6,16,16,-4,-9,16,16,45,45,16,45,16,16,16,45,45,45,16,45,45,45,45,45,]),'STRING_LITERAL':([0,3,4,5,6,12,13,19,25,26,27,28,29,30,43,44,63,65,67,83,85,87,88,91,96,99,100,],[17,17,-3,-5,-6,17,17,-4,-9,17,17,58,58,17,58,17,17,17,58,58,58,17,58,58,58,58,58,]),'$end':([1,2,3,4,5,6,18,19,20,21,22,23,24,25,26,27,36,37,38,39,40,41,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,68,72,73,76,77,79,81,82,86,90,92,98,],[0,-1,-12,-3,-5,-6,-2,-4,-7,-8,-13,-14,-15,-9,-10,-11,-59,-60,-66,-67,-47,-16,-20,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-17,-19,-61,-68,-21,-24,-23,-35,-18,-62,-69,-22,-25,-36,-26,-27,-28,]),'EQUALS':([10,11,14,15,16,17,75,94,],[28,29,-39,-40,-41,-42,88,99,]),'DOT':([11,14,15,16,17,31,32,33,34,35,78,80,],[30,-39,-40,-41,-42,63,-63,-65,65,-71,63,65,]),'CPAR':([14,15,16,17,31,32,33,40,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,66,67,68,69,71,72,73,78,81,82,83,84,85,86,89,90,91,92,93,97,98,100,],[-39,-40,-41,-42,62,-63,-65,-47,-20,68,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-21,68,-24,82,-32,-23,-35,-64,-22,-25,90,92,-30,-36,-33,-26,98,-27,-29,-34,-28,-31,]),'CPAR2':([14,15,16,17,34,35,80,],[-39,-40,-41,-42,64,-71,-70,]),'COMMENT':([26,27,40,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,64,66,67,68,72,73,81,82,83,85,86,90,91,92,96,98,100,],[36,38,-47,-20,70,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,76,77,79,-21,70,-24,-23,-35,-22,-25,70,70,-36,-26,70,-27,70,-28,70,]),'ACHAV':([28,29,43,67,83,85,88,91,96,99,100,],[44,44,44,44,44,44,44,44,44,44,44,]),'BOOL':([28,29,43,67,83,85,88,91,96,99,100,],[46,46,46,46,46,46,46,46,46,46,46,]),'NULL':([28,29,43,67,83,85,88,91,96,99,100,],[47,47,47,47,47,47,47,47,47,47,47,]),'BINARY':([28,29,43,67,83,85,88,91,96,99,100,],[49,49,49,49,49,49,49,49,49,49,49,]),'OCTAL':([28,29,43,67,83,85,88,91,96,99,100,],[50,50,50,50,50,50,50,50,50,50,50,]),'HEXA':([28,29,43,67,83,85,88,91,96,99,100,],[51,51,51,51,51,51,51,51,51,51,51,]),'NAN':([28,29,43,67,83,85,88,91,96,99,100,],[52,52,52,52,52,52,52,52,52,52,52,]),'INFINITY':([28,29,43,67,83,85,88,91,96,99,100,],[53,53,53,53,53,53,53,53,53,53,53,]),'DATE':([28,29,43,67,83,85,88,91,96,99,100,],[54,54,54,54,54,54,54,54,54,54,54,]),'TIME':([28,29,43,67,83,85,88,91,96,99,100,],[55,55,55,55,55,55,55,55,55,55,55,]),'DATETIME':([28,29,43,67,83,85,88,91,96,99,100,],[56,56,56,56,56,56,56,56,56,56,56,]),'MULTILINE_STRING':([28,29,43,67,83,85,88,91,96,99,100,],[57,57,57,57,57,57,57,57,57,57,57,]),'MULTILINE_STRING_LITERAL':([28,29,43,67,83,85,88,91,96,99,100,],[59,59,59,59,59,59,59,59,59,59,59,]),'COMMA':([40,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,66,68,69,71,72,73,74,81,82,85,86,89,90,91,92,93,95,97,98,100,101,],[-47,-20,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-21,-24,83,-32,-23,-35,87,-22,-25,-30,-36,96,-26,-31,-27,96,-37,96,-28,-31,-38,]),'CCHAV':([40,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,66,68,72,73,74,81,82,86,90,92,95,98,101,],[-47,-20,73,-43,-44,-45,-46,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-21,-24,-23,-35,86,-22,-25,-36,-26,-27,-37,-28,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'converter':([0,],[1,]),'file':([0,],[2,]),'file_lines':([0,],[3,]),'line':([0,3,],[4,19,]),'elem_newline':([0,3,],[6,6,]),'atrib':([0,3,26,27,30,],[7,22,37,39,61,]),'table':([0,3,],[8,23,]),'array_table':([0,3,],[9,24,]),'key':([0,3,12,13,26,27,30,44,63,65,87,],[11,11,33,35,11,11,11,75,33,35,94,]),'last_line':([3,],[18,]),'elem':([3,],[20,]),'empty':([3,],[21,]),'tab_cont':([12,63,],[31,78,]),'arr_table_cont':([13,65,],[34,80,]),'content':([28,29,43,67,83,85,88,91,96,99,100,],[41,60,71,71,71,71,95,71,71,101,71,]),'value':([28,29,43,67,83,85,88,91,96,99,100,],[42,42,42,42,42,42,42,42,42,42,42,]),'arr_cont':([43,67,],[66,81,]),'a_cont':([43,67,83,85,91,96,100,],[69,69,89,93,97,89,97,]),'table_cont':([44,],[72,]),'t_cont':([44,],[74,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> converter","S'",1,None,None,None),
  ('converter -> file','converter',1,'p_converter','projeto_PL_parser.py',7),
  ('file -> file_lines last_line','file',2,'p_file','projeto_PL_parser.py',14),
  ('file_lines -> line','file_lines',1,'p_file_lines','projeto_PL_parser.py',19),
  ('file_lines -> file_lines line','file_lines',2,'p_file_lines','projeto_PL_parser.py',20),
  ('line -> NEWLINE','line',1,'p_line_newline','projeto_PL_parser.py',28),
  ('line -> elem_newline','line',1,'p_line','projeto_PL_parser.py',33),
  ('last_line -> elem','last_line',1,'p_last_line','projeto_PL_parser.py',38),
  ('last_line -> empty','last_line',1,'p_last_line','projeto_PL_parser.py',39),
  ('elem_newline -> atrib NEWLINE','elem_newline',2,'p_elem_newline','projeto_PL_parser.py',44),
  ('elem_newline -> table NEWLINE','elem_newline',2,'p_elem_newline','projeto_PL_parser.py',45),
  ('elem_newline -> array_table NEWLINE','elem_newline',2,'p_elem_newline','projeto_PL_parser.py',46),
  ('empty -> <empty>','empty',0,'p_empty','projeto_PL_parser.py',51),
  ('elem -> atrib','elem',1,'p_elem','projeto_PL_parser.py',55),
  ('elem -> table','elem',1,'p_elem','projeto_PL_parser.py',56),
  ('elem -> array_table','elem',1,'p_elem','projeto_PL_parser.py',57),
  ('atrib -> FLOAT EQUALS content','atrib',3,'p_atrib_float','projeto_PL_parser.py',62),
  ('atrib -> key EQUALS content','atrib',3,'p_atrib','projeto_PL_parser.py',67),
  ('atrib -> key EQUALS content COMMENT','atrib',4,'p_atrib','projeto_PL_parser.py',68),
  ('atrib -> key DOT atrib','atrib',3,'p_atrib','projeto_PL_parser.py',69),
  ('content -> value','content',1,'p_content','projeto_PL_parser.py',74),
  ('content -> APAR arr_cont','content',2,'p_content','projeto_PL_parser.py',75),
  ('content -> APAR NEWLINE arr_cont','content',3,'p_content','projeto_PL_parser.py',76),
  ('content -> ACHAV table_cont','content',2,'p_content','projeto_PL_parser.py',77),
  ('arr_cont -> CPAR','arr_cont',1,'p_arr_cont','projeto_PL_parser.py',87),
  ('arr_cont -> a_cont CPAR','arr_cont',2,'p_arr_cont','projeto_PL_parser.py',88),
  ('arr_cont -> a_cont COMMA CPAR','arr_cont',3,'p_arr_cont','projeto_PL_parser.py',89),
  ('arr_cont -> a_cont NEWLINE CPAR','arr_cont',3,'p_arr_cont','projeto_PL_parser.py',90),
  ('arr_cont -> a_cont COMMA NEWLINE CPAR','arr_cont',4,'p_arr_cont','projeto_PL_parser.py',91),
  ('a_cont -> COMMENT NEWLINE a_cont','a_cont',3,'p_a_cont_comments','projeto_PL_parser.py',99),
  ('a_cont -> COMMENT NEWLINE','a_cont',2,'p_a_cont_comments','projeto_PL_parser.py',100),
  ('a_cont -> a_cont COMMA NEWLINE','a_cont',3,'p_a_cont_ending','projeto_PL_parser.py',108),
  ('a_cont -> content','a_cont',1,'p_a_cont','projeto_PL_parser.py',113),
  ('a_cont -> a_cont COMMA a_cont','a_cont',3,'p_a_cont','projeto_PL_parser.py',114),
  ('a_cont -> a_cont COMMA NEWLINE a_cont','a_cont',4,'p_a_cont','projeto_PL_parser.py',115),
  ('table_cont -> CCHAV','table_cont',1,'p_table_cont','projeto_PL_parser.py',125),
  ('table_cont -> t_cont CCHAV','table_cont',2,'p_table_cont','projeto_PL_parser.py',126),
  ('t_cont -> key EQUALS content','t_cont',3,'p_t_cont','projeto_PL_parser.py',134),
  ('t_cont -> t_cont COMMA key EQUALS content','t_cont',5,'p_t_cont','projeto_PL_parser.py',135),
  ('key -> KEY','key',1,'p_key','projeto_PL_parser.py',144),
  ('key -> INTEGER','key',1,'p_key','projeto_PL_parser.py',145),
  ('key -> STRING','key',1,'p_key','projeto_PL_parser.py',146),
  ('key -> STRING_LITERAL','key',1,'p_key','projeto_PL_parser.py',147),
  ('value -> STRING','value',1,'p_value','projeto_PL_parser.py',152),
  ('value -> BOOL','value',1,'p_value','projeto_PL_parser.py',153),
  ('value -> NULL','value',1,'p_value','projeto_PL_parser.py',154),
  ('value -> INTEGER','value',1,'p_value','projeto_PL_parser.py',155),
  ('value -> FLOAT','value',1,'p_value','projeto_PL_parser.py',156),
  ('value -> BINARY','value',1,'p_value','projeto_PL_parser.py',157),
  ('value -> OCTAL','value',1,'p_value','projeto_PL_parser.py',158),
  ('value -> HEXA','value',1,'p_value','projeto_PL_parser.py',159),
  ('value -> NAN','value',1,'p_value','projeto_PL_parser.py',160),
  ('value -> INFINITY','value',1,'p_value','projeto_PL_parser.py',161),
  ('value -> DATE','value',1,'p_value','projeto_PL_parser.py',162),
  ('value -> TIME','value',1,'p_value','projeto_PL_parser.py',163),
  ('value -> DATETIME','value',1,'p_value','projeto_PL_parser.py',164),
  ('value -> MULTILINE_STRING','value',1,'p_value','projeto_PL_parser.py',165),
  ('value -> STRING_LITERAL','value',1,'p_value','projeto_PL_parser.py',166),
  ('value -> MULTILINE_STRING_LITERAL','value',1,'p_value','projeto_PL_parser.py',167),
  ('table -> table NEWLINE COMMENT','table',3,'p_table_comments','projeto_PL_parser.py',172),
  ('table -> table NEWLINE atrib','table',3,'p_table_elem','projeto_PL_parser.py',177),
  ('table -> APAR tab_cont CPAR','table',3,'p_table','projeto_PL_parser.py',185),
  ('table -> APAR tab_cont CPAR COMMENT','table',4,'p_table','projeto_PL_parser.py',186),
  ('tab_cont -> FLOAT','tab_cont',1,'p_tab_cont_float','projeto_PL_parser.py',191),
  ('tab_cont -> tab_cont DOT tab_cont','tab_cont',3,'p_tab_cont','projeto_PL_parser.py',196),
  ('tab_cont -> key','tab_cont',1,'p_tab_cont','projeto_PL_parser.py',197),
  ('array_table -> array_table NEWLINE COMMENT','array_table',3,'p_array_table_comments','projeto_PL_parser.py',207),
  ('array_table -> array_table NEWLINE atrib','array_table',3,'p_array_table_elem','projeto_PL_parser.py',212),
  ('array_table -> APAR2 arr_table_cont CPAR2','array_table',3,'p_array_table','projeto_PL_parser.py',219),
  ('array_table -> APAR2 arr_table_cont CPAR2 COMMENT','array_table',4,'p_array_table','projeto_PL_parser.py',220),
  ('arr_table_cont -> arr_table_cont DOT arr_table_cont','arr_table_cont',3,'p_arr_table_cont','projeto_PL_parser.py',225),
  ('arr_table_cont -> key','arr_table_cont',1,'p_arr_table_cont','projeto_PL_parser.py',226),
]
