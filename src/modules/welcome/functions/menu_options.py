import os;
import time;

def menu_options_principal():
    time.sleep(2);

    # -> Dependiendo del sistema, borra la consola
    if os.name.__eq__('nt'): #windows
        os.system('cls')
    else: #linux/mac
        os.system('clear')

    time.sleep(2);
    print("**************************************");
    print("|              BONES                 |");
    print("**************************************");
    print("\nWelcome to the menu options program:");
    print("1. Update System Apps");