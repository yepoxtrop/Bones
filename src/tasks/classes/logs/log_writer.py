from src.tasks.classes.logs.logs import Log;
from typing import List;

class LogWriter:
    
    # -> Metodo constructor
    # -> Atr `array_logs` - Arreglo de objetos log
    def __init__(self):
        self._array_logs:List[Log] = [];

    # -> Get array_logs
    @property
    def array_logs(self)->List[Log]:
        return self._array_logs;
    
    # -> Metodo que agrega objetos log a la lista de logs
    def array_logs_add(self, log:Log):
        self.array_logs.append(log);
    
    # -> Metodo que crea los archivo con extension *.log
    def build_log_file(self, log:Log):
        with open(log.path_file, 'w', encoding='utf-8') as log_file:
            log_file.write(log.__str__());
    
    # -> Metodo que crea archivo log en base al ultimo objeto log
    def build_last_log_file(self):
        self.build_log_file(self.array_logs[-1]);
    
    # -> Metodo que crea archivos log segun la cantidad de objetos file que tenga
    def build_all_log_files(self):
        for file in self.array_logs:
            self.build_log_file(file);
    
    # -> Metodo que crea los archivo con extension *.log        
    def __str__(self):
        text = "";
        for file in self.array_logs:
            text += file.__str__();
            text +="\n";
            
        return text;
    
    # -> Metodo del para borrar el objeto logwriter
    def __del__():
        pass;