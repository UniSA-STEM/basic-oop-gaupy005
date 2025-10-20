"""
File: main.py
Description: <Assignment 1 Basic OOP.>
Author: <Prince Gautam>
ID: <110351192>
Username: <GAUPY005>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig
from Hacker import Hacker

print("=== Setup ===")
h = Hacker("Prince")
print("Hacker created:", h.get_name())
print("Trace level:", h.get_trace_level())
print()

# This to test acquire_rig
print("=== Acquire rig ===")
h.acquire_rig()
if h.get_rigCount() is not None:
    print("Rig owned:", h.get_rigCount().get_name())
else:
    print("No rig owned")
print()


# This Adds a Data Spike and launches an attack on a new Rig
print("=== Add Data Spike and attack ===")
h.add_asset(Asset("Data Spike", "Used in battles"))
victim = Rig("VictimRig")
print("Before attack:", victim)
h.launch_attack(victim)
print("After attack:", victim)
print()

# This uses a Hardware Patch to upgrade rig
print("=== Upgrade rig ===")
h.add_asset(Asset("Hardware Patch", "Upgrades rigs"))
h.upgrade_rig()
if h.get_rigCount() is not None:
    print("Rig condition now:", h.get_rigCount().get_condition())
print()

# This stores an unencrypted asset into hacker's rig and retrieves it
print("=== Store and retrieve asset ===")
h.add_asset(Asset("Report", "Stolen file"))
h.store_to_rig("Report")
h.retrieve_from_rig("Report")
print()

# This Encrypts an asset which will require a Security Chip
print("=== Encrypt asset ===")
h.add_asset(Asset("Secret.txt", "Sensitive"))
h.add_asset(Asset("Security Chip", "Used to encrypt/decrypt"))
h.encrypt_asset("Secret.txt")
print()

# This here is a test extraction from a broken rig
print("=== Extract from broken rig ===")
# create a rig with some assets (it already has spikes + drive)
target = Rig("OldRig")


# This puts a cleared asset into target, and an encrypted one to test filtering
target.store_asset(Asset("Notes", "Important"))
enc = Asset("LockedDoc", "Encrypted doc")
enc.encrypt()
target.store_asset(enc)
# Break the rig (two hits)
target.take_hit()
target.take_hit()


print("Target rig after being broken:", target.get_condition())

# This gives hacker a Removable Drive and extract assets
h.add_asset(Asset("Removable Drive", "Used for extraction"))
h.extract_assets(target)

# This shows the hacker’s inventory after extraction
print("Hacker inventory after extraction:")
for item in h._Hacker__inventory:   # (just for testing)
    print("-", item.get_name())

print("\n=== Tests finished ===")

