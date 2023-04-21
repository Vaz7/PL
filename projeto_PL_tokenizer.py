import ply.lex as lex

tokens = (
    'KEY',
    'EQUALS',
    'BOOL',
    'NULL',
    'NUMERIC', # TODO: Partir isto em vários tipos de números (tipo REAL, INTEGER, SCIENTIFIC). Posso fazer tudo dentro da mesma func tho (pensar se vale a pena)
    #'INTEGER',
    #'FLOAT',
    #'SCIENTIFIC_NOTATION',
    #'BINARY',
    #'OCTAL',
    #'HEXA',
    'NAN',
    'INFINITY',
    'APAR',
    'CPAR',
    'APAR2',
    'CPAR2',
    'COMMA',
    'DATE',
    'TIME',         # TODO: Ver documentação do toml (tenho de trocar umas coisas no último parâmetro do tempo, mas não é nada difícl de fazer)
    'DATETIME',
    'STRING',  
    #'MULTILINE_STRING,
    'STRING_LITERAL',              # TODO: Fazer 2 estados para conseguir retirar os tokens de strings multiline (ver exercícios dos comentários das fichas PL)
    #'MULTILINE_STRING_LITERAL',
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
    r"'[\sa-zA-Z0-9_.-]+'"
    return t

def t_STRING(t):
    r'(("[^"\\]*(\\.[^"\\]*)*"|\\".+\\")|[a-zA-Z_-][a-zA-Z_\-0-9]*)+(\.("[^"\\]*(\\.[^"\\]*)*"|\\".+\\")|\.[a-zA-Z_0-9\-]+)*' # Podemos ter que rever está expressão regular!
    if t.value[0] != '\"':
        t.type = 'KEY'
    return t

def t_DATETIME(t):
    r'\d+-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?([\+|-]\d{2}:\d{2})?[zZ]?'
    return t

def t_DATE(t):
    r'\d+-\d{2}-\d{2}'
    return t

def t_TIME(t):
    r'\d{2}:\d{2}:\d{2}(\.\d+)?([\+|-]\d{2}:\d{2})?[zZ]?'
    return t

def t_NUMERIC(t):
    r'(\+|-)?\d+\.?\d*'
    return t

t_ANY_ignore = ' \n\t\r'

def t_ANY_error(t):
    print(f"Caracter inválido {t.value[0]}")
    t.lexer.skip(1)

data = None

with open('test_file.toml') as file:
    data = file.read()

lexer = lex.lex()
lexer.input(data)

while tok := lexer.token():
    print(tok)
