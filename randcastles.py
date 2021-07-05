
from random import randint

width = 200
view = 5
life = 5

def lifereq(view,lifemn=2,lifemx=2):
    return ( sum(view) >= lifemn
            and sum(view) <= lifemx )


def it(foo,down = 5, up = 5,lifemn=3,lifemx=3):
    newfoo = [0]*len(foo)
    for i in range(len(foo)):
        start = max(0,i-down)
        end = min(len(foo),i+1+up)
        if lifereq(foo[start:end],lifemn=lifemn,lifemx=lifemx):
            newfoo[i] = 1
    return newfoo

def makeit(foo,down = 5,up=5,lifemn=3,lifemx=3):
    randcastle = []
    for i in range(500):
    #while True:
        randcastle += [foo]
        newfoo = it(foo,down=down,up=up,lifemn=lifemn,lifemx=lifemx)
        if newfoo == foo:
            break
        foo = newfoo

    return randcastle

def draw(randcastle):
    drawing = ""
    for line in reversed(randcastle):
        drawing+= "".join("#" if x else " " for x in line)
        drawing+= "\n"
    return drawing

if __name__ == "__main__":
    view = randint(1,12)
    life1 = randint(2,view*2+1)
    life2 = randint(2,view*2+1)
    lifemn = min((life1,life2))
    lifemx = max((life1,life2))
    print(f"V: {view*2+1}  Lmn: {lifemn}  Lmx: {lifemx}")
    foo = list(randint(0,1) for _ in range(width))
    rc = makeit(foo,down = view, up = view, lifemn = lifemn, lifemx=lifemx)
    dr = draw(rc)
    print(dr)
