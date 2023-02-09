import lexer
def main():
    lex = lexer.lexer()
    while True:
        Input = input('cross  <> ')
        if Input == 'quit()':
            return
        else:
            lex.getText(Input)
            tok, err = lex.lex()
            if err: print(err)
            else: print(tok)


if __name__ == '__main__':
    main()
