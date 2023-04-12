import ply.lex as lex

#states = (
#    ('o_list', 'inclusive'),
#    ('c_list', 'inclusive'),
#    ('o_table', 'inclusive'),
#    ('c_table', 'inclusive'),
#)

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
    'TAG_NAME'
)

t_EQUALS = r'='

def t_COMMENT(t):
    r'\#.+'
    pass

def t_VALUE(t):
    r'".+"'
    return t

def t_NUMERIC(t):
    r'(\+|-)?\d+\.?\d*'
    return t

def t_KEY(t):
    r'\w+'

    if t.value in ["true", "false"]:
        t.type = 'BOOL'
    elif t.value == 'null':
        t.type = 'NULL'

    return t    

t_ignore = ' \n\t\r'

def t_error(t):
    print(f"Caracter inválido {t.value[0]}")
    t.lexer.skip(1)

data = """
# This is a TOML document.

title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00 # First class dates

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
"""

lexer = lex.lex()
lexer.input(data)

while tok := lexer.token():
    print(tok)