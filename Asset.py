"""
File: Asset.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:

    # This makes an asset (token, drive, chip etc.)
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False

    # This makes it encrypted
    def encrypt(self):
        self.encrypted = True

    # This to turn of encrytpion
    def decrypt(self):
        self.encrypted = False

    # This is to show the status if it's encrypted or not
    def __str__(self):
        if self.encrypted == True
            return self.name + ":" + self.description + " encrypted"
        else:
            return self.name + ":" + self.description











