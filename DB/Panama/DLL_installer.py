import shutil
import os

def copy_dll_to_system32(dll_path, dll_path2):
    system32_path = os.path.join(os.environ['WINDIR'], 'System32')
    shutil.copy2(dll_path, system32_path)
    shutil.copy2(dll_path2, system32_path)

if __name__ == "__main__":
    dll_path = "dll\\snap7.dll"
    dll_path2 = "dll\\snap7.lib"
    copy_dll_to_system32(dll_path, dll_path2)
