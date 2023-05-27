import json
import ply.yacc as yacc
from projeto_PL_tokenizer import tokens
import utils

def p_converter(p):
    '''converter : file
    '''
    p[0] = dict()
    for d in p[1]:
        p[0] = utils.merge_elems(p[0], d)

def p_file(p):
    '''file : file_lines last_line
    '''
    p[0] = p[1] + p[2]

def p_file_lines(p):
    '''file_lines : line
             | file_lines line
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_line_newline(p):
    '''line : NEWLINE
    '''
    p[0] = []

def p_line(p):
    '''line : elem_newline
    '''
    p[0] = p[1]

def p_last_line(p):
    '''last_line : elem
                 | empty
    '''
    p[0] = p[1]

def p_elem_newline(p):
    '''elem_newline : atrib NEWLINE 
                    | table NEWLINE 
                    | array_table NEWLINE 
    '''
    p[0] = [p[1]]

def p_empty(p):
    '''empty :'''
    p[0] = []

def p_elem(p):
    '''elem : atrib
            | table
            | array_table
    '''
    p[0] = [p[1]]

def p_atrib_float(p):
    '''atrib : FLOAT EQUALS content
    '''
    p[0] = utils.build_dict(p[1], p[3])

def p_atrib(p):
    '''atrib : key EQUALS content
            | key EQUALS content COMMENT
            | key DOT atrib
    '''
    p[0] = {p[1] : p[3]}

def p_content(p):
    '''content : value
                | APAR arr_cont
                | APAR NEWLINE arr_cont
                | ACHAV table_cont
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[3]
    else:
        p[0] = p[2]

def p_arr_cont(p):
    '''arr_cont : CPAR
                | a_cont CPAR
                | a_cont COMMA CPAR
                | a_cont NEWLINE CPAR
                | a_cont COMMA NEWLINE CPAR
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1]

def p_a_cont_comments(p):
    '''a_cont : COMMENT NEWLINE a_cont
             | COMMENT NEWLINE
    '''
    if len(p) == 4:
        p[0] = p[3]
    else:
        p[0] = []

def p_a_cont_ending(p):
    '''a_cont : a_cont COMMA NEWLINE
    '''
    p[0] = p[1]

def p_a_cont(p):
    '''a_cont : content
                | a_cont COMMA a_cont
                | a_cont COMMA NEWLINE a_cont 
    '''
    if len(p) == 2: 
        p[0] = [p[1]]
    elif len(p) == 5:
        p[0] = p[1] + p[4]
    else:
        p[0] = p[1] + p[3]

def p_table_cont(p):
    '''table_cont : CCHAV
                    | t_cont CCHAV
    '''
    if len(p) == 2:
        p[0] = {}
    else:
        p[0] = p[1]

def p_t_cont(p):
    '''t_cont : key EQUALS content
              | t_cont COMMA key EQUALS content
    '''
    if len(p) == 4:
        p[0] = {p[1] : p[3]}
    else:
        p[1].update({p[3] : p[5]})
        p[0] = p[1]

def p_key(p):
    '''key : KEY
            | INTEGER
            | STRING
            | STRING_LITERAL
    '''
    p[0] = p[1]

def p_value(p):
    '''value : STRING
                | BOOL
                | NULL
                | INTEGER
                | FLOAT
                | BINARY
                | OCTAL
                | HEXA
                | NAN
                | INFINITY
                | DATE
                | TIME
                | DATETIME
                | MULTILINE_STRING
                | STRING_LITERAL
                | MULTILINE_STRING_LITERAL
    '''
    p[0] = p[1]

def p_table_comments(p):
    '''table : table NEWLINE COMMENT
    '''
    p[0] = p[1]

def p_table_elem(p):
    '''table : table NEWLINE atrib
    '''
    key = next(iter(p[3]))
    utils.add_to_dict_chain(p[1], key, p[3][key])
    p[0] = p[1]

def p_table(p):
    '''table : APAR tab_cont CPAR 
            | APAR tab_cont CPAR COMMENT
    '''
    p[0] = p[2]

def p_tab_cont_float(p):
    '''tab_cont : FLOAT
    '''
    p[0] = utils.build_dict(p[1], {})

def p_tab_cont(p):
    '''tab_cont : tab_cont DOT tab_cont
                | key
    '''
    if len(p) == 4:
        key = next(iter(p[3])) 
        utils.add_to_dict_chain(p[1], key, p[3][key])
        p[0] = p[1]
    else:
        p[0] = {p[1] : {}}

def p_array_table_comments(p):
    '''array_table : array_table NEWLINE COMMENT
    '''
    p[0] = p[1]

def p_array_table_elem(p):
    '''array_table : array_table NEWLINE atrib
    '''
    key = next(iter(p[3]))
    utils.add_to_array_chain(list(p[1].values())[-1][-1], key, p[3][key])
    p[0] = p[1]

def p_array_table(p):
    '''array_table : APAR2 arr_table_cont CPAR2
                    | APAR2 arr_table_cont CPAR2 COMMENT
    '''
    p[0] = p[2]

def p_arr_table_cont(p):
    '''arr_table_cont : arr_table_cont DOT arr_table_cont
                    | key
    '''
    if len(p) == 4:
        key = next(iter(p[3]))
        utils.add_to_array_chain(list(p[1].values())[-1][-1], key, p[3][key])
        p[0] = p[1]
    else:
        p[0] = {p[1] : [dict()]}

def p_error(p):

    # get formatted representation of stack
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

    print('Syntax error in input! Parser State:{} {} . {}'
          .format(parser.state,
                  stack_state_str,
                  p))

parser = yacc.yacc()

data = None

with open('parse_file.toml') as file:
    data = file.read()

myjson = parser.parse(data, debug=0)

with open('output.json', 'w') as f:
    json.dump(myjson, f, indent=4, separators=(',', ': '), ensure_ascii=False)