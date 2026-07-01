import platform
from src.tasks.classes.tasks.models.task_os import TaskOs;

def define_os()->TaskOs:
    operative_system = platform.system()
    
    if operative_system == 'Windows':
        return TaskOs.WINDOWS
    elif operative_system == 'Linux':
        return TaskOs.LINUX
    elif operative_system == 'Darwin': # No funcionara actualmente
        return TaskOs.MACOS
    else:
        raise ValueError(f"Sistema operativo no soportado: {operative_system}")