from enum import Enum;

class TaskTypeJob(Enum):
    UPDATE_OS = "manual"
    SCHEDULED = "scheduled"
    RECURRING = "recurring"