from src.tasks.classes.logs.log_writer import LogWriter;

# -> Funcion que devuelve un objeto logwriter
def create_logger()->LogWriter:
    return LogWriter();