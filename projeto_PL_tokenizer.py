import ply.lex as lex
import re
import datetime

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

def validDate(data):
    data_separada = data.split('-')
    if len(data_separada) != 3:
        return False  # invalid format, must have exactly 3 parts separated by hyphens
    try:
        year = int(data_separada[0])
        month = int(data_separada[1])
        day = int(data_separada[2])
    except ValueError:
        return False  # could not convert parts to integers, invalid format
    # check if year, month, and day are within valid ranges
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        return False  # invalid values for year, month, or day
    # check for valid number of days for the given month and year
    if month in [4, 6, 9, 11] and day > 30:
        return False  # April, June, September, and November have 30 days
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False  # leap year has 29 days in February
        else:
            if day > 28:
                return False  # non-leap year has 28 days in February
    return True  # valid date


def validDateTime(datetime_str):
    try:
        # split datetime string into its components
        date_str, time_str = datetime_str.split('T')
        year_str, month_str, day_str = date_str.split('-')

        offset = re.split(r'\+|-|z|z', time_str)
        hour_str, minute_str, second_str = offset[0].split(':')
        second_parts = second_str.split('.')
        second_int = int(second_parts[0])
        microsecond_int = int(second_parts[1]) if len(second_parts) > 1 else 0

        if len(offset) == 3 or len(offset) == 2 and offset[1] != '':
            offset_hour, offset_min = offset[1].split(':')
            offset_hour = int(offset_hour)
            offset_min = int(offset_min)

            if offset_hour < 0 or offset_hour > 24 or offset_min < 0 or offset_min > 59:
                return False

        # parse date and time components into datetime object
        dt = datetime.datetime(
            year=int(year_str), month=int(month_str), day=int(day_str),
            hour=int(hour_str), minute=int(minute_str), second=second_int,
            microsecond=microsecond_int
        )

        return True  # valid datetime

    except (ValueError, IndexError):
        return False  # invalid datetime format





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
    if not validDateTime(t.value): raise SyntaxError(f"Datetime {t.value} é inválido")
    return t

def t_DATE(t):
    r'\d+-\d{2}-\d{2}'
    if not validDate(t.value): raise SyntaxError(f"Data {t.value} é inválida")
    return t

def t_TIME(t):
    r'\d{2}:\d{2}:\d{2}(\.\d+)?([\+|-]\d{2}:\d{2})?[zZ]?'
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




def t_NUMERIC(t):
    #r'(\+|-)?\d+\.?\d*'
    r'(\+|-)?\d+(_\d+)*(\.\d+(_\d+)*)?([eE](\+|-)?\d+)?'
    t.value = t.value.replace('_','')
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


while True:
    try:
        tok = lexer.token()

        if not tok:
            break
        
        print(tok)
    except SyntaxError as e:
        print(f"Error : {str(e)}")
