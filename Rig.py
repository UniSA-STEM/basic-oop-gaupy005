"""
File: Rig.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    # this makes a rig and sets up some starting values
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0

    # getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # to check damage
    def get_damage(self):
        return self.__damage

    # getter to check if the rig is broken
    def is_broken(self):
        return self.__broken

    # to check the upgrade level
    def get_upgrade_level(self):
        return self.__upgrade_level

    # this is used when the rig gets attacked or hit
    def take_hit(self):
        self.__damage = self.__damage + 1
        # if damage gets too high, rig breaks
        if self.__damage >= 2:
            self.__broken = True

    # this just tries to repair the rig back to normal
    def repair(self):
        if self.__broken == True:
            self.__damage = 0
            self.__broken = False
            print(self.__name + " rig repaired.")
        else:
            print(self.__name + " No repair required.")

    # this just prints out how the rig is doing
    def __str__(self):
        if self.__broken == True:
            return self.__name + " - Broken (Damage: " + str(self.__damage) + ")"
        else:
            return self.__name + " - Working (Damage: " + str(self.__damage) + ")"

rig1 = Rig("Rig1")
print(rig1)

rig1.get_name()
rig1.get_damage()
print(rig1)