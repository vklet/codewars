import re

def insert_line_break(m, pos:int) -> str:
    nl = '\n'
    return f'nl{m.group()}' if m.span()[0] >= pos else m.group()

def justify(text:str, width:int):
    bounds = [i for i in range(0, len(text), width)]

    spl = [text.rfind(' ', bounds[i-1], bounds[i]) for i in range(1, len(bounds))]

    #t = re.sub('')
    return spl


print(justify('123 45 6', 7))
