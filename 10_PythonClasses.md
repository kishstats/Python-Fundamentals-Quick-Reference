# Python Classes

```python
from abc import ABCMeta, abstractmethod  # Abstract Base Class


class Player(metaclass=ABCMeta):
    sport = 'football'
    league = 'NFL'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def full_name(self):
        return self.fname + ' ' + self.lname

    @abstractmethod
    def get_key_stats():
        pass


class DefensivePlayer(Player):
    def __init__(self, fname, lname, tackles, interceptions, sacks):
        super(DefensivePlayer, self).__init__(fname, lname)
        self.tackles = tackles
        self.interceptions = interceptions
        self.sacks = sacks

    def get_key_stats(self):
        return (self.tackles, self.interceptions, self.sacks)


class OffensivePlayer(Player):

    def __init__(self, fname, lname, passing_yards=0, rushing_yards=0,
                 receiving_yards=0):
        super(OffensivePlayer, self).__init__(fname, lname)
        self.passing_yards = passing_yards
        self.rushing_yards = rushing_yards
        self.receiving_yards = receiving_yards

    @classmethod
    def change_league(cls, league_name):
        cls.league = league_name

    @staticmethod
    def get_positions():
        return ['quarterback', 'running back', 'wide receiver', 'tight end',
                'tackle', 'guard', 'center']

    def get_key_stats(self):
        return (self.passing_yards, self.rushing_yards, self.receiving_yards)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return '{self.__class__.__name__}("{self.fname}", "{self.lname}", {self.passing_yards}, {self.rushing_yards}, {self.receiving_yards})'.format(self=self)


player = OffensivePlayer('russell', 'wilson', 4500, 550, 0)
print(player.lname)  # wilson
# print(player.full_name())  # changed to property, will result in TypeError
print(player.full_name)  # russell wilson

print(player.__dict__)  # {'fname': 'russell', 'lname': 'wilson', 'passing_yards': 4500, 'rushing_yards': 550, 'receiving_yards': 0}

player2 = OffensivePlayer('dez', 'bryant', 0, 40, 1200)
print(player2.lname)  # bryant
print(player2.full_name)  # dez bryant
print(player2.receiving_yards)  # 1200
print(player2.league)  # NFL

player3 = DefensivePlayer('Kahlil', 'Mack', 110, 1, 10)
print(player3.lname)  # Mack
print(player3.full_name)  # Kahlil Mack
print(player3.tackles)  # 110

# OffensivePlayer.league = 'NCAA'
OffensivePlayer.change_league('NCAA')

rookie = OffensivePlayer('joe', 'rookie', receiving_yards=55)
print(rookie.lname)  # rookie
print(rookie.full_name)  # joe rookie
print(rookie.receiving_yards)  # 55
print(rookie.passing_yards)  # 0

print(rookie.league)  # NCAA
print(rookie.get_positions())  # ['quarterback', 'running back', 'wide receiver', 'tight end', 'tackle', 'guard', 'center']


# Magic Methods
print(player.__dict__)  # {'fname': 'russell', 'lname': 'wilson', 'passing_yards': 4500, 'rushing_yards': 550, 'receiving_yards': 0}
print(str(player))  # {'fname': 'russell', 'lname': 'wilson', 'passing_yards': 4500, 'rushing_yards': 550, 'receiving_yards': 0}
print(repr(player))  # OffensivePlayer("russell", "wilson", 4500, 550, 0)

```
