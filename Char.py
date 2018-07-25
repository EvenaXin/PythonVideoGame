import math
import random


class Char:
    Name = ""
    Agi = 0
    Str = 0
    Bod = 0
    Mod = 0
    Mana_Max = 0
    Mana_Eff = 0
    Health_Max = 0
    Sta_Eff = 0
    Sta_Max = 0

    @staticmethod
    def Char_Def() -> object:
        Name = str(input("What is your name? "))
        Agi = int(input("How agile are you? "))
        Str = int(input("How strong are you? "))
        Bod = int(input("How tough are you? "))
        Mod = int(input("How well rounded are you? "))
        Mana_Max = int(input("How much magic can you hold? "))
        Mana_Eff = int(input("How much magic do you use? "))
        Sta_Eff = int(input("How efficiently do you move? "))
        pass

    @staticmethod
    def MaxHP():
        Health_Max = math.floor((Char.Bod * Char.Mod) / 2)
        pass

    @staticmethod
    def MaxSta(int):
        Sta_Max = math.floor((Agi * Mod) / 2)
        pass

    pass


CharMain = Char()
Player1 = CharMain.__class__
Player2 = CharMain.__class__
Player1.Char_Def()
Player1.MaxHP()
print("Name: " + Player1.Name)
print("MaxHP: " + str(Player1.Health_Max))
print("CurrentHP: " + str(Player1.Health_Max))
print("MaxMP: " + str(Player1.Mana_Max))
print("CurrentMP: " + str(Player1.Mana_Max))
print("MaxStamina: " + str(Player1.Sta_Max))
