
from const import *

#### tokens ####
class Token:
    def __init__(self, tok_type, tok_val=None):
        self.type = tok_type
        self.value = tok_val

    def __repr__(self):
        if self.value is None:
            return f'<{self.type}>'
        else:
            return f'<{self.type} = {self.value}>'

class error:
    def __init__(self, name:str, details:str):
        self.name = name
        self.details = details

    def __repr__(self):
        return f'{self.name.upper()}: {self.details}'


#### lexer ####
class lexer:
    def __init__(self):
        self.text = None
        self.idx = -1
        self.currentChar = None
        self.tokens = []

    def getText(self, text):
        if len(self.tokens) != 0:
            self.tokens.append(Token(TT_ENDL))
        self.text = text
        self.idx = -1
        self.advance()

    def advance(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.currentChar = self.text[self.idx]
        else:
            self.currentChar = None

    def lex(self):
        # ALL functions used here that are able to have an error should return None, error(name, details)
        while self.currentChar is not None:
            if False: # placeholder
                pass
            else:
                tok, err = self.readMult()
                if err:
                    return None, err
                else: self.tokens.append(tok)
        return self.tokens, None

    def readMult(self):
        firstChar = self.currentChar
        tok_str = ''
        while self.currentChar not in (' ', '\n', '\t', '(', ')', '{', '}', '[', ']', '<', '>', None):
            tok_str += self.currentChar
            self.advance()
        self.advance()
        if tok_str in longNameTT:
            if not self.idx + 2 > len(self.text):
                if self.text[self.idx + 2] == '=':
                    return None, error('syntaxError', 'attempted reassignment of base keyword')
                else:
                    return Token(longNameTT[tok_str]), None

        elif tok_str in shortNameTT:
            return Token(shortNameTT[tok_str]), None

        elif firstChar in DIGITS:
            if '.' in tok_str:
                dots = 0
                for ii in tok_str:
                    if ii == '.':
                        dots += 1
                if dots > 1:
                    return None, error('syntaxError', 'unexpected \'.\' in number')
                else: return Token(TT_FLOAT, float(tok_str)), None
            else: return Token(TT_INT, int(tok_str)), None

        else: return None, error('syntaxError', f'unknown symbol \'{tok_str}\'')
