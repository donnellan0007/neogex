"""

Take a string and return a list of tokens.

For example: "TEXT with MIN 8 CHAR" -> ['TEXT', 'with', 'MIN', '8', 'CHAR']

"""

TOKENS = (
    'TEXT',
    'MIN',
    'MAX',
    'CHAR',    
)

HELPERS = (
    'and',
    'or',
    'not',
    'in',
    'with',
)

def lex(string):
    token = []
    tokens = []
    for i in string:
        # If the character is a space, then we have reached the end of a token.
        token.append(i)
        if i == ' ' or i == '':
            token = []
        token_ = ("").join(token)
        token_ = token_.strip()
        """ 
        check if token_ is a number, as numbers are tokens.
        ideally, this will be consolidated into a if statement
        """
        if token_.isdigit():
            tokens.append(token_)
            print("Token: " + ("").join(token))
        else:
            if token_ in TOKENS:
                tokens.append(token_)
                print("Token: " + ("").join(token))

    return tokens

print(lex("TEXT with MIN 8 CHAR and MAX 10 CHAR"))