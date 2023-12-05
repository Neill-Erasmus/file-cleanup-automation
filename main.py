import os, sys

def MenuOptions() -> str:
    return """Choose one of the options from the menu below:\n
                1) Temp Files
                2) Downloads 
                3) Recycle Bin
                4) Exit
              Option: """

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