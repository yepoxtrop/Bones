import os;
from src.tasks.classes.tasks.models.task_os import TaskOs;

def define_os()->TaskOs:
    opertive_system = os.name;
    if opertive_system == 'nt':
        return TaskOs.WINDOWS;
    elif opertive_system == 'posix':
        return TaskOs.LINUX;