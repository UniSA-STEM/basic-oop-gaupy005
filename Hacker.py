"""
File: Hacker.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:
    # this creates a hacker with a name, trace level and inventory
    def __init__(self, name):
        self.__name = name
        self.__trace_level = 0
        self.__inventory = []
        self.__rig = None

