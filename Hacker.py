"""
File: Hacker.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


from Asset import Asset
from Rig import Rig
class Hacker:

    # this creates a hacker with a name, trace level, rigCount and inventory
    def __init__(self, name):
        self.__name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs")]
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


    # this just lets the hacker acquire a rig using one CryptoToken
    def acquire_rig(self, rig=None):
        # check if hacker already has a rig
        if self.__rigCount is not None:
            print(self.__name + " already owns a rig.")
            return

    # This looks for a CryptoToken in the inventory
        for asset in self.__inventory:
            if asset.get_name().lower() == "cryptotoken":
                # spend the token to obtain a rig
                self.__inventory.remove(asset)

                # create a rig if none was passed in
                if rig is None:
                    rig = Rig(self.__name + "'s Rig")

                # assign the rig to rigCount
                self.__rigCount = rig
                print(self.__name + " has acquired a new rig: " + rig.get_name())
                return

        # if we finished the loop without returning, then no token was found
        print(self.__name + " does not own a CryptoToken.")

    # this just increases the hacker's trace level by an amount
    def increase_trace(self, amount):
        self.__trace_level = self.__trace_level + amount
        print(self.__name + "'s trace level increased by " + str(amount))

    # this just decreases the hacker's trace level by an amount
    def decrease_trace(self, amount):
        self.__trace_level = self.__trace_level - amount

        # Trace level do not go below 0
        if self.__trace_level < 0:
            self.__trace_level = 0
        print(self.__name + "'s trace level decreased by " + str(amount))

    # this just upgrades the hacker's rig using a Hardware Patch
    def upgrade_rig(self):
        # this checks if hacker has a rig
        if self.__rigCount is None:
            print(self.__name + " does not have a rig to upgrade.")
            return

        # To look for a Hardware Patch in the inventory
        for asset in self.__inventory:
            if asset.get_name().lower() == "hardware patch":
                # To use the patch
                self.__inventory.remove(asset)

                # To upgrade the rig
                self.__rigCount.upgrade()
                print(self.__name + " used a Hardware Patch to upgrade their rig.")
                return

        # if no patch found
        print(self.__name + " does not have a Hardware Patch.")

        # this just searches the hacker inventory for an asset by name and returns it (removes it)
    def scan_inventory(self, asset_name):
        for asset in self.__inventory:
            if asset.get_name().lower() == asset_name.lower():
                self.__inventory.remove(asset)
                return asset
        return None

    # this just stores an asset from hacker inventory into the rig
    def store_to_rig(self, asset_name):
        if self.__rigCount is None:
            print(self.__name + " has no rig to store items in.")
            return

        # this to find the asset in hacker's inventory
        for asset in self.__inventory:
            if asset.get_name().lower() == asset_name.lower():
                if asset.is_encrypted():
                    print(asset.get_name() + " is encrypted and cannot be stored.")
                    return

                # to store the asset
                if len(self.__rigCount.get_storage()) < 5:  # assuming capacity is 5
                    self.__rigCount.store_asset(asset)
                    self.__inventory.remove(asset)
                else:
                    print(self.__name + "'s rig storage is full.")
                return

        print(asset_name + " not found in inventory.")








