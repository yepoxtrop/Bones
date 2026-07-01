from enum import Enum;
from src.tasks.classes.tasks.models.task_windows_commands import TaskWindowsCommands;
from src.tasks.classes.tasks.models.task_linux_commands import TaskLinuxCommands;

class TaskActivity(Enum):
    # -> [CLAVE_ACTIVIDAD] = nombre_tarea, ((comandos_windows),(comandos_linux)), descripcion_tarea
    DELETE_TEMPORAL_FILES = "delete_temporal_files",((),()),"";
    UPDATE_OS = (
        "update_os",
        ((
            TaskWindowsCommands.WINGET
         ),(
            TaskLinuxCommands.APT,
            TaskLinuxCommands.GET,
            TaskLinuxCommands.UPDATE,
        )),
        ""
    );
    INSTALL_APPLICATION = "install_aplication",((),()),"";
    DOWNLOAD_DATA = "download_data",((),()),"";
    CLEAN_DISK = "clean_disk",((),()),"";