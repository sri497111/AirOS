#Air is a Kernal-based operating system in its alpha stage. It is currently being developed by Sricharan Athanti(MoonDEV)
import os
import sys
from datetime import datetime
#__________________________________________________________
with open('version.txt', 'r') as version_file:
    version = version_file.read()
time = datetime.now().strftime("%H:%M:%S")
info = f'''
{time}
Air Alpha {version}

As of March 2025, project Air has been initiated. Read patch.txt for
more info about this os version. 
'''

print(info)
# main_________________________________________________________
username = 'user'
path = './disk/'
def main():
    global path
    while True:
        time = datetime.now().strftime("%H:%M:%S:")
        filelist = os.listdir(path)
        filelist_parsed = "\n".join(filelist)
        kernel = input(f"Air@{username} X:{path[1:]} ").strip()
        if kernel.lower() == "shutdown":
            break
        elif kernel.lower() == "path":
            print(path)
        elif kernel.startswith("cd "):
            try:
                newdir = kernel[3:].strip()
                newpath = f"{path.rstrip('/')}/{newdir}"

                previous_path = open('previous_path.txt', 'r+')
                
                if "." in newdir:
                    print("The location is not a folder or path.")
                    continue
                if os.path.exists(path) and os.path.isdir(path):
                    path = newpath
                else:
                    print("The Directory is non-existent")
            except:
                print("The location is not a folder or path.")
        elif kernel.lower() == "time":
            print(time)
        elif kernel.startswith("echo "):
            print(kernel[5:])
        elif kernel.startswith("echo"):
            print("Usage - echo [text]")
        elif kernel.lower() == "ls":
            print(filelist_parsed)
        elif kernel.startswith(""):
            continue
        else:
            print(f"{repr(kernel)} is not a recognized command, program or operation")
        

if __name__ == "__main__":
    main()
