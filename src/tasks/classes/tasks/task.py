# -> libraries
import requests;
import shutil;

# -> modules
from abc import ABC, abstractmethod;
from datetime import datetime;
from typing import List;
import os;

from src.tasks.classes.tasks.models import task_execution_mode
# -> models
from src.tasks.classes.tasks.models.task_execution_mode import TaskExecutionMode;
from src.tasks.classes.tasks.models.task_status import TaskStatus;
from src.tasks.classes.tasks.models.task_activity import TaskActivity;
from src.tasks.classes.tasks.models.task_os import TaskOs;
from src.tasks.classes.tasks.models.task_windows_commands import TaskWindowsCommands;
from src.tasks.classes.tasks.models.task_linux_commands import TaskLinuxCommands;

# -> utils
from src.utils.define_os import define_os;

class Task(ABC):
    
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
    def __init__(
        self,
        title:str,
        description:str,
        activity:List[TaskActivity],
        execution_mode:TaskExecutionMode,
        date_creation:datetime,
        date_execution:datetime,
        is_active:bool=True,
        progress:int=0,
        status:TaskStatus=TaskStatus.PENDING,
        date_repeat:List[datetime]|None=None,
        result:str|None=None,
    ):
        self._title = title;
        self._description = description;
        self._activity = activity;
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
    
    # -> Get activity
    @property
    def activity(self)->List[TaskActivity]:
        return self._activity;
    
    # -> Set activity
    @activity.setter
    def activity(self, new_activity:List[TaskActivity]):
        self._activity = new_activity;
    
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
    
    # -> Meotod abstracto de ejecucion de la tarea
    @abstractmethod
    def execute(self):
        pass;
    
    # -> Metodo para validar si es posible ejecutar la tarea
    # -> Verofica la conectividad de red
    # -> Permisos locales (admin/root)
    # -> Existencia de comandos específicos
    def validate_exec(self)->bool:
        # -> Validar el tipo de os para la tarea
        operative_system = define_os();
        check_validate_task = self.is_ready_to_execute(operative_system=operative_system);
        return  check_validate_task;
    
    # -> Metodo para validar si la tarea es posible de ejecutarse
    def is_ready_to_execute(self, operative_system:TaskOs) -> bool:
        network = self.validate_network();
        permissions = self.validate_user_permissions(type_os=operative_system);
        commands = self.validate_sys_commands(type_os=operative_system);

        return network and permissions and commands[0];
    
    # -> Metodo para validar la conexion a internet del equipo cliente
    def validate_network(self)->bool:
        try:
            request = requests.get(url="https://1.1.1.1", timeout=5);
            if request.status_code == 200:
                return True;
            else:
                print("Problems with the network");
                return False;
        except requests.exceptions.ConnectionError:
            print("Connection failured");
            return False;
        except requests.exceptions.ConnectTimeout:
            print("Connection timeout");
            return False;
        except Exception as error:
            print("Unexpected error.");
            return False;
        
    # -> Metodo para validar los permisos de admin/root en el os
    def validate_user_permissions(self, type_os:TaskOs)->bool:
        try:
            if type_os == TaskOs.WINDOWS:
                import ctypes
                if ctypes.windll.shell32.IsUserAnAdmin():
                    return True;
                else:
                    return False;
            elif type_os == TaskOs.LINUX:
                if os.geteuid() == 0:
                    return True;
                else:
                    return False;
            elif type_os == TaskOs.MACOS:
                raise NotImplementedError(f"Mac os no implementado aun");
            else:
                raise TypeError(f"Sistema operativo no encontrado");
        except Exception as error:
            print("Unexpected error.");
            return False;

    # -> Metodo para validad la existencia de comandos
    def validate_sys_commands(self, type_os:TaskOs) ->tuple:
        list_missing_commands = [];

        try:
            if type_os == TaskOs.WINDOWS:
                for command in TaskWindowsCommands:
                    if shutil.which(command.value) is None:
                        list_missing_commands.append(command.value);
            elif type_os == TaskOs.LINUX:
                for command in TaskLinuxCommands:
                    if shutil.which(command.value) is None:
                        list_missing_commands.append(command.value);
            elif type_os == TaskOs.MACOS:
                pass
            else:
                raise TypeError(f"Sistema operativo no encontrado");

            return len(list_missing_commands) == 0, list_missing_commands;
        except Exception as error:
            print("Unexpected error.");
            return False;

    @abstractmethod
    def validate_network_components(self):
        pass;

    # -> Metodo para actualizar el progreso de la tarea
    @abstractmethod
    def update_progress(self, new_value:int):
        pass;
    
    # -> Metodo que marca como completada la tarea
    def mark_as_completed(self):
        self.status = TaskStatus.COMPLETED;
    
    # -> Metodo que marca como fallada la tarea
    def mark_as_failed(self, error: str):
        self.status = TaskStatus.FAILED;
    
    # ->
    @abstractmethod
    def create_log(self, message: str, status: bool):
        pass;
    
    # ->
    @abstractmethod
    def log_result(self, result: str):
        pass;
    
    # ->    
    @abstractmethod
    def should_execute_now(self):
        pass;
    
    # ->
    @abstractmethod
    def get_next_execution(self):
        pass;