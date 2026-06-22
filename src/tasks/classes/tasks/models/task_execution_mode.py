from enum import Enum;

class TaskExecutionMode(Enum):
    MANUAL = "manual"
    SCHEDULED = "scheduled"
    RECURRING = "recurring"