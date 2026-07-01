# -> clases
from src.tasks.classes.tasks.task import Task;

# -> modulos
from datetime import datetime;
from typing import List;
import subprocess;
import os;

# -> models
from src.tasks.classes.tasks.models.task_execution_mode import TaskExecutionMode;
from src.tasks.classes.tasks.models.task_status import TaskStatus;
from src.tasks.classes.tasks.models.task_activity import TaskActivity;
from src.tasks.classes.tasks.models.task_os import TaskOs;
from src.tasks.classes.tasks.models.task_windows_commands import TaskWindowsCommands;
from src.tasks.classes.tasks.models.task_linux_commands import TaskLinuxCommands;

class TaskDesktop(Task):
    
    def __init__(
        self,
        title: str,
        description: str,
        activity: List[TaskActivity],
        execution_mode: TaskExecutionMode,
        date_creation: datetime,
        date_execution: datetime,
        is_active: bool = True,
        progress: int = 0,
        status: TaskStatus = TaskStatus.PENDING,
        date_repeat: List[datetime] | None = None,
        result: str | None = None,
    ):
        super().__init__(title, description, activity, execution_mode, date_creation, date_execution, is_active, progress, status, date_repeat, result);