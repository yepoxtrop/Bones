import time;

def welcome_message():
    mensaje = [
        'mmmmmm      mmmm    mmm   mm  mmmmmmmm    mmmm',   
        '##""""##   ##""##   ###   ##  ##""""""  m#""""#',  
        '##    ##  ##    ##  ##"#  ##  ##        ##m',      
        '#######   ##    ##  ## ## ##  #######    "####m', 
        '##    ##  ##    ##  ##  #m##  ##             "##', 
        '##mmmm##   ##mm##   ##   ###  ##mmmmmm  #mmmmm#"', 
        '""""""""    """"    ""   """  """"""""   """""'
    ]

    for linea in mensaje:
        for letra in linea:
            print(letra, end=" ")
            time.sleep(0.05)
        print()

    time.sleep(0.08);
    print("Por Luis Diaz\n");