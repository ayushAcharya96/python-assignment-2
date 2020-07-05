'''
16. Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player.
'''

class Mario:
  def __init__(self, x_position, y_position):
    self.x_position = x_position
    self.y_position = y_position
    self.in_air = False
    self.is_big = False
    self.is_super = False
  
  def move(self):
    pass

  def jump(self):
    pass

  def shoot_fireball(self):
    pass

  def check_collision(self):
    pass

  