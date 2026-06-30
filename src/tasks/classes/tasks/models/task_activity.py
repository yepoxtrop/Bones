from enum import Enum;

class TaskActivity(Enum):
    DELETE_TEMPORAL_FILES = "delete_temporal_files";
    UPDATE_OS = "update_os";
    INSTALL_APPLICATION = "install_aplication";
    DOWNLOAD_DATA = "download_data";
    CLEAN_DISK = "clean_disk";