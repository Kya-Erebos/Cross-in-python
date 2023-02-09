DIGITS = '0123456789'
#### tok_types ####
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'

TT_CHAR = 'CHAR'

TT_BOOL = 'BOOL'
TT_TRUE = 'TRUE'
TT_FALSE = 'FALSE'
TT_NONE = 'NONE'
TT_NULL = 'Null'

TT_ARRAY = 'ARRAY'
TT_DICT = 'DICT'
TT_OBJECT = 'OBJECT'

TT_PLUS = '+'
TT_MINUS = '-'
TT_STAR = '*'  # named weird due to being used for wildcard, pointers, and arithmatic
TT_SLASH = '/'  # (also possibly more)
TT_EQ = '='

TT_LOGIC_LEQ = '=='
TT_LOGIC_NEQ = '!='
TT_LOGIC_LT = '<'
TT_LOGIC_GT = '>'
TT_LOGIC_EQL = '<='
TT_LOGIC_EQG = '>='

TT_ENDL = 'endl'

TT_AS = 'as'
TT_PUBLIC = 'public'
TT_PRIVATE = 'private'
TT_STATIC = 'static'
TT_CLASS = 'class'
TT_VAR = 'var'
TT_FUNC = 'func'
TT_DEFARROW = '=>'
TT_DEF = 'def'
TT_PASS = 'pass'


####groups####

longNameTT = { # for readMult() in lexer
    'as' : TT_AS,
    'public' : TT_PUBLIC,
    'private' : TT_PRIVATE,
    'static' : TT_STATIC,
    'class' : TT_CLASS,
    'var' : TT_VAR,
    'func' : TT_FUNC,
    '=>' : TT_DEFARROW,
    'def' : TT_DEF,
    'pass' : TT_PASS,
    '<=': TT_LOGIC_EQL,
    '>=': TT_LOGIC_EQG,
    '==': TT_LOGIC_LEQ,
    '!=': TT_LOGIC_NEQ
}

shortNameTT = {
    '<': TT_LOGIC_LT,
    '>': TT_LOGIC_GT,
    '+': TT_PLUS,
    '-': TT_MINUS,
    '*': TT_STAR ,
    '/': TT_SLASH,
    '=': TT_EQ
}

varTypes = {
    'INT': TT_INT,
    'FLOAT': TT_FLOAT,
    'CHAR': TT_CHAR,
    'BOOL': TT_BOOL,
    'TRUE': TT_TRUE,
    'FALSE': TT_FALSE,
    'NONE': TT_NONE,
    'Null': TT_NULL,
    'ARRAY': TT_ARRAY,
    'DICT': TT_DICT,
    'OBJECT': TT_OBJECT
}