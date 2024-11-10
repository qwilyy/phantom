import platform, subprocess, sys, requests, time, datetime# comments so you know there is no ratted shit, I will probably not even use this.
from sys import exit# 
from datetime import datetime#
#
disalloweduuids = [
  "6A542136-E167-11EA-BF7C-27EF3FED1A00"
]#
#
if platform.system() == "Windows":#
        uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()#
elif platform.system() == "Linux":#
        uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip()#
#
if uuid in disalloweduuids:#
  print("[!!!] Your UUID is not allowed due to misuse!                       ")#
  input()#
  exit()#
#
data = {
  "content": f"UUID: {uuid}\nOpened: {datetime.now()}"
}#
#
if uuid:
  "Nothing but your UUID, and the Time you opened it will be sent to this webhook(I don't care if u spam it, I muted it)"
  response = requests.post("https://discord.com/api/webhooks/1277332995145072711/AaWEF-RUI5iv610R7JBU8b7iVywJq6Ecew7zCZqPm62Ib3ZwD8IPp0WsCCNcnmc1NxNm", json=data)#
