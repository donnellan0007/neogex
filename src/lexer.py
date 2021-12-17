"""

Take a string and return a list of tokens.

For example: "TEXT with MIN 8 CHAR" -> ['TEXT', 'with', 'MIN', '8', 'CHAR']

"""

TOKENS = (
    'TEXT',
    'MIN',
    'MAX',
    'CHAR',
    'and',
    'or',
    'not',
    'includes',
    'with',
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
        if i == ' ':
            token = []
        token_ = ("").join(token)
        token_ = token_.strip()
        """ 
        check if token_ is a number, as numbers are tokens.
        ideally, this will be consolidated into a if statement
        """
        # check if character after token is a double space
        if token_.isdigit():
            tokens.append(token_)
            # print("Token: " + ("").join(token))
        else:
            if token_ in TOKENS:
                tokens.append(token_)
                # print("Token: " + ("").join(token))

    return tokens

# print(lex("TEXT with MIN 8 CHAR and MAX 20 CHAR and includes[1:] {'@', '#'}"))
# print(lex("TEXT with MIN 8 CHAR and MAX 9 CHAR"))

def parser(tokens):
    """
    Takes a list of tokens and returns a list of parsed tokens.
    """
    parsed = []
    for i in tokens:
        if i in TOKENS:
            parsed.append(i)
        elif i in HELPERS:
            parsed.append(i)
        else:
            parsed.append(int(i))
    return parsed

def parsing(tokens):

    counter = 0
    elem_pos = {}

    if tokens[0] == 'TEXT':
        for i in tokens:
            counter = counter + 1
            elem_pos[counter] = i
        print(elem_pos)


print(parsing(lex("TEXT with MIN 8 CHAR and MAX 9 CHAR")))