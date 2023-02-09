def mayor(numero1:int, numero2:int)->int | None:
    result = 0
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2
    else:
        result = None
    return result

def test_mayor1():
    assert mayor(2,1) == 2

def test_mayor2():
    assert mayor(1,2) == 2

def test_mayor3():
    assert mayor(2,2) == None
