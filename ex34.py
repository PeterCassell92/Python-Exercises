#!/usr/bin/python3

import json

with open("test.json", "r") as f:
    info = json.load(f)

if info["laptops"]:
    print("{} are owned".format(info.get("laptops")))