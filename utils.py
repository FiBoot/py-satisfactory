
def log(title, args):
    print(f'{title}: {args}\n')

def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub_pair(a, b):
    return (a[0] - b[0], a[1] - b[1])

def calc_menu_width(menu_items, min_width, char_width):
    max_length = 0
    for item in menu_items:
        new_length = len(item.text)
        max_length = new_length if new_length > max_length else max_length
    return max_length * char_width + min_width

def calc_recipe_menu_width(recipe_list, component_width):
    max_length = 0
    for recipe in recipe_list:
        new_length = len(recipe.inputs) + len(recipe.outputs)
        max_length = new_length if new_length > max_length else max_length
    return max_length * component_width * 2 # component + text

def contains(item, list):
    try:
        list.index(item)
        return True
    except ValueError:
        return False