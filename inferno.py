import platform#
import subprocess#
import requests#
from datetime import datetime#
from sys import exit#
#
# Read me: 
# I've added comments everywhere to show you that I can only access your UUID and the time you opened it
# Like just look at the code, it only accesses your UUID and checks if its in the list.
# Also if you decided to spam this WebHook then props to you for being an asshole :D
#
disalloweduuids = [""]  # List of disallowed UUIDs if your dumbahh couldn't figure it out
#
if platform.system() == "Windows":#
    uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()#
elif platform.system() == "Linux":#
    uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip()#
#
uuid = f"INFERNO.{uuid}"#
#
if uuid in disalloweduuids:#
    print("[!] Your UUID is not allowed due to misuse!")#
    input()#
    exit()#
#
data = {#
    "embeds": [#
        {#
            "title": "UUID Check",#
            "description": f"UUID: {uuid}\nOpened: {datetime.now()}",#
            "color": 0xFC2803#
        }#
    ]#
}#
#
if uuid:#
    response = requests.post("https://discord.com/api/webhooks/1277332995145072711/AaWEF-RUI5iv610R7JBU8b7iVywJq6Ecew7zCZqPm62Ib3ZwD8IPp0WsCCNcnmc1NxNm", json=data)#
