"""
File: Rig.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
class Rig:
    # this makes a rig and sets up some starting values
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__storage = [
        self.__storage = [
        Asset("Data Spike", "Used in battles"),
        Asset("Data Spike", "Used in battles"),
        Asset("Removable Drive", "Used for extraction")
        ]
        self.__upgrade_level = 0
        self.__capacity = 5

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

    # this just upgrades the rig using a hardware patch
    def upgrade(self):
            self.__upgrade_level += 1
            self.__capacity += 1
            print(self.__name + " upgraded to level " + str(self.__upgrade_level))

    # this just returns the list of stored assets
    def get_storage(self):
        return self.__storage

    # this just adds an asset to storage if there is space
    def store_asset(self, asset):
        if len(self.__storage) >= self.__capacity:
            print(self.__name + " storage is full.")
        else:
            self.__storage.append(asset)
            print(asset.get_name() + " stored in " + self.__name)

    # this just releases an asset by name if not encrypted
    def release_asset(self, asset_name):
        for item in self.__storage:
            if item.get_name().lower() == asset_name.lower():
                if item.is_encrypted() == True:
                    print(item.get_name() + " is encrypted and cannot be moved.")

                self.__storage.remove(item)
                print(item.get_name() + " released from " + self.__name)
                return item
        print(asset_name + " not found in storage.")

    # this just shows the rig condition
    def get_condition(self):
            if self.__broken == True:
                status = "Broken"
            else:
                status = "Pristine"
            return status + " (Level " + str(self.__upgrade_level) + ")"

    # this just prints out how the rig is doing
    def __str__(self):
        if self.__broken == True:
            return self.__name + " - Broken (Damage: " + str(self.__damage) + ")"
        else:
            return self.__name + " - Working (Damage: " + str(self.__damage) + ")"


# Testing

rig1 = Rig("Rig1")
print(rig1)


rig1.get_name()
rig1.get_damage()
print(rig1)