def complete_form(urlFormulario:str)->bool:


    try:
        # -> Si la url esta vacia falla
        if len(urlFormulario) == 0:
            print("URL is empty");
            return False;


        return True;

    except ValueError:
        #-> Si la url no es un string falla
        print("URL is not a string");
        return False;