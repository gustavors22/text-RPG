import random

class Game_rules(object):
	"""Aqui fica toda as regras do jogo"""
	def __init__(self):
		self.hero_life = 10
		self.enemy_life = 10

	def roll_dice(self):
		return random.randint(1,6)

	def get_life_player(self):
		return self.hero_life

	def set_life_player(self, new_value):
		self.hero_life = new_value

	def get_enemy_life(self):
		return self.enemy_life

	def set_enemy_life(self, new_value):
		self.enemy_life = new_value
