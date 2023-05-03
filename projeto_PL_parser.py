import json
import ply.yacc as yacc
from projeto_PL_tokenizer import tokens
import utils

def p_converter(p):
    'converter : atribs'
    p[0] = dict()
    for d in p[1]:
        p[0].update(d)

def p_atribs(p):
    '''atribs : atribs atrib
                | atrib
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_atrib(p):
    'atrib : KEY EQUALS content'
    p[0] = {p[1] : p[3]}

def p_content(p):
    '''content : value
                | APAR arr_cont
                | ACHAV table_cont
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_arr_cont(p):
    '''arr_cont : CPAR
                | a_cont CPAR
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1]

def p_a_cont(p):
    '''a_cont : content
                | a_cont COMMA content
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_table_cont(p):
    '''table_cont : CCHAV
                    | t_cont CCHAV
    '''
    if len(p) == 2:
        p[0] = {}
    else:
        p[0] = p[1]

def p_t_cont(p):
    '''t_cont : KEY EQUALS t_value
              | t_cont COMMA KEY EQUALS t_value
    '''
    if len(p) == 4:
        p[0] = {p[1] : p[3]}
    else:
        p[1].update({p[3] : p[5]})
        p[0] = p[1]


def p_t_value(p):
    ''' t_value : value
                | APAR arr_cont
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[2]

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

print(myjson)

with open('output.json', 'w') as f:
    json.dump(myjson, f, indent=4, separators=(',', ': '), ensure_ascii=False)