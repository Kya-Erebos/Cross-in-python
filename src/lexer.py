
class token:
    def __init__(self, type, val=None):
        self.type = type
        self.val = val

    def __repr__(self):
        if self.val is not None:
            return f'<{self.type} = {self.val}>'
        return f'<{self.type}>'

class lexer:
    def __init__(self):
        self.text = ''
        self.idx = -1
        self.row = 0
        self.col = -1
        self.currentChar = None
        self.tokens = []

    def getInput(self, text:str):
        self.text = text
        self.idx = -1
        self.col = -1
        self.advance()

    def advance(self):
        self.idx += 1
        if self.idx < len(self.text): self.currentChar = self.text[self.idx]
        else: self.currentChar = None

        if self.currentChar is None:
            self.col += 1
            self.row = -1
        else: self.row += 1

    def lex(self):

        while self.currentChar is not None:
            if self.currentChar in ['\t', '\n', ' ']:
                self.advance()

            elif self.currentChar == ';':
                self.tokens.append(token(';'))
                self.advance()

            else:
                tok, err = self.readMult()
                if err: return None, err
                else: self.tokens.append(tok)
        return self.tokens, None

    def readMult(self):
        tok_str = ''
        FirstChar = True
        exemptList = ['\t', ' ', '\n', ';',
                      '<', '>', '(', ')', '{', '}', '[', ']',
                      '|', '\\', '.', ',', None]
        while self.currentChar not in exemptList:
            tok_str += self.currentChar
            if (self.currentChar in '0123456789') and FirstChar:
                exemptList.remove('.')
            FirstChar = False
            self.advance()

        if tok_str[0] in '0123456789':
            if '.' in tok_str:
                try: return token(float, float(tok_str)), None
                except ValueError: return None, f'Error: illegal string \'{tok_str}\''
            else:
                try: return token(int, int(tok_str)), None
                except ValueError: return None, f'Error: cannot have variable name \'{tok_str}\''

        elif len(tok_str) == 1:
            if tok_str in '+-*/%':
                return token(tok_str), None
            else:
                return None, f'Error: illegal CHR \'{tok_str}\''
        else: return None, f'Error: illegal STR \'{tok_str}\''
