from itertools import combinations, chain, permutations
import numpy as np

def get_pins(observed:str):# -> list:

    keypad = np.vstack([np.arange(1,10).reshape((3,3)), (np.nan, 0, np.nan)])

    def get_index_range(cell:int, incl:bool=False) -> tuple:
        ub = 4 if incl else 3
        return tuple(filter(lambda c: 0 <= c < ub, (cell-1, cell, cell+1)))
  
    def get_deviations(n:int) -> str:
        row, column = map(int, np.where(keypad == n))
        rows = get_index_range(row, True)
        columns = get_index_range(column)
        deviations = list(filter(lambda x: not np.isnan(x), [keypad[r][c] for r in rows for c in columns if r == row or c == column]))
        return ''.join(map(str, map(int, deviations)))

    sequences = [get_deviations(int(n)) for n in observed]
    
    print(sequences)

    #return set(map(lambda x: ''.join(x), combinations(''.join(deviations), len(observed))))
    #temp = [list(chain(map(lambda x: ''.join(x), combinations(d, len(observed))))) for d in deviations]
    
    #return list(set(chain(*temp)))
    #return #list(set(map(lambda x: ''.join(x),))


print(get_pins('369'))
