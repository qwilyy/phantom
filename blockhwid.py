import platform#
import subprocess#
import requests#
import webbrowser#
import time#
from datetime import datetime#
from sys import exit#
#
#                     ->>> READ ME
#        IVE PUT COMMENTS EVERYWHERE (AGAIN) BECAUSE PEOPLE
#        KEPT SPAMMING THIS FREAKING WEBHOOK, NOW IT'S 
#        ENCRYPTED, YOU CAN ALSO SEE ITS SENDING YOUR UUID ONLY!!!
#
disalloweduuids = [""]#
#
leaveruuids = ["63A51763-A475-11E9-8102-9C5A446DAF83", "78524D80-B83F-11DC-94A1-14DAE96F2E4", "87DEC3A-AFEC-B417-A6D2-D8U43AE69AAB1"]#
#
if platform.system() == "Windows":#
    uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip()#
elif platform.system() == "Linux":#
    uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip()#
#
if uuid in disalloweduuids:#
    print("[!] Your UUID is not allowed due to misuse!")#
    input()#
    exit()#
#
if uuid in leaveruuids:#
    print("[!] You sicko thought you could leave the Discord!")#
    time.sleep(1)#
    print("[!] No, no, no. You can't. Be in the Server, make an appeal and accept the consequences.")#
    time.sleep(0.5)#
    print("[!] Note: You can use this after your appeal has been processed.")#
    webbrowser.open("https://discord.gg/auratools")#
    input()#
    exit()#

data = {#
    "embeds": [#
        {#
            "title": "UUID Check",#
            "description": f"UUID: {uuid}\nOpened: {datetime.now()}",#
            "color": 0x7289DA#
        }#
    ]#
}#

data_priv = {
    "embeds": [
        {
            "title": "Someone opened Phantom!"
            "description": f"UUID: {uuid[:-15]}"
            "color": 0x7289DA
#
if uuid:#
    response = requests.post(#
        "https://l.webhook.party/hook/nRBn6m7Ry%2FTrJgqsWP4KpAFbM4F3cF%2F5nIcITfsg0v2aOf24tNlVtvD6gH9sJE7imYjYNS2O5dBbK%2BxEOKKxWYfDCixfqD8yMFoHWqM4YI69JqO1zkcNinMIf8qKvzJ%2BfcUX1ZnF0wLzeYN2AGxWq5DcL7pVZl1GlWvnNNOix72TvHj27OjabPrxDtrTY4qo6KS%2BPRdvN3x59jxaj%2FPz1Ud2DSbwrT8ZL%2BEf0l6uK%2B7cXjkKOowrbRCBhGvDZ%2BQT7ZsTjB9d8H7xGh%2Buf6B0wZfondYaqrNEiVFniIPnJ7VMLwavIlkSU0xynUCGUIItF7FinJZhEdkmqcwJFn%2Fw%2FiEYmYGUcpXPb%2FnTMNhwfbuSCAPl80mWKuTr9KLVaCmXFk1Op2ZtlLc%3D/WAp%2FDRUYSqs00voB",
        json=data#
    )#
    response = requests.post(
        "https://l.webhook.party/hook/nRBn6m7Ry%2FTrJgqsWP4KpAFbM4F3cF%2F5nIcITfsg0v2aOf24tNlVtvD6gH9sJE7imYjYNS2O5dBbK%2BxEOKKxWYfDCixfqD8yMFoHWqM4YI69JqO1zkcNinMIf8qKvzJ%2BfcUX1ZnF0wLzeYN2AGxWq5DcL7pVZl1GlWvnNNOix72TvHj27OjabPrxDtrTY4qo6KS%2BPRdvN3x59jxaj%2FPz1Ud2DSbwrT8ZL%2BEf0l6uK%2B7cXjkKOowrbRCBhGvDZ%2BQT7ZsTjB9d8H7xGh%2Buf6B0wZfondYaqrNEiVFniIPnJ7VMLwavIlkSU0xynUCGUIItF7FinJZhEdkmqcwJFn%2Fw%2FiEYmYGUcpXPb%2FnTMNhwfbuSCAPl80mWKuTr9KLVaCmXFk1Op2ZtlLc%3D/WAp%2FDRUYSqs00voB",
        json=data_priv
    )
#
