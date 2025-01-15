import platform#
import subprocess#
import requests#
import webbrowser#
import time#
from datetime import datetime#
from sys import exit#

disalloweduuids = [""]

leaveruuids = ["63A51763-A475-11E9-8102-9C5A446DAF83", "78524D80-B83F-11DC-94A1-14DAE96F2E4", "87DEC3A-AFEC-B417-A6D2-D8U43AE69AAB1"]

if platform.system() == "Windows":
    uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()
elif platform.system() == "Linux":
    uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip()

if uuid in disalloweduuids:
    print("[!] Your UUID is not allowed due to misuse!")
    input()
    exit()

if uuid in leaveruuids:
    print("[!] You sicko thought you could leave the Discord!")
    time.sleep(1)
    print("[!] No, no, no. You can't. Be in the Server, make an appeal and accept the consequences.")
    time.sleep(0.5)
    print("[!] Note: You can use this after your appeal has been processed.")
    webbrowser.open("https://discord.gg/auratools")
    input()
    exit()

data = {
    "embeds": [
        {
            "title": "UUID Check",
            "description": f"UUID: {uuid}\nOpened: {datetime.now()}",
            "color": 0x7289DA
        }
    ]
}

if uuid:
    response = requests.post(
        "https://discord.com/api/webhooks/1329076411868119143/7XkG1-SJG-_B5_B4xjdL7OZJwBW3wQc-seRGqs4ayeI8I2iBgtBqNEgi95nBA0TLGgVY",
        json=data
    )
