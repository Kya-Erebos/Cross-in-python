import lexer as lexx
def main():
    lexer = lexx.lexer()

    while True:
        text = input('Cross <> ')
        if text == 'quit':
            return
        else:
            lexer.getInput(text)
            tokens, err = lexer.lex()
            if err: print(err)
            else: print(tokens)


if __name__ == '__main__':
    main()
