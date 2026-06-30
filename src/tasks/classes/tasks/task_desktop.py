from src.tasks.classes.tasks.task import Task;

class TaskDesktop(Task):
    
    def __init__(self, title, description, actvity, progress, status, is_active, execution_mode, date_creation, date_execution, date_repeat = None, result = None):
        super().__init__(title, description, actvity, progress, status, is_active, execution_mode, date_creation, date_execution, date_repeat, result);