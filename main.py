from src.utils.logger import create_logger;
from src.tasks.classes.logs.logs import Log;
import os;
if __name__ == "__main__":
    # gestor = create_logger();
    # log1 = Log()
    # log2 = Log()
    # log3 = Log()
    # log4 = Log()
    # log5 = Log()
    try:
        info = os.access(os.path.abspath(__file__), os.X_OK)
        print(info)
    except Exception as error:
        print("Unexpected error.");
        print(error)
        