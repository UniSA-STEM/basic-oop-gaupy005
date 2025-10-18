"""
File: Hacker.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    # this creates a hacker with a name, trace level, rigCount and inventory
    def __init__(self, name):
        self.__name = name
        self.__trace_level = 0
        self.__inventory = []
        self.__rigCount = None

    # getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # to check the trace level
    def get_trace_level(self):
        return self.__trace_level

    # to check the rig count
    def get_rigCount(self):
        return self.__rigCount

# this just adds an asset to the hacker's inventory
    def add_asset(self, asset):
        self.__inventory.append(asset)
        print(asset.get_name() + " added to " + self.__name + "'s inventory.")