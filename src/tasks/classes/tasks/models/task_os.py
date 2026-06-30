from enum import Enum;

class TaskOs(Enum):
    WINDOWS = "windows"
    LINUX = "linux"
    WINDOWS_FILE_TEST = "C:\\Windows\\System32\\drivers\\etc\\hosts"
    LINUX_FILE_TEST = "/etc/shadow"