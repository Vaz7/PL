import ply.lex as lex

states = (
    ('olist', 'inclusive'),
    ('otable', 'inclusive'),
)

tokens = (
    'KEY',
    'VALUE',
    'EQUALS',
    'BOOL',
    'NULL',
    'NUMERIC',
    'APAR',
    'CPAR',
    'APAR2',
    'CPAR2',
    'TAG_NAME',
    'COMMA',
    'DATE',
    'TIME',
    'DATETIME'
)

t_EQUALS = r'='
t_COMMA = r','

def t_COMMENT(t):
    r'\#.+'
    pass

def t_ANY_VALUE(t):
    r'\".+\"'
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

def t_ANY_NUMERIC(t):
    r'(\+|-)?\d+\.?\d*'
    return t

def t_KEY(t):
    r'\w+'

    if t.value in ["true", "false"]:
        t.type = 'BOOL'
    elif t.value == 'null':
        t.type = 'NULL'

    return t    

def t_APAR2(t):
    r'\[\['
    t.lexer.push_state('otable')
    return t

def t_APAR(t):
    r'\['
    t.lexer.push_state('olist')
    return t

def t_otable_CPAR2(t):
    r'\]\]'
    t.lexer.pop_state()
    return t

def t_olist_CPAR(t):
    r'\]'
    t.lexer.pop_state()
    return t

def t_olist_otable_TAG_NAME(t):
    r'([a-zA-Z0-9_.]+|\"[^\"]+\")'
    return t

t_ANY_ignore = ' \n\t\r'

def t_ANY_error(t):
    print(f"Caracter inválido {t.value[0]}")
    t.lexer.skip(1)

data = """
# This is a TOML document.

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First class dates
deb = 1979-05-27
dab = 07:32:00UC

[database]
server = "192.168.1.1"
ports = [ 8000, 8001, 8002 ]
connection_max = 5000
enabled = true

[servers]

  # Indentation (tabs and/or spaces) is allowed but not required
  [servers.alpha]
  ip = "10.0.0.1"
  dc = "eqdc10"

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

[[fruit]]
name = "potato"
flavour = 10
"""

lexer = lex.lex()
lexer.input(data)

while tok := lexer.token():
    print(tok)