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
        self.__name = name
        self.__description = description
        self.__encrypted = False

    # getter and setter for name
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # getter used for description
    def get_description(self):
        return self.__description

    # getter to show encryption status
    def is_encrypted(self):
        return self.__encrypted

    # this will make it encrypted
    def encrypt(self):
        self.__encrypted = True

    # this will turn off encryption
    def decrypt(self):
        self.__encrypted = False

    # this just shows if it's encrypted or not
    def __str__(self):
        if self.__encrypted == True:
            return self.__name + " : " + self.__description + " [Encrypted]"
        else:
            return self.__name + " : " + self.__description





asset1 = Asset("CryptoToken", "Use to acquire or repair rigs")
print(asset1)
asset1.encrypt()
print(asset1)








