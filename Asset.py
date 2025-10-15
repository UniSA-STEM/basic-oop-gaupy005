"""
File: Asset.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    # this makes an asset which has a name, description and encryption
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._encrypted = False

    # getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # getter used for description
    def get_description(self):
        return self._description

    # getter to show encryption status
    def is_encrypted(self):
        return self._encrypted

    # this will make it encrypted
    def encrypt(self):
        self._encrypted = True

    # this will turn off encryption
    def decrypt(self):
        self._encrypted = False




