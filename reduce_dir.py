
opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}

def reduce_dirs(dirs:list) -> list:

    for i, d in enumerate(dirs[1:], start=1):
        
        if d == opposites[dirs[i-1]]:

            dirs.remove(d)

            return reduce_dirs(dirs)

    return dirs
d = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
#d = ['NORTH', 'WEST', 'SOUTH', 'EAST']
print(reduce_dirs(d))

