from src.tasks.classes.logs.logs import Log;
from typing import List;

class LogWriter:
    
    def __init__(self):
        self._array_logs:List[Log] = [];
    
    # -> Metodo que crea los archivo con extension *.log
    def build_log_file(self, log:Log):
        with open(log.path_file, 'w', encoding='utf-8') as log_file:
            log_file.write(f"[{+log.date}]  [FILE_TYPE]   Log File\n");
            
            if log.status:
                log_file.write(f"[{+log.date}]  [SUCCES]      Process completed Successfully\n");
            else:
                log_file.write(f"[{+log.date}]  [ERROR_CODE]  self.error_code\n");
                log_file.write(f"[{+log.date}]  [ERROR]       Process Failure\n");
            
            log_file.write(f"[{+log.date}] [MESSAGE] {self.message}\n");