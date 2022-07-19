import os

with os.scandir("/Users/jeremy/Desktop/siteweb_techno") as entries:
    for entry in entries:
        print(entry.name)