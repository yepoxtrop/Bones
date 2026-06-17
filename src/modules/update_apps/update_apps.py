import os;
import subprocess;

def update_apps():
    # -> Funcion para revalidar el sistema operativo antes de actualizar
    pass;

def update_apps_windows():
    # ->Valdar la existencia del paquete winget
    try:
        winget_version = subprocess.run("winget -v", check=True, capture_output=True, text=True);
        
        if not winget_version.stdout.__eq__(''):
            winget_list = subprocess.run("winget update", check=True, capture_output=True, text=True);
            
            print(list(winget_list.stdout))
    except:
        print("Fall");    
    pass;

def update_apps_linux():
    pass;

update_apps_windows()