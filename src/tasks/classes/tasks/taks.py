from datetime import datetime
from typing import List;
from src.tasks.classes.tasks.models.task_execution_mode import TaskExecutionMode;
from src.tasks.classes.tasks.models.task_status import TaskStatus;

class task():
    
    # -> Metodo constructor
    # -> Atr `title` - Titulo de la tarea
    # -> Atr `description` - Descripcion de la tarea
    # -> Atr `progress` - Progreso de la tarea en porcentaje
    # -> Atr `status` - Estado de la tarea
    # -> Atr `is_active` - Estado booleano para saber si la tarea esta activa
    # -> Atr `execution_mode` - Modo de ejecucion de la tarea
    # -> Atr `date_creation` - Fecha de creacion de la tarea
    # -> Atr `date_execution` - Fecha de ejecucion de la tarea
    # -> Atr `date_repeat` - Fechas de repeticion opcional de la tarea
    # -> Atr `result` - Resultado opcional de la tarea
    def __init__(self, title:str, description:str, progress:int, status:TaskStatus, is_active:bool, execution_mode:TaskExecutionMode, date_creation:datetime, date_execution:datetime, date_repeat:List[datetime]|None=None, result:str|None=None):
        self._title = title;
        self._description = description;
        self._progress = progress;
        self._status = status;
        self._is_active = is_active;
        self._execution_mode = execution_mode;
        self._date_creation = date_creation;
        self._date_execution = date_execution;
        self._date_repeat = date_repeat;
        self._result = result;
    
    # -> Get title
    @property
    def title(self)->str:
        return self._title;
    
    # -> Set title
    @title.setter
    def title(self, new_title:str):
        self._title = new_title;
    
    # -> Get description
    @property
    def description(self)->str:
        return self._description;
    
    # -> Set description
    @description.setter
    def description(self, new_description:str):
        self._description = new_description;
    
    # -> Get progress
    @property
    def progress(self)->int:
        return self._progress;
    
    # -> Set progress
    @progress.setter
    def progress(self, new_progress:int):
        self._progress = new_progress;
    
    # -> Get status
    @property
    def status(self)->TaskStatus:
        return self._status;
    
    # -> Set status
    @status.setter
    def status(self, new_status:TaskStatus):
        self._status = new_status;
    
    # -> Get is_active
    @property
    def is_active(self)->bool:
        return self._is_active;
    
    # -> Set is_active
    @is_active.setter
    def is_active(self, new_is_active:bool):
        self._is_active = new_is_active;
    
    # -> Get execution_mode
    @property
    def execution_mode(self)->TaskExecutionMode:
        return self._execution_mode;
    
    # -> Set execution_mode
    @execution_mode.setter
    def execution_mode(self, new_execution_mode:TaskExecutionMode):
        self._execution_mode = new_execution_mode;
    
    # -> Get date_creation
    @property
    def date_creation(self)->datetime:
        return self._date_creation;
    
    # -> Set date_creation
    @date_creation.setter
    def date_creation(self, new_date_creation:datetime):
        self._date_creation = new_date_creation;
    
    # -> Get date_execution
    @property
    def date_execution(self)->datetime:
        return self._date_execution;
    
    # -> Set date_execution
    @date_execution.setter
    def date_execution(self, new_date_execution:datetime):
        self._date_execution = new_date_execution;
    
    # -> Get date_repeat
    @property
    def date_repeat(self)->List[datetime]|None:
        return self._date_repeat;
    
    # -> Set date_repeat
    @date_repeat.setter
    def date_repeat(self, new_date_repeat:List[datetime]|None):
        self._date_repeat = new_date_repeat;
    
    # -> Get result
    @property
    def result(self)->str|None:
        return self._result;
    
    # -> Set result
    @result.setter
    def result(self, new_result:str|None):
        self._result = new_result;