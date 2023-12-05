import os, sys

def ClearTemp() -> None:
    for root, dirs, files in os.walk("C://Windows//Temp"):
        for file in files:
            os.remove(os.path.join(root, file))

def ClearDownloads() -> None:
    for root, dirs, files in os.walk(f"{os.path.join(os.path.expanduser('~'), 'Downloads')}"):
        for file in files:
            os.remove(os.path.join(root, file))

def ClearRecycleBin() -> None:
    os.system('cmd /c "echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin"')

def main() -> None:
    pass

if __name__ == "__main__":
    main()