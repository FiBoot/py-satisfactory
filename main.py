import gc
import pygame
import utils

from enums import *
from game_ressources import GameRessources
from context_menu import ContextMenu
from context_menu_item import ContextMenuBaseItem, SubContextMenuItem, SubContextMenuRecipe

from constructions.list import CONSTRUCTION_LIST
from recipes.list import RECIPE_LIST


class Main():
  def __init__(self):
    # Game Ressource = font, screen & icons
    self.GR = GameRessources()

    self.clock = pygame.time.Clock()
    self.context_menu = ContextMenu()

    self.frame = 0
    self.running = False

    self.constructed_builds = []
    self.active_build = None
    self.active_connection = None
    self.clipboard = None

  # menu callbacks
  def quit(self, _):
    self.running = False

  def create_building(self, rel, construction):
    self.constructed_builds.append(construction(rel))

  def rotate_build(self, _, build):
    build.rotate()

  def delete_building(self, _, build):
    build.disconnect()
    self.constructed_builds.remove(build)
    del build

  def select_recip(self, _, args):
    [build, recipe] = args
    build.set_recipe(recipe)


  # funcs
  def collide_build(self, pos, builds):
    collided = None
    for build in builds:
      build.selected = False
      if build.collide(pos):
        collided = build
    if collided:
      collided.selected = True
    return collided

  def get_selected_build(self, builds):
    for build in builds:
      if build.selected:
        return build
    return None

  def construction_context_menu_items(self, constructions):
    menu_items = []
    for (list_name, construction_list) in constructions:
      sub_context_menu_items = []
      for (name, construction) in construction_list:
        sub_context_menu_items.append(ContextMenuBaseItem(name, self.create_building, construction))  
      menu_items.append(SubContextMenuItem(list_name, sub_context_menu_items))          
    return menu_items

  def get_recipe_list(self, build):
    for [name, recipes] in RECIPE_LIST:
      if name == build.type:
        return recipes
    return None

  def build_recipe_list_menu_items(self, build):
    menu_item = []
    recipe_list = self.get_recipe_list(build)
    if recipe_list:
      recipe_menu_width = utils.calc_recipe_menu_width(recipe_list, EScreen.COMPONENT_WIDTH + EScreen.PADDING)
      for recipe in recipe_list:
        menu_item.append(SubContextMenuRecipe(self.select_recip, build, recipe, recipe_menu_width))
      return SubContextMenuItem('Recipes', menu_item)
    return None

  def draw_grid(self, screen):
    for i in range(0, (EScreen.WIDTH // EScreen.CELL_SIZE) + 1):
      color = EColor.GRID if i % 2 else EColor.GRID_ALT
      pygame.draw.line(screen, color, (i * EScreen.CELL_SIZE, 0), (i * EScreen.CELL_SIZE, EScreen.HEIGHT))
      pygame.draw.line(screen, color, (0, i * EScreen.CELL_SIZE), (EScreen.WIDTH, i * EScreen.CELL_SIZE))


  def start(self):
    # main loop
    self.running = True

    while self.running:
      # events
      for event in pygame.event.get():
        match event.type:
          case pygame.QUIT:
            self.running = False

          case pygame.MOUSEWHEEL:
            if self.context_menu.displayed and self.context_menu.sub_menu:
              self.context_menu.slide_sub_menu(event.y)

          case pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            selected_build = self.get_selected_build(self.constructed_builds)
            if pressed_keys[pygame.K_r] and selected_build:
              selected_build.rotate()
            if pressed_keys[pygame.K_d] and selected_build:
              self.delete_building(None, selected_build)
            if pressed_keys[pygame.K_c]:
              build = self.collide_build(pygame.mouse.get_pos(), self.constructed_builds)
              if build:
                self.clipboard = build.copy()
            if pressed_keys[pygame.K_v] and self.clipboard:
              new_build = self.clipboard.copy()
              new_build.pos = pygame.mouse.get_pos()
              new_build.move((0, 0))
              self.constructed_builds.append(new_build)

          case pygame.MOUSEBUTTONDOWN:
            match event.button: 
              case EButtonType.LEFT:
                # context menu
                if self.context_menu.displayed:
                  menu_collide = self.context_menu.collide(event.pos)
                  if not menu_collide:
                    self.context_menu.close()
                # active build
                self.active_build = self.collide_build(event.pos, self.constructed_builds)
                if self.active_build:
                  self.active_connection = self.active_build.collide_connection(event.pos)

              case EButtonType.RIGHT:
                # open context menu
                build = self.collide_build(event.pos, self.constructed_builds)
                if build:
                  menu_items = [
                    ContextMenuBaseItem('Rotate', self.rotate_build, build),
                    ContextMenuBaseItem('Delete', self.delete_building, build),
                  ]
                  recipe_menu_items = self.build_recipe_list_menu_items(build)
                  if recipe_menu_items:
                    menu_items.insert(0, recipe_menu_items)
                  self.context_menu.open(event.pos, menu_items)
                else:
                  menu_items = self.construction_context_menu_items(CONSTRUCTION_LIST)
                  menu_items.append(ContextMenuBaseItem('Quit', self.quit))
                  self.context_menu.open(event.pos, menu_items)

          case pygame.MOUSEBUTTONUP:
            # connection
            if self.active_connection:
              for build in self.constructed_builds:
                if build != self.active_build and build.collide(event.pos):
                  connection = build.collide_connection(event.pos)
                  if connection:
                    self.active_connection.try_connect(connection)
              self.active_connection = None
            self.active_build = None

          case pygame.MOUSEMOTION:
            # move build
            if self.active_build and not self.active_connection:
              self.active_build.move(event.rel)


      # render
      self.GR.screen.fill(EColor.BACKGROUND)

      self.draw_grid(self.GR.screen)

      for build in self.constructed_builds:
        build.draw(self.GR)
      for build in self.constructed_builds:
        build.draw_connection_lines(self.GR.screen)
      for build in self.constructed_builds:
        build.draw_ratio(self.GR)

      self.context_menu.draw(self.GR)

      # display
      pygame.display.flip()

      # limit fps
      self.clock.tick(EConfig.FPS)

      if self.frame % EConfig.GC_TIMEOUT == 0:
        gc.collect()
      self.frame += 1

    #end loop
    print('Quitting..')
    pygame.quit()


# launch
main = Main()
main.start()