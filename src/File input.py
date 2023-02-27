import lexer as lexx

def main():
    path = input('path to file: ')
    try:
        file = open(path, 'rt')
    except FileNotFoundError:
        print('invalid file path\n')
        return main()
    lexer = lexx.lexer()
    lines = file.readlines()
    for ii in lines:
        lexer.getInput(ii, path)
        tokens, err = lexer.lex()
        if err: print(err)
    print(lexer.tokens)


if __name__ == '__main__':
    main()