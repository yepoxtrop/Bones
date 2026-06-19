class log():
    
    # -> Atr de la clase para el id de los logs
    _id_log = 0;
    
    # -> Metodo constructor
    # -> Atr `title` - Titulo del log
    # -> Atr `message` - Mensaje del log
    # -> Atr `status` - Estado boleano para el tipo de log
    # -> Atr `error_code` - Codigo de error opcional si el log es de error
    def __init__(self, title:str, message:str, status:bool, path_file:str, error_code:str|None):
        self._title = title;
        self._message = message;
        self._status = status;
        self._path_file = path_file;
        self._error_code = error_code;
    
    def build_log_file(self):
        with open(self._path_file, 'w', encoding='utf-8') as log_file:
            log_file.write()
        pass