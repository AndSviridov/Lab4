from random import randint

def letter():
    return chr(randint(65, 90))

def number():
    return chr(randint(48, 57))

def block():
    block = ''
    numb = randint(0, 3)
    for i in range(0, 4):
        if i == numb: block = block + number()
        else: block = block + letter()
    return block

def key():
    return block() + '-' + block() + '-' + block() + '-' + block()
