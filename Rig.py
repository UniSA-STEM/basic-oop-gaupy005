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
        self._name = name
        self._damage = 0
        self._broken = False
        self._upgrade_level = 0

    # getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # to check damage
    def get_damage(self):
        return self._damage

    # getter to check if the rig is broken
    def is_broken(self):
        return self._broken

    # to check the upgrade level
    def get_upgrade_level(self):
        return self._upgrade_level

    # this is used when the rig gets attacked or hit
    def take_hit(self):
        self._damage = self._damage + 1
        # if damage gets too high, rig breaks
        if self._damage >= 2:
            self._broken = True

    # this just tries to repair the rig back to normal
    def repair(self):
        if self._broken == True:
            self._damage = 0
            self._broken = False
            print(self._name + " rig repaired.")
        else:
            print(self._name + " No repair required.")

    # this just prints out how the rig is doing
    def __str__(self):
        if self._broken == True:
            return self._name + " - Broken (Damage: " + str(self._damage) + ")"
        else:
            return self._name + " - Working (Damage: " + str(self._damage) + ")"

