#UTF-8
import subprocess
import os

# удалить стандартный вирус

def antivirus():
    oldPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.expandvars("%userprofile%"),"AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")
    os.chdir(path)
    if not os.path.isdir("Startupp"):
        os.mkdir("Startupp")
    
    with open(path+"\\Startupp\\antivirus.bat", "w+", encoding="utf-8") as w:
        # you need a " " at the beginning otherwise it doesn't work :/
        w.write('@echo off\ndel /q "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Dobriy file.lnk"\nrmdir /s /q "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startupp"\n')

    
    subprocess.Popen(path+"\\Startupp\\antivirus.bat", creationflags=0x08000000)
    # subprocess.Popen("C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startupp\\antivirus.bat")
    
    os.chdir(oldPath)

if __name__ == "__main__":
    antivirus()