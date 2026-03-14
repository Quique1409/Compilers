import re

#Define tokens for regular expressions
tokens =[
    ('Keyword', r'\b(print|printf|int)\b'),
    ('Constant', r'"[^"]*"|\d+'),
    ('Identifier', r'[a-zA-Z_]\w*'),
    ('Operator', r'[+\-*/=]'),
    ('Punctuation', r'[();$]'),
    ('Space',r'\s+'),
    ('Ignore', r'.')
]

#
def lexer(text, tokens):
    pos = 0
    result = []
    while pos < len(text):
        match = None
        for token in tokens:
            type, patron = token
            regex = re.compile(patron)
            match = regex.match(text, pos)
            if match:
                value = match.group(0)
                if type != 'Ignore' and type != 'Space':
                    result.append(type)
                break
        if not match:
            print("Invalid character:", text[pos])
            pos +=1
        else:
            pos = match.end(0)
    return result

examples = [
    'pŕintf("This is an example");',
    'int $a=1$;'
]

for i, text in enumerate(examples, 1):
    print(f"Evaluating input {i}")
    print(f"Input: {text}")
    
    result = lexer(text, tokens)

    print(" ".join(result))
    print(f"Totalñ Tokens: {len(result)}\n")