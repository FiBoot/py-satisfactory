import pygame

def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub_pair(a, b):
    return (a[0] - b[0], a[1] - b[1])

def calc_recipe_menu_width(recipes):
     pass

def get_icon(ressource):
        try:
            return pygame.image.load(f'./assets/ressources/{ressource}.png') 
        except:
            return pygame.image.load('./assets/ressources/Not_Found.png')