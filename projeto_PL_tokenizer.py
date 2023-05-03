import ply.lex as lex
import utils

multiline_string_literal = ""
multiline_string = ""

states = (
    ('multilineLiteral', 'exclusive'),
    ('multilineString', 'exclusive'),
)

tokens = (
    'KEY',
    'EQUALS',
    'BOOL',
    'NULL',
    'INTEGER',
    'FLOAT',
    'BINARY',
    'OCTAL',
    'HEXA',
    'NAN',
    'INFINITY',
    'APAR',
    'CPAR',
    'APAR2',
    'CPAR2',
    'COMMA',
    'DATE',
    'TIME',
    'DATETIME',
    'STRING',  
    'MULTILINE_STRING',
    'STRING_LITERAL',
    'MULTILINE_STRING_LITERAL',
    'ACHAV',
    'CCHAV'
)

t_EQUALS = r'='
t_COMMA = r','
t_APAR = r'\['
t_CPAR = r'\]'
t_APAR2 = r'\[\['
t_CPAR2 = r'\]\]'
t_ACHAV = r'\{'
t_CCHAV = r'\}'
t_MULTILINE_STRING_LITERAL = r"\'\'\'\'\'\'"
t_MULTILINE_STRING = r'\"\"\"\"\"\"'

def t_MULTILINE_STRING_open(t):
    r'\"\"\"'
    t.lexer.push_state('multilineString')

def t_multilineString_leave(t):
    r'\"\"\"'
    global multiline_string
    t.value = utils.set_up_multiline_string(multiline_string.strip('\n'))
    multiline_string = ""
    t.type = "MULTILINE_STRING"
    t.lexer.pop_state()
    return t

def t_multilineString_MULTILINE_STRING(t):
    r'(.|\n)+?'
    global multiline_string
    multiline_string = multiline_string + str(t.value)

def t_MULTILINE_STRING_LITERAL_open(t):
    r"\'\'\'"
    t.lexer.push_state('multilineLiteral')

def t_multilineLiteral_leave(t):
    r"\'\'\'"
    global multiline_string_literal
    t.value = multiline_string_literal.strip('\n')
    multiline_string_literal = ""
    t.type = "MULTILINE_STRING_LITERAL"
    t.lexer.pop_state()
    return t

def t_multilineLiteral_MULTILINE_STRING_LITERAL(t):
    r'(.|\n)+?'
    global multiline_string_literal
    multiline_string_literal = multiline_string_literal + str(t.value)

def t_COMMENT(t):
    r'\#.+'
    pass

def t_BOOL(t):
    r'true|false'
    return t

def t_NULL(t):
    r'null'
    return t

def t_NAN(t):
    r'(\+|-)?nan'
    return t

def t_INFINITY(t):
    r'(\+|-)?infinity'
    return t

def t_STRING_LITERAL(t):
    r"'[^']*'"
    return t

def t_STRING(t):
    r'(("[^"\\]*(\\.[^"\\]*)*"|\\".+\\")|[a-zA-Z_-][a-zA-Z_\-0-9]*)+(\.("[^"\\]*(\\.[^"\\]*)*"|\\".+\\")|\.[a-zA-Z_0-9\-]+)*'
    if t.value[0] != '\"':
        t.type = 'KEY'
        if not utils.validKey(t.value):
            raise SyntaxError(f"KEY {t.value} é inválida")
    else:
        t.value = t.value[1:-1]
    return t

def t_DATETIME(t):
    r'\d+-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?([\+|-]\d{2}:\d{2})?[zZ]?'
    if not utils.validDateTime(t.value): 
        raise SyntaxError(f"Datetime {t.value} é inválido")
    return t

def t_DATE(t):
    r'\d+-\d{2}-\d{2}'
    if not utils.validDate(t.value): 
        raise SyntaxError(f"Data {t.value} é inválida")
    return t

def t_TIME(t):
    r'\d{2}:\d{2}:\d{2}(\.\d+)?([\+|-]\d{2}:\d{2})?[zZ]?'
    if not utils.validTime(t.value):
        raise SyntaxError(f"Time {t.value} é inválido")
    return t

def t_BINARY(t):
    r'0[b|B][01]+'
    return t

def t_OCTAL(t):
    r'0[o|O][0-7]+'
    return t;

def t_HEXA(t):
    r'0[x|X][0-15A-F]+'
    return t;

def t_FLOAT(t):
    r'(\+|-)?\d+(_\d+)*\.(\d+(_\d+)*)?([eE](\+|-)?\d+)?'
    t.value = t.value.replace('_','')
    return t

def t_INTEGER(t):
    r'(\+|-)?\d+(_\d+)*([eE](\+|-)?\d+)?'
    t.value = t.value.replace('_','')
    return t

t_ignore = ' \n\t\r'
t_multilineLiteral_ignore = ''
t_multilineString_ignore = ''

def t_ANY_error(t):
    print(f"Caracter inválido {t.value[0]}")
    t.lexer.skip(1)

#data = None
#
#with open('parse_file.toml') as file:
#    data = file.read()

lexer = lex.lex()
#lexer.input(data)
#
#while True:
#    try:
#        tok = lexer.token()
#
#        if not tok:
#            break
#        
#        print(tok)
#    except SyntaxError as e:
#        print(f"Erro: {str(e)}")
