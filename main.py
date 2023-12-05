import os, sys

def MenuOptions() -> str:
    """
    Displays the menu options for the user.

    Returns:
    str: User prompt for selecting an option.
    """
    
    return """Choose one of the options from the menu below:\n
                1) Temp Files
                2) Downloads 
                3) Recycle Bin
                4) Exit
              Option: """

def ClearTemp() -> None:
    """
    Clears temporary files in the 'C://Windows//Temp' directory.

    Raises:
    PermissionError: If the script doesn't have the necessary permissions.
    """
    
    for root, dirs, files in os.walk("C://Windows//Temp"):
        for file in files:
            os.remove(os.path.join(root, file))

def ClearDownloads() -> None:
    """
    Clears files in the user's 'Downloads' directory.

    Raises:
    PermissionError: If the script doesn't have the necessary permissions.
    """
    
    for root, dirs, files in os.walk(f"{os.path.join(os.path.expanduser('~'), 'Downloads')}"):
        for file in files:
            os.remove(os.path.join(root, file))

def ClearRecycleBin() -> None:
    """
    Empties the recycle bin using PowerShell commands.

    Raises:
    PermissionError: If the script doesn't have the necessary permissions.
    """
    
    os.system('cmd /c "echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin"')

def main() -> None:
    """
    Main function to execute the script.

    This function runs a loop allowing the user to choose different options
    to clean specific directories. It handles permission errors gracefully.
    """
    
    while True:
        option = int(input(MenuOptions()))
        if option == 1:
            ClearTemp()
        elif option == 2:
            try:
                ClearDownloads()
            except PermissionError:
                print("You do not have the necessary permissions to delete of the files in this folder!")
        elif option == 3:
            ClearRecycleBin()
        elif option == 4:
            input("Press enter to exit the application...")
            sys.exit(0)
        else:
            print(f'Option: "{option}" is not a valid option! ')

if __name__ == "__main__":
    main()