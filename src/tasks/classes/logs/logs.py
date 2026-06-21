from datetime import datetime;
class Log():
    
    # -> Atr de la clase para el id de los logs
    _id_log = 0;
    
    # -> Metodo constructor
    # -> Atr `title` - Titulo del log
    # -> Atr `date` - Fecha del log
    # -> Atr `message` - Mensaje del log
    # -> Atr `status` - Estado boleano para el tipo de log
    # -> Atr `path_file` - Ubicacion del log
    # -> Atr `error_code` - Codigo de error opcional si el log es de error
    def __init__(self, title:str, date:datetime, message:str, status:bool, path_file:str, error_code:str|None=None):
        self._id = Log._id_log + 1;
        Log._id_log += 1;
        self._title = title;
        self._date = date;
        self._message = message;
        self._status = status;
        self._path_file = path_file;
        self._error_code = error_code;
    
    # -> Get id
    @property
    def id(self)->int:
        return self._id;
        
    # -> Get title
    @property
    def title(self)->str:
        return self._title;
    
    # -> Set title
    @title.setter
    def title(self, new_title:str):
        self._title = new_title;
        
    # -> Get date
    @property
    def date(self)->datetime:
        return self._date;
    
    # -> Set title
    @date.setter
    def date(self, new_date:datetime):
        self._date = new_date;
    
    # -> Get message
    @property
    def message(self)->str:
        return self._message;
    
    # -> Set message
    @message.setter
    def message(self, new_message:str):
        self._message = new_message;
    
    # -> Get status
    @property
    def status(self)->bool:
        return self._status;
    
    # -> Set status
    @status.setter
    def status(self, new_status:bool):
        self._status = new_status;
    
    # -> Get path_file
    @property
    def path_file(self)->str:
        return self._path_file;
    
    # -> Set path_file
    @path_file.setter
    def path_file(self, new_path_file:str):
        self._path_file = new_path_file;
    
    # -> Get error_code
    @property
    def error_code(self)->str|None:
        return self._error_code;
    
    # -> Set error_code
    @error_code.setter
    def error_code(self, new_error_code:str|None):
        self._error_code = new_error_code;
    
    # -> Sobreescritura del metodo _str_
    def __str__(self)->str:
        text_log = "";
        text_log += f"[{self.date}]  [FILE_TYPE]   Log File\n";
        if self.status:
                text_log += f"[{self.date}]  [SUCCES]      Process completed Successfully\n";
        else:
            text_log += f"[{self.date}]  [ERROR_CODE]  {self.error_code}\n";
            text_log += f"[{self.date}]  [ERROR]       Process Failure\n";
        text_log += f"[{self.date}]  [MESSAGE]     {self.message}\n";
        return text_log;