

def cakes(recipe:dict, ingredients:dict) -> int:
    
    available = {item: ingredients.get(item, 0) for item in recipe}

    check = [available[item]//recipe[item] for item in recipe]


    return min(check)


r = {'flour': 500, 'sugar': 200, 'eggs': 1}

i = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}

x = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
y = {'sugar': 500, 'flour': 2000, 'milk': 2000}


print(cakes(x, y))

