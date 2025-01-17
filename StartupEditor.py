import os
import sys
import subprocess
import winreg

class StartupEditor:
    def __init__(self):
        self.startup_registry_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        self.startup_folder_path = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")

    def list_startup_items(self):
        print("Listing all startup items...\n")
        self.list_registry_startup_items()
        self.list_folder_startup_items()
    
    def list_registry_startup_items(self):
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.startup_registry_path, 0, winreg.KEY_READ) as key:
                i = 0
                while True:
                    try:
                        name, value, _ = winreg.EnumValue(key, i)
                        print(f"Registry: {name} -> {value}")
                        i += 1
                    except OSError:
                        break
        except Exception as e:
            print(f"Failed to read registry startup items: {e}")

    def list_folder_startup_items(self):
        try:
            for item in os.listdir(self.startup_folder_path):
                print(f"Folder: {item}")
        except Exception as e:
            print(f"Failed to read folder startup items: {e}")

    def add_startup_item(self, name, command, location='registry'):
        if location == 'registry':
            self.add_registry_startup_item(name, command)
        elif location == 'folder':
            self.add_folder_startup_item(name, command)
        else:
            print("Invalid location specified. Must be 'registry' or 'folder'.")

    def add_registry_startup_item(self, name, command):
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.startup_registry_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, name, 0, winreg.REG_SZ, command)
            print(f"Added registry startup item: {name}")
        except Exception as e:
            print(f"Failed to add registry startup item: {e}")

    def add_folder_startup_item(self, name, command):
        try:
            shortcut_path = os.path.join(self.startup_folder_path, f"{name}.lnk")
            subprocess.run(['powershell', '-Command', f'$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut("{shortcut_path}"); $Shortcut.TargetPath = "{command}"; $Shortcut.Save()'])
            print(f"Added folder startup item: {name}")
        except Exception as e:
            print(f"Failed to add folder startup item: {e}")

    def remove_startup_item(self, name, location='registry'):
        if location == 'registry':
            self.remove_registry_startup_item(name)
        elif location == 'folder':
            self.remove_folder_startup_item(name)
        else:
            print("Invalid location specified. Must be 'registry' or 'folder'.")

    def remove_registry_startup_item(self, name):
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.startup_registry_path, 0, winreg.KEY_WRITE) as key:
                winreg.DeleteValue(key, name)
            print(f"Removed registry startup item: {name}")
        except Exception as e:
            print(f"Failed to remove registry startup item: {e}")

    def remove_folder_startup_item(self, name):
        try:
            shortcut_path = os.path.join(self.startup_folder_path, f"{name}.lnk")
            os.remove(shortcut_path)
            print(f"Removed folder startup item: {name}")
        except Exception as e:
            print(f"Failed to remove folder startup item: {e}")

if __name__ == "__main__":
    editor = StartupEditor()
    editor.list_startup_items()
    # Example usage
    editor.add_startup_item("MyApp", "C:\\Path\\To\\MyApp.exe", location='registry')
    editor.remove_startup_item("MyApp", location='registry')