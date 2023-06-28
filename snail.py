from itertools import chain


def coil(nxn:list, x:list) -> tuple:
    if not nxn:
        return ()
    rows = list(map(tuple, nxn))
    r = rows.pop(0) if rows else ()
    columns = list(zip(*rows))[::-1]
    c = columns.pop(0) if columns else ()
    x.append(r)
    x.append(c)
    mxm = list(zip(*columns))[::-1]
    return coil(mxm, x)


def get_snail_values(nxn):
    x= []
    coil(nxn, x)
    return list(chain(*x))

def main():
    #nxn = [[1, 2, 3, 1], [4, 5, 6, 2], [7, 8, 9, 3], [4, 5, 6, 7]]
    nxn = [[1, 2, 3, 4, 1], [5, 6, 7, 8, 2], [9, 1, 2, 3, 3], [4, 5, 6, 7, 4], [5, 6, 7, 8, 9]]
    print(get_snail_values(nxn))
    
if __name__ == '__main__':
    main()
