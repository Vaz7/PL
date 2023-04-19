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
    r'\"[\sa-zA-Z0-9_.-]+\"|[a-zA-Z_-][a-zA-Z_\-0-9]*(\.\".+\"|\.[a-zA-Z_0-9\-]+)*' # Podemos ter que rever está expressão regular!
    if t.value[0] != '\"':
        t.type = 'KEY'
    return t

def t_DATETIME(t):
    r'\d+-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(-\d{2}:\d{2}|\w+)?'
    return t

def t_DATE(t):
    r'\d+-\d{2}-\d{2}'
    return t

def t_TIME(t):
    r'\d{2}:\d{2}:\d{2}(-\d{2}:\d{2}|\w+)?'
    return t

def t_NUMERIC(t):
    r'(\+|-)?\d+\.?\d*'
    return t

t_ANY_ignore = ' \n\t\r'

def t_ANY_error(t):
    print(f"Caracter inválido {t.value[0]}")
    t.lexer.skip(1)

data = """
# This is a TOML document.

title = "TOML Example"
[1]
testing = [2001-01-20]

["owner"]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First class dates
deb = 1979-05-27
dab = 07:32:00UC

[database]
server = "192.168.1.1"
ports = [ 8000, 8001, 8002 ]
connection_max = 5000
enabled = true
type = null
sl = '  string literal'

[servers]

  # Indentation (tabs and/or spaces) is allowed but not required
  [servers."alpha"."delta"]
  ip = "10.0.0.1"
  dc = "eqdc10"
  inf = +infinity
  n = -nan

  [servers.beta]
  ip = "10.0.0.2"
  dc = "eqdc10"

[clients]
data = [ ["gamma", "delta"], [1, 2] ]

# Line breaks are OK when inside arrays
hosts = [
  "alpha",
  "omega"
]

inline = { test = "test", more = "more", name = null }

[[fruit]]
name = "potato"
flavour = 10
"""

lexer = lex.lex()
lexer.input(data)

while tok := lexer.token():
    print(tok)